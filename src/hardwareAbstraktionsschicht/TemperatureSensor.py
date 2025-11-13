import random

class TemperatureSensor:
    """
    Klasse zur Simulation des Temperatursensors.
    Implementiert das Singleton Pattern, um nur eine Instanz zu erlauben.
    """

    # Privates Attribut
    _instance = None

    simulated_temp: float = 25.0

    def __init__(self):
        """
        
        """
        # Prüft, ob _instance bereits gesetzt wurde
        if TemperatureSensor._instance is not None:
            raise Exception("FEHLER: Diese Klasse ist ein Singleton!")

        # Die erste 
        TemperatureSensor._instance = self
        print("--- INFO: TemperatureSensor erstellt.")


    def leseTemperatur(self) -> float:
        """
        [Req 2.2] Liefert den aktuellen Ist-Temperaturwert (in °C) für den Regelkreis.
        Für Iteration 1 wird der Wert nur simuliert.
        """

        schwankung = random.random() * 0.1 - 0.05
        return round(self.simulated_temp + schwankung, 2)

    def setze_simulierte_temperatur(self, neue_temp: float):
        """
        Hilfsmethode
        """
        self.simulated_temp = max(90.0, neue_temp)


    def get_sensor_instance():
        """
        Gibt die Singleton-Instanz von TemperatureSensor zurück.
        """

        #TODO ich bin nicht sicher diese code Richtig, muss ich testen.

        if TemperatureSensor._instance is None:
            TemperatureSensor()
        return TemperatureSensor._instance