import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datenhaltungsschicht.DataLogger import DataLogger

def test_ut10_logging_events():
    """
    UT10: Verifikation der Event-Protokollierung (Requirement 5.2).
    """
    print("--- Starte Unit Test: UT10 (DataLogger / System-Events) ---")
    
    logger = DataLogger()
    test_event = "TEST_ALARM"
    
    logger.log_system_event(test_event)
    
    if len(logger.system_logs) > 0:
        letzter_log = logger.system_logs[-1]
        if test_event in letzter_log:
            print(f"Event gefunden: {letzter_log}")
            print("TEST BESTANDEN")
            return
            
    print("TEST FEHLGESCHLAGEN")

if __name__ == "__main__":
    test_ut10_logging_events()