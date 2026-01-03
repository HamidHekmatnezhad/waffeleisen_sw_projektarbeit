import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from steuerungsschicht_regelungsschicht.PIDRegler import PIDRegler

def test_ut13_leistungsbegrenzung_100w():
    """
    UT13: Verifikation, dass die berechnete Heizleistung den physikalischen 
    Grenzwert von 100W niemals überschreitet (Requirement 3.2).
    """
    print("--- Starte Unit Test: UT13 (Leistungsbegrenzung 100W) ---")
    
    regler = PIDRegler()
    soll_temp = 200.0
    regler.setzeSolltemperatur(soll_temp)
    
    ist_temp = 20.0
    berechnete_leistung = regler.calculateHeatingPower(ist_temp)
    
    print(f"Eingabe: {ist_temp}°C | Soll: {soll_temp}°C")
    print(f"Berechnete Leistung: {berechnete_leistung}W")
    
    if berechnete_leistung <= 100.0:
        if berechnete_leistung > 99.0: 
            print("TEST BESTANDEN (Leistung korrekt auf 100W begrenzt)")
        else:
            print(f"Hinweis: Leistung ist {berechnete_leistung}W (im zulässigen Bereich)")
            print("TEST BESTANDEN")
    else:
        print(f"TEST FEHLGESCHLAGEN (Leistung {berechnete_leistung}W überschreitet Limit!)")

if __name__ == "__main__":
    test_ut13_leistungsbegrenzung_100w()