import time
from anwendungsschicht.WaffelController import WaffelController
from Benutzeroberfläche_userinterface.ButtonInput import ButtonInput
from Benutzeroberfläche_userinterface.SimpleGUI import SimpleGUI
from steuerungsschicht_regelungsschicht.PIDRegler import PIDRegler
from steuerungsschicht_regelungsschicht.Solltabelle import Solltabelle

def test_it11_reaktionszeit():
    """
    IT11: Verifikation, dass die Systemreaktionszeit auf eine 
    Benutzereingabe unter 2 Sekunden liegt (Requirement 1.3).
    """
    print("--- Starte Integration Test: IT11 (Performance / Reaktionszeit) ---")
    
    gui = SimpleGUI(controller=None)
    regler = PIDRegler()
    tabelle = Solltabelle()
    controller = WaffelController(gui, regler, tabelle)
    input_handler = ButtonInput(controller)
    
    print("Aktion: Simulation eines Tastendrucks und Zeitmessung...")
    
    start_zeit = time.perf_counter() 
    input_handler.simuliereTaste('+') 
    end_zeit = time.perf_counter() 
    
    reaktionszeit = end_zeit - start_zeit
    
    print(f"Gemessene Reaktionszeit: {reaktionszeit:.6f} Sekunden")
    
    if reaktionszeit < 2.0:
        print("TEST BESTANDEN (Zeit liegt deutlich unter 2 Sekunden)")
    else:
        print(f"TEST FEHLGESCHLAGEN (System zu langsam: {reaktionszeit}s)")

if __name__ == "__main__":
    test_it11_reaktionszeit()