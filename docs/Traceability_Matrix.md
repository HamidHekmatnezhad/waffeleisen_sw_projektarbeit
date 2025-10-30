## Traceability Matrix: Anforderung zu Implementierung (Mit Sprint-Zuordnung)

| Requirement-ID | Jira-Issue | Komponente | Klasse(n) | Schnittstelle(n) | Testfall(e) | 
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1.1** | BAT-7 | userInterface, hardwareAbstraction | `ButtonInput` | `ButtonInput()` | BB4 | 
| **1.2** | BAT-8 | userInterface | `SimpleGUI` | `getDisplayState()` | UX1 | 
| **2.2** | BAT-11 | hardwareAbstraction | `TemperatureSensor` | `readTemperature()` | BB1 | 
| **3.1** | BAT-20 | controlLogic | `PIDRegler` | `calculateHeatingPower()` | UT3 | 
| **3.3** | BAT-21 | controlLogic | `PIDRegler` | Keine | UT1, UT2 |
| 4.1 | BAT-10 | userInterface | `SimpleGUI` | `getDisplayState()` | BB2 |
| 5.1 | BAT-14 | controlLogic | `AkustikSignalgeber` | `setState()` | BB3 |