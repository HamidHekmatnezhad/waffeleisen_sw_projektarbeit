from typing import Dict

class Solltabelle:
    """
    Klasse zur Verwaltung der Kalibrierungsdaten.
    Konvertiert den vom Benutzer gewählten Bräunungsgrad in die Soll-Temperatur (°C).
    """
    
    _GRAD_ZU_TEMPERATUR: Dict[int, int] = { 
        # Grad 1 = niedrigste Temperatur, Grad 5 = höchste Temperatur.
        1: 150,  # Leichte Bräunung
        2: 165,
        3: 180,  # Mittlere Bräunung
        4: 195,
        5: 210   # Dunkle Bräunung
    }

    def __init__(self):
        """Initialisiert die Solltabelle."""
        print("--- INFO: Solltabelle Initialisierung abgeschlossen.")
        
    def holeSolltemperatur(self, grad: int) -> int:
        """
        Gibt die Zieltemperatur in °C für den gewählten Bräunungsgrad zurück.
        
        Args:
            grad (int): Der gewählte Bräunungsgrad (1 bis 5).
            
        Returns:
            int: Die zugehörige Soll-Temperatur in °C.
        """
        
        if 1 <= grad <= 5:
            return self._GRAD_ZU_TEMPERATUR[grad]
        else:
            print(f"FEHLER: Ungültiger Bräunungsgrad ({grad}) gewählt. Setze auf Standard (Grad 3).")
            return self._GRAD_ZU_TEMPERATUR[3]