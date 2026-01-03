import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from anwendungsschicht.WaffelController import WaffelController, Zustand
from steuerungsschicht_regelungsschicht.PIDRegler import PIDRegler
from steuerungsschicht_regelungsschicht.Solltabelle import Solltabelle
from Benutzeroberfläche_userinterface.SimpleGUI import SimpleGUI
from hardwareAbstraktionsschicht.HeaterActuator import HeaterActuator

def test_it14_sicherheitsabschaltung():
    """
    IT14: Verifikation der Sicherheitsabschaltung (Requirement 5.3).
    """
    print("--- Starte Integration Test: IT14 (Sicherheitsabschaltung) ---")
    
    gui = SimpleGUI(controller=None)
    regler = PIDRegler()
    aktor = HeaterActuator()
    
    aktor.ist_leistung = 0.0
    original_setze_leistung = aktor.setzeLeistung

    def patched_setze_leistung(leistung):
        aktor.ist_leistung = leistung # Wert fuer den Test speichern
        original_setze_leistung(leistung) # Original-Funktion aufrufen

    aktor.setzeLeistung = patched_setze_leistung
    # -----------------------------------------------------------------------

    regler.heater_aktuator = aktor 
    tabelle = Solltabelle()
    
    controller = WaffelController(gui, regler, tabelle)
    gui.controller = controller 
    
    print("Aktion: Backvorgang wird gestartet...")
    controller.starteBackvorgang()
    
    controller.runRegelkreisIteration()
    print(f"Zustand vor Stopp: {controller._aktuellerZustand}")
    
    print("Aktion: stoppeProzess() wird aufgerufen...")
    controller.stoppeProzess()
    
    zustand_nach_stopp = controller._aktuellerZustand
    heizung_aktiv = controller._isHeizungAktiv
    aktuelle_leistung = aktor.ist_leistung 
    
    print(f"Zustand nach Stopp: {zustand_nach_stopp}")
    print(f"Heizung aktiv (Flag): {heizung_aktiv}")
    print(f"Letzte Leistung am Aktor: {aktuelle_leistung}")
    
    if zustand_nach_stopp == Zustand.STANDBY and aktuelle_leistung == 0.0:
        print("TEST BESTANDEN (Sicherheitsabschaltung erfolgreich)")
    else:
        print("TEST FEHLGESCHLAGEN (System nicht im Sicherheitszustand)")

if __name__ == "__main__":
    test_it14_sicherheitsabschaltung()