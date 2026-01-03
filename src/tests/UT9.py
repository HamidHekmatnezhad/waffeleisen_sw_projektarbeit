import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datenhaltungsschicht.DataLogger import DataLogger

def test_ut9_logging_messwerte():
    """
    UT9: Verifikation der Temperatur-Protokollierung (Requirement 2.1).
    """
    print("--- Starte Unit Test: UT9 (DataLogger / Messwerte) ---")
    
    logger = DataLogger()
    test_temperatur = 180.5
    
    print(f"Aktion: log_messwert({test_temperatur}) wird aufgerufen...")
    logger.log_messwert(test_temperatur)
    
    if len(logger.messwerte) > 0 and logger.messwerte[-1]["temp"] == test_temperatur:
        print(f"Gespeicherter Wert in List: {logger.messwerte[-1]['temp']}°C")
        print("TEST BESTANDEN")
    else:
        print("TEST FEHLGESCHLAGEN (Struktur mismatch oder Wert fehlt)")

if __name__ == "__main__":
    test_ut9_logging_messwerte()