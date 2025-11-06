## Traceability Matrix: Anforderung zu Implementierung (Mit Sprint-Zuordnung)

| Requirement-ID | Beschreibung (Kurz) | Klasse(n) (SW Design) | Schnittstelle(n) (Methode) | Testfall(e) |
| :------------ | :------------------- | :--------------------- | -------------------------- | :--------- |
| 1.1 | Bräunungsgrad Einstellung | WaffelController, ButtonInput | verarbeiteEingabe(grad: int) | BB4 |
| 1.2 | Anzeige des aktuellen Bräunungsgrades | SimpleGUI | zeigeZustand(text: String) | UX1 |
| 2.2 | Temperaturmessung (MUSS) | TemperatureSensor | leseTemperatur(): float | BB1 |
| 3.1 | Temperaturregelung (MUSS) | PIDRegler | calculateHeatingPower(istTemp: float): float | UT3 |
| 3.3 | Testbarkeit des Regelalgorithmus (MUSS) | PIDRegler | calculateHeatingPower() (als isolierte Einheit) | UT1, UT2 |
| 4.1 | Sicherheitsfehleranzeige | SimpleGUI | zeigeZustand(text: String) (mit "FEHLER") | BB2 |
| 5.1 | Akustisches Signal | AkustikSignalgeber | setzeLeistung() (Aktuator-Ansteuerung) | BB3 |