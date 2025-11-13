from typing import Dict
from hardwareAbstraktionsschicht.TemperatureSensor import get_sensor_instance

class PIDRegler:
    """
    Klasse zur Implementierung des PID-Regelalgorithmus.
    Verantwortlich für die Berechnung der notwendigen Heizleistung.
    """

    _kp: float = 0.5  # Proportional-Verstärkung (nur ein Beispiel)
    _ki: float = 0.05 # Integral-Verstärkung
    _kd: float = 0.0  # Differential-Verstärkung

    _soll_temperatur: float = 0.0
    _integraler_fehler: float = 0.0
    _letzter_fehler: float = 0.0

    def __init__(self):
        """Initialisiert"""
        self.sensor = get_sensor_instance()
        print("--- INFO: PIDRegler Instanz erstellt und mit Sensor verbunden.")

    def setzeSolltemperatur(self, temp: int) -> None:
        """
        Setzt die Zieltemperatur, die vom Regler gehalten werden soll.

        Args:
            temp (int):  °C.
        """
        self._soll_temperatur = float(temp)
        self._integraler_fehler = 0.0 
        self._letzter_fehler = 0.0

    def calculateHeatingPower(self, istTemp: float) -> float:
        """
        [Req 3.1] Berechnet die notwendige Stellgröße (Heizleistung) basierend auf dem Fehler.

        Args:
            istTemp (float): Die aktuelle gemessene Temperatur.

        Returns:
            float: Der Leistungswert (0.0 bis 1.0).
        """
        fehler = self._soll_temperatur - istTemp

        p_anteil = self._kp * fehler

        self._integraler_fehler += fehler
        i_anteil = self._ki * self._integraler_fehler

        d_anteil = self._kd * (fehler - self._letzter_fehler)
        self._letzter_fehler = fehler

        stellgroesse = p_anteil + i_anteil + d_anteil

        stellgroesse_begrenzt = max(0.0, min(1.0, stellgroesse))

        return stellgroesse_begrenzt

    def hole_regler_parameter(self) -> Dict[str, float]:
        """Gibt die aktuellen Reglerparameter zurück."""
        return {'Kp': self._kp, 'Ki': self._ki, 'Kd': self._kd}
