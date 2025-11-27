# Implementierung

## Traceability Matrix: Anforderung zu Implementierung

| Requirement-ID | Beschreibung (Kurz) | **Sprint** | **Komponenten** | Klasse(n) (SW Design) | Schnittstelle(n) (Methode) | Testfall(e) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1.1** | Bräunungsgrad Einstellung | **Sprint 1** | UI / App | `WaffelController`, `ButtonInput` | `verarbeiteEingabe(grad: int)` | **UT6** |
| **1.2** | Anzeige des aktuellen Bräunungsgrades | **Sprint 1** | UI | `SimpleGUI` | `zeigeZustand(text: String)` | **UT5** |
| **2.2** | Temperaturmessung (MUSS) | **Sprint 1** | Hardware | `TemperatureSensor` | `leseTemperatur(): float` | **UT4** |
| **3.1** | Temperaturregelung (MUSS) | **Sprint 1** | Core / Logic | `PIDRegler` | `calculateHeatingPower(ist: float): float` | **UT1, UT2, UT3** |
| **3.3** | Testbarkeit des Regelalgorithmus | **Sprint 1** | Core / Logic | `PIDRegler` | `calculateHeatingPower()` (als isolierte Einheit) | **UT1, UT2, UT3** |
| 4.1 | Sicherheitsfehleranzeige | - | UI | `SimpleGUI` | `zeigeZustand(...)` (mit "FEHLER") | - |
| 5.1 | Akustisches Signal | - | Hardware | `AkustikSignalgeber` | `setzeLeistung()` | - |  