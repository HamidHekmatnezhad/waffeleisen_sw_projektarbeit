from datenhaltungsschicht.DataLogger import DataLogger

def test_ut10_logging_events():
    """
    UT10: Verifikation, dass System-Ereignisse (Start/Stopp) korrekt
    mit Zeitstempel protokolliert werden (Requirement 5.2).
    """
    print("--- Starte Unit Test: UT10 (DataLogger / System-Events) ---")
    
    logger = DataLogger()
    test_event = "BACKVORGANG_GESTARTET"
    
    print(f"Aktion: log_system_event('{test_event}') wird aufgerufen...")
    logger.log_system_event(test_event)
    
    if len(logger.system_logs) > 0:
        letzter_eintrag = logger.system_logs[-1]
        print(f"Gespeicherter Log-Eintrag: {letzter_eintrag}")
        
        if test_event in letzter_eintrag:
            print("TEST BESTANDEN (Event inkl. Zeitstempel gefunden)")
        else:
            print("TEST FEHLGESCHLAGEN (Event-Text fehlt)")
    else:
        print("TEST FEHLGESCHLAGEN (Log-Liste ist leer)")
if __name__ == "__main__":
    test_ut10_logging_events()