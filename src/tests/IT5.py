import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from anwendungsschicht.WaffelController import WaffelController
from Benutzeroberfläche_userinterface.SimpleGUI import SimpleGUI
from steuerungsschicht_regelungsschicht.PIDRegler import PIDRegler
from steuerungsschicht_regelungsschicht.Solltabelle import Solltabelle

def test_it5_gui_aktualisierung():
    """
    IT5: Verifikation, dass Zustandsänderungen im Controller 
    korrekt an die GUI-Anzeige weitergegeben werden.
    """
    print("--- Starte Integration Test: IT5 (GUI-Update) ---")
    
    gui = SimpleGUI(controller=None)
    regler = PIDRegler()
    tabelle = Solltabelle()
    controller = WaffelController(gui, regler, tabelle)
    gui.controller = controller 
    
    print(f"Ursprünglicher GUI-Zustand: {gui.getDisplayState()}")
    
    controller.starteBackvorgang()
    
    aktueller_text = gui.getDisplayState()
    print(f"Aktualisierter GUI-Zustand: {aktueller_text}")
    
    if "AUFHEIZEN" in aktueller_text:
        print("TEST BESTANDEN")
    else:
        print(f"TEST FEHLGESCHLAGEN (Erwartet: AUFHEIZEN, Erhalten: {aktueller_text})")

if __name__ == "__main__":
    test_it5_gui_aktualisierung()