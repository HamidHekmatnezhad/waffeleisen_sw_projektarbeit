import time
from datetime import datetime

class DataLogger:
    """
    Klasse zur Protokollierung von Messwerten und Ereignissen.
    Verantwortlich für das Speichern von Temperaturverläufen und Systemstatus.
    """

    def __init__(self):
        self.messwerte = []
        self.system_logs = []
        print("--- INFO: DataLogger initialisiert.")

    def log_messwert(self, temperatur: float):
        """
        Speichert einen Temperaturwert mit Zeitstempel.
        Simuliert einen Ringpuffer (behält nur die letzten 100 Werte).
        """
        eintrag = {
            "zeit": time.time(),
            "temp": temperatur
        }
        self.messwerte.append(eintrag)
        
        if len(self.messwerte) > 100:
            self.messwerte.pop(0)

    def log_system_event(self, nachricht: str):
        """
        Speichert Systemereignisse mit Datum/Uhrzeit.
        """
        zeitstempel = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_eintrag = f"[{zeitstempel}] {nachricht}"
        
        self.system_logs.append(log_eintrag)
        
        print(f"++ LOG: {log_eintrag}")

    def get_logs(self):
        """Gibt alle gespeicherten System-Logs zurück."""
        return self.system_logs