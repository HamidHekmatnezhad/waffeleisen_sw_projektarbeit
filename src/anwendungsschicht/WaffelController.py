from enum import Enum
from steuerungsschicht_regelungsschicht.PIDRegler import PIDRegler
from steuerungsschicht_regelungsschicht.Solltabelle import Solltabelle
from Benutzeroberfläche_userinterface.SimpleGUI import SimpleGUI
from datenhaltungsschicht.ConfigLoader import ConfigLoader
from hardwareAbstraktionsschicht.AkustikSignalgeber import AkustikSignalgeber
from datenhaltungsschicht.DataLogger import DataLogger

class Zustand(Enum):
    """Definiert die möglichen Zustände des Waffeleisens."""
    STANDBY = "STANDBY"
    AUFHEIZEN = "AUFHEIZEN"
    BEREIT = "BEREIT"
    FEHLER = "FEHLER"

class WaffelController:
    """
    Hauptkoordinator der Anwendung (Application Layer).
    Verantwortlich für die Zustandsverwaltung und die Steuerung des Regelkreises.
    """
    
    _regler: PIDRegler
    _tabelle: Solltabelle
    _gui: SimpleGUI
    
    _aktuellerZustand: Zustand = Zustand.STANDBY
    _aktueller_grad: int = 3
    _sollTemp: int = 180
    _isHeizungAktiv: bool = False
    
    # Statische Referenz für Singleton-ähnlichen Zugriff 
    _instance = None

    def __init__(self, gui: SimpleGUI, regler: PIDRegler, tabelle: Solltabelle):
        """Initialisiert den Controller und seine Abhängigkeiten."""
        self._gui = gui
        self._regler = regler
        self._tabelle = tabelle
        
        self._sollTemp = self._tabelle.holeSolltemperatur(self._aktueller_grad)
        self._regler.setzeSolltemperatur(self._sollTemp)
        self._gui.zeigeZustand(Zustand.STANDBY.value)
        print("--- INFO: WaffelController initialisiert.")

        # Sprint 2: buzzer and config loader        
        self.buzzer = AkustikSignalgeber()
        self.config_loader = ConfigLoader()
        self.konfiguration = self.config_loader.laod_lang("DE")

        # Sprint 3: DataLogger initialisieren und Start-Event loggen
        self.logger = DataLogger()
        self.logger.log_system_event("System gestartet - Waffeleisen bereit.")
        
        self.text_bereit = self.konfiguration["BEREIT"]
        self.text_aufheizen = self.konfiguration["AUFHEIZEN"]

    def verarbeiteEingabe(self, delta_grad: int) -> None:
        """
        Verarbeitet die Eingabe vom Benutzer (von ButtonInput ausgelöst).
        """
        neuer_grad = self._aktueller_grad + delta_grad
        
        if 1 <= neuer_grad <= 5:
            self._aktueller_grad = neuer_grad
            self._sollTemp = self._tabelle.holeSolltemperatur(neuer_grad)
            self._regler.setzeSolltemperatur(self._sollTemp)
            print(f"CONTROLLER: Neuer Grad {neuer_grad} gewählt. Soll-Temperatur: {self._sollTemp}°C")
            
            self._gui.zeigeZustand(f"Grad {self._aktueller_grad} / {self._sollTemp}°C")

    def starteBackvorgang(self) -> None:
        """
        Startet den eigentlichen Aufheiz- und Backvorgang.
        """
        if self._aktuellerZustand in (Zustand.STANDBY, Zustand.BEREIT):
            self._aktuellerZustand = Zustand.AUFHEIZEN
            self._gui.zeigeZustand(self.text_aufheizen)
            self._isHeizungAktiv = True
            print(f"CONTROLLER: Backvorgang gestartet. {self.text_aufheizen}...")

    def runRegelkreisIteration(self) -> None:
        """
        Führt eine Iteration des Regelkreises aus (Kern der Applikation).
        Diese Methode wird zyklisch von einem Timer/Scheduler aufgerufen.
        """
        if self._aktuellerZustand == Zustand.AUFHEIZEN:
            
            # 1. Ist-Temperatur lesen 
            ist_temp = self._regler.sensor.leseTemperatur() 

            # logger
            self.logger.log_messwert(ist_temp)
            
            # 2. Stellgröße berechnen 
            leistung = self._regler.calculateHeatingPower(ist_temp)
            
            # 3. Hardware ansteuern 
            self._regler.heater_aktuator.setzeLeistung(leistung) 
            
            # 4. Simulation der Temperatur im Sensor
            self._regler.sensor.setze_simulierte_temperatur(
                ist_temp + (leistung * 0.5) 
            )

            # 5. Zustandsprüfung
            if ist_temp >= self._sollTemp - 2: 
                self._aktuellerZustand = Zustand.BEREIT
                self._gui.zeigeZustand(self.text_bereit)

                self.logger.log_system_event(f"Backvorgang beendet. End-Temp: {ist_temp:.1f}°C")

                print(f"CONTROLLER: *** {self.text_bereit} ***")
                self.buzzer.piep(anzahl=3)

            print(f"Regelkreis: Ist={ist_temp:.1f}°C, Soll={self._sollTemp}°C, Leistung={leistung:.2f}")
    
    def stoppeProzess(self):
        """
        Stoppt den aktuellen Backvorgang sofort aus Sicherheitsgründen 
        oder durch Benutzabbruch.
        """
        self._aktuellerZustand = Zustand.STANDBY
        self._isHeizungAktiv = False
        
        self._gui.zeigeZustand(Zustand.STANDBY.value)

        if hasattr(self._regler, 'heater_aktuator'):
            self._regler.heater_aktuator.setzeLeistung(0.0)
        
        if hasattr(self, 'logger'):
            self.logger.log_system_event("MANUAL_STOP: Heizvorgang abgebrochen / Not-Aus.")
        
        print("CONTROLLER: System wurde sicher in den STANDBY-Modus versetzt.")