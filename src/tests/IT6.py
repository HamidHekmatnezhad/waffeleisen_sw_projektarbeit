from anwendungsschicht.WaffelController import WaffelController
from Benutzeroberfläche_userinterface.ButtonInput import ButtonInput
from steuerungsschicht_regelungsschicht.Solltabelle import Solltabelle
from steuerungsschicht_regelungsschicht.PIDRegler import PIDRegler
from Benutzeroberfläche_userinterface.SimpleGUI import SimpleGUI

def test_it6_eingabekette():
    """
    IT6: Verifikation der Kette vom Tastendruck bis zur Sollwert-Änderung.
    """
    print("--- Starte Integration Test: IT6 (Eingabeverarbeitung) ---")
    
    gui = SimpleGUI(controller=None)
    regler = PIDRegler()
    tabelle = Solltabelle()
    controller = WaffelController(gui, regler, tabelle)
    input_handler = ButtonInput(controller)
    
    print(f"Start-Soll-Temperatur: {controller._sollTemp}°C (Grad {controller._aktueller_grad})")
    
    print("Aktion: Taste '+' gedrückt.")
    input_handler.simuliereTaste('+')
    
    neue_temp = controller._sollTemp
    neuer_grad = controller._aktueller_grad
    print(f"Neuer Zustand: Grad {neuer_grad} | Soll-Temp: {neue_temp}°C")
    
    if neuer_grad == 4 and neue_temp == 195:
        print("TEST BESTANDEN")
    else:
        print(f"TEST FEHLGESCHLAGEN (Erwartet: Grad 4/195°C)")

if __name__ == "__main__":
    test_it6_eingabekette()