from anwendungsschicht.WaffelController import WaffelController 

class ButtonInput:
    """
    Klasse zur Simulation der Tasten-Eingabe ('+' und '-').
    """
    
    def __init__(self, controller: WaffelController):
        """Initialisiert die Eingabekomponente und verbindet sie mit dem Controller."""
        self.controller = controller 
        print("--- INFO: ButtonInput Instanz erstellt und mit Controller verbunden.")

    
    def simuliereTaste(self, taste: str):
        """
        Simuliert das Drücken einer Taste ('+' oder '-').
        """
        if taste == '+':
            self.verarbeiteEingabe(1) 
            print("SIMULATION: Taste '+' gedrückt.")
        elif taste == '-':
            self.verarbeiteEingabe(-1)
            print("SIMULATION: Taste '-' gedrückt.")
        else:
            print("FEHLER: Ungültige Taste.")


    def verarbeiteEingabe(self, delta_grad: int) -> None:
        """
        [Req 1.1] Leitet die Eingabe an den WaffelController weiter.
        Diese Methode wird asynchron (Event-basiert) aufgerufen.
        """
        self.controller.verarbeiteEingabe(delta_grad)