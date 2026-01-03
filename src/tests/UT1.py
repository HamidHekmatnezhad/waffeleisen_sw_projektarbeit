import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from steuerungsschicht_regelungsschicht.PIDRegler import PIDRegler

def test_ut1_kaltstart():
    """
    UT1: Verifikation, dass der Regler bei einem Kaltstart 
    die maximale Heizleistung (1.0) anfordert.
    """
    print("--- Starte Unit Test: UT1 (Kaltstart) ---")
    
    regler = PIDRegler()
    soll_temp = 180.0
    regler.setzeSolltemperatur(soll_temp)
    
    ist_temp = 25.0
    leistung = regler.calculateHeatingPower(ist_temp)
    
    print(f"Eingabe (Ist-Temp): {ist_temp}°C | Ziel (Soll-Temp): {soll_temp}°C")
    print(f"Ergebnis (Leistung): {leistung}")
    
    if leistung == 1.0:
        print("TEST BESTANDEN")
    else:
        print(f"TEST FEHLGESCHLAGEN (Erwartet: 1.0, Erhalten: {leistung})")

if __name__ == "__main__":
    test_ut1_kaltstart()