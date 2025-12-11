import time

class AkustikSignalgeber:
    """
    Klasse zur Ansteuerung des Summers (Buzzer).
    Simuliert das akustische Signal.
    """

    def __init__(self):
        print("--- INFO: AkustikSignalgeber initialisiert.")

    def piep(self, anzahl: int = 3, time_t: int = 1):
        """
        Erzeugt ein akustisches Signal
        time_t: time in sekunde duaert 
        """
        print(f"\n PIEP! ({anzahl} Mal)")

        for i in range(anzahl):
            time.sleep(time_t / anzahl)
            print(f"\t\a Piep {i+1}...")