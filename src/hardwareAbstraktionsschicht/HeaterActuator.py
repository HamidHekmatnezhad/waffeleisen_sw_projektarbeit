class HeaterActuator:
    """
    Klasse zur Simulation des Heizelement-Aktors.
    """

    def __init__(self):
        """Initialisiert"""
        self.aktuelle_leistung: float = 0.0
        print("--- INFO: HeaterActuator Instanz erstellt.")


    def setzeLeistung(self, leistung: float):
        """
        [Req 3.1] Stellt die Leistung des Heizelements ein.
        """
        if not (0.0 <= leistung <= 1.0):
            print(f"FEHLER: Leistungswert ({leistung}) ist außerhalb des erlaubten Bereichs (0.0 - 1.0).")

        self.aktuelle_leistung = leistung

        if leistung > 0.0:
            status = f"EIN ({int(leistung * 100)}%)"
        else:
            status = "AUS"

        print(f"Status von HeaterActoutor:\n\t {status}")

    def holeAktuelleLeistung(self) -> float:
        """Gibt die aktuelle Leistungsstufe zurück (Hilfsmethode für Simulation/Debugging)."""
        return self.aktuelle_leistung