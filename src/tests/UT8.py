import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hardwareAbstraktionsschicht.AkustikSignalgeber import AkustikSignalgeber

def test_ut8_buzzer_signal():
    """
    UT8: Überprüfung der Hardware-Abstraktion AkustikSignalgeber 
    und der Methode piep().
    """
    print("--- Starte Unit Test: UT8 (Buzzer / Akustisches Signal) ---")
    
    buzzer = AkustikSignalgeber()
    
    print("Aktion: piep(anzahl=3) wird aufgerufen...")
    
    try:
        buzzer.piep(anzahl=3)
        test_erfolgreich = True
    except Exception as e:
        print(f"Fehler beim Aufruf der Hardware-Simulation: {e}")
        test_erfolgreich = False
    
    if test_erfolgreich:
        print("TEST BESTANDEN (Signalgabe ohne Fehler ausgeführt)")
    else:
        print("TEST FEHLGESCHLAGEN")

if __name__ == "__main__":
    test_ut8_buzzer_signal()