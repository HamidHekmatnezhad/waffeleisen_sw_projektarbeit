from anwendungsschicht.WaffelController import WaffelController, Zustand
from steuerungsschicht_regelungsschicht.PIDRegler import PIDRegler
from steuerungsschicht_regelungsschicht.Solltabelle import Solltabelle
from Benutzeroberfläche_userinterface.SimpleGUI import SimpleGUI
from hardwareAbstraktionsschicht.HeaterActuator import HeaterActuator

def test_it14_sicherheitsabschaltung():
    """
    IT14: Verifikation der manuellen Abschaltfunktion und der 
    sofortigen Unterbrechung der Heizleistung (Requirement 5.3).
    """
    print("--- Starte Integration Test: IT14 (Sicherheitsabschaltung / Not-Aus) ---")
    
    gui = SimpleGUI(controller=None)
    regler = PIDRegler()
    aktor = HeaterActuator()
    regler.heater_aktuator = aktor 
    tabelle = Solltabelle()
    
    controller = WaffelController(gui, regler, tabelle)
    gui.controller = controller 
    
    print("Aktion: Backvorgang wird gestartet...")
    controller.starteBackvorgang()
    
    controller.runRegelkreisIteration()
    print(f"Aktueller Zustand vor Stopp: {controller._aktuellerZustand}")
    
    print("Aktion: stoppeProzess() wird aufgerufen (Not-Aus)...")
    controller.stoppeProzess()
    
    zustand_nach_stopp = controller._aktuellerZustand
    heizung_aktiv = controller._isHeizungAktiv
    aktuelle_leistung = aktor.ist_leistung 
    
    print(f"Zustand nach Stopp: {zustand_nach_stopp}")
    print(f"Heizung aktiv: {heizung_aktiv}")
    print(f"Heizleistung am Aktor: {aktuelle_leistung}W")
    
    if zustand_nach_stopp == Zustand.STANDBY and not heizung_aktiv and aktuelle_leistung == 0.0:
        print("TEST BESTANDEN (Sicherheitsabschaltung erfolgreich)")
    else:
        print("TEST FEHLGESCHLAGEN (System wurde nicht sicher abgeschaltet!)")

if __name__ == "__main__":
    test_it14_sicherheitsabschaltung()