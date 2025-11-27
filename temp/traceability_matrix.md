| Requirement-ID | Jira-Issue | Komponente | Klasse(n) | Schnittstelle(n) | Testfall(e) | 
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1.1** | BAT-7 | userInterface, hardwareAbstraction | `ButtonInput` | `ButtonInput()` | BB4 | 
| **1.2** | BAT-8 | userInterface | `SimpleGUI` | `getDisplayState()` | UX1 | 
| **2.2** | BAT-11 | hardwareAbstraction | `TemperatureSensor` | `readTemperature()` | BB1 | 
| **3.1** | BAT-20 | controlLogic | `PIDRegler` | `calculateHeatingPower()` | UT3 | 
| **3.3** | BAT-21 | controlLogic | `PIDRegler` | Keine | UT1, UT2 |
| 4.1 | BAT-10 | userInterface | `SimpleGUI` | `getDisplayState()` | BB2 |
| 5.1 | BAT-14 | controlLogic | `AkustikSignalgeber` | `setState()` | BB3 |




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


| Requirement-ID | Beschreibung (Kurz) | **Sprint** | **Architektur** | Klasse(n) (SW Design) | Schnittstelle(n) (Methode) | Testfall(e) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1.1** | Bräunungsgrad Einstellung | **Sprint 1** | UI / App | `WaffelController`, `ButtonInput` | `verarbeiteEingabe(grad: int)` | **UT6** |
| **1.2** | Anzeige des aktuellen Bräunungsgrades | **Sprint 1** | UI | `SimpleGUI` | `zeigeZustand(text: String)` | **UT5** |
| **2.2** | Temperaturmessung (MUSS) | **Sprint 1** | Hardware | `TemperatureSensor` | `leseTemperatur(): float` | **UT4** |
| **3.1** | Temperaturregelung (MUSS) | **Sprint 1** | Core / Logic | `PIDRegler` | `calculateHeatingPower(ist: float): float` | **UT1, UT2, UT3** |
| **3.3** | Testbarkeit des Regelalgorithmus | **Sprint 1** | Core / Logic | `PIDRegler` | `calculateHeatingPower()` (als isolierte Einheit) | **UT1, UT2, UT3** |
| 4.1 | Sicherheitsfehleranzeige | - | UI | `SimpleGUI` | `zeigeZustand(...)` (mit "FEHLER") | - |
| 5.1 | Akustisches Signal | - | Hardware | `AkustikSignalgeber` | `setzeLeistung()` | - |
