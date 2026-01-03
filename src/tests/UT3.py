import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from steuerungsschicht_regelungsschicht.PIDRegler import PIDRegler

def test_ut3_clamping_begrenzung():
    """
    UT3: Prüfung, ob der Rückgabewert korrekt auf maximal 1.0 begrenzt wird,
    auch wenn die mathematische Differenz extrem hoch ist.
    """
    print("--- Starte Unit Test: UT3 (Stellgrößenbegrenzung / Clamping) ---")
    
    regler = PIDRegler()
    soll_temp = 250.0 # Extrem hoher Zielwert
    regler.setzeSolltemperatur(soll_temp)
    
    ist_temp = 0.0
    leistung = regler.calculateHeatingPower(ist_temp)
    
    print(f"Eingabe: {ist_temp}°C | Soll: {soll_temp}°C | Differenz: {soll_temp - ist_temp}°C")
    print(f"Berechnete Leistung: {leistung}")
    
    if leistung == 1.0:
        print("TEST BESTANDEN (Wert wurde korrekt auf 1.0 begrenzt)")
    elif leistung > 1.0:
        print(f"TEST FEHLGESCHLAGEN (Wert {leistung} ist zu hoch!)")
    else:
        print(f"TEST FEHLGESCHLAGEN (Unerwarteter Wert: {leistung})")
        
if __name__ == "__main__":
    test_ut3_clamping_begrenzung()