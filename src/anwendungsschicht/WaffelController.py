from enum import Enum
from steuerungsschicht_regelungsschicht.PIDRegler import PIDRegler
from steuerungsschicht_regelungsschicht.Solltabelle import Solltabelle
from Benutzeroberfläche_userinterface.SimpleGUI import SimpleGUI

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


    def verarbeiteEingabe(self, delta_grad: int) -> None:
        """
        [Req 1.1] Verarbeitet die Eingabe vom Benutzer (von ButtonInput ausgelöst).
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
            self._gui.zeigeZustand(Zustand.AUFHEIZEN.value)
            self._isHeizungAktiv = True
            print("CONTROLLER: Backvorgang gestartet. Beginne Aufheizen...")

    def runRegelkreisIteration(self) -> None:
        """
        [Req 3.1] Führt eine Iteration des Regelkreises aus (Kern der Applikation).
        Diese Methode wird zyklisch von einem Timer/Scheduler aufgerufen.
        """
        if self._aktuellerZustand == Zustand.AUFHEIZEN:
            
            # 1. Ist-Temperatur lesen 
            ist_temp = self._regler.sensor.leseTemperatur() 
            
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
                self._gui.zeigeZustand(Zustand.BEREIT.value)
                print("CONTROLLER: *** Waffeleisen ist BEREIT zum Backen! ***")
            
            print(f"Regelkreis: Ist={ist_temp}°C, Soll={self._sollTemp}°C, Leistung={leistung:.2f}")