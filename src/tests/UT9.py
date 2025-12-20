from datenhaltungsschicht.DataLogger import DataLogger

def test_ut9_logging_messwerte():
    """
    UT9: Verifikation, dass Temperaturwerte korrekt im Speicher 
    des DataLoggers abgelegt werden (Requirement 2.1).
    """
    print("--- Starte Unit Test: UT9 (DataLogger / Messwerte) ---")
    
    logger = DataLogger()
    test_temperatur = 180.5
    
    print(f"Aktion: log_messwert({test_temperatur}) wird aufgerufen...")
    logger.log_messwert(test_temperatur)
    
    if len(logger.messwerte) > 0 and logger.messwerte[-1] == test_temperatur:
        print(f"Gespeicherter Wert im Log: {logger.messwerte[-1]}°C")
        print("TEST BESTANDEN")
    else:
        print("TEST FEHLGESCHLAGEN (Wert wurde nicht korrekt gespeichert)")

if __name__ == "__main__":
    test_ut9_logging_messwerte()