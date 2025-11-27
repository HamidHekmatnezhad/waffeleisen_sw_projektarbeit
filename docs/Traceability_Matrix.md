## Traceability Matrix: Anforderung zu Implementierung 

| Requirement-ID | Beschreibung (Kurz) | **Sprint** | **Komponenten** | Klasse(n) (SW Design) | Schnittstelle(n) (Methode) | Testfall(e) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1.1** | Bräunungsgrad Einstellung | **Sprint 1** | UI / App | `WaffelController`, `ButtonInput` | `verarbeiteEingabe(grad: int)` | **UT6** |
| **1.2** | Anzeige des aktuellen Bräunungsgrades | **Sprint 1** | UI | `SimpleGUI` | `zeigeZustand(text: String)` | **UT5** |
| **1.3** | Reaktionszeit Auswahl (< 2s) | - | System / UI | `WaffelController` | - | - |
| **1.4** | Konfigurierbare Texte (Config) | - | Persistence | `ConfigLoader` | `loadConfiguration(path: String)` | - |
| **2.1** | Protokollierung Messwerte (Ringpuffer) | - | Data / Logic | `DataLogger` | `logMeasurement(temp: float)` | - |
| **2.2** | Temperaturmessung (MUSS) | **Sprint 1** | Hardware | `TemperatureSensor` | `leseTemperatur(): float` | **UT4** |
| **2.3** | Sensorfunktion bei Umgebungstemp. | - | Hardware | `TemperatureSensor` | - | - |
| **3.1** | Temperaturregelung (MUSS) | **Sprint 1** | Core / Logic | `PIDRegler` | `calculateHeatingPower(...)` | **UT1, UT2, UT3** |
| **3.2** | Energieverbrauch (< 100W) | - | Hardware | `HeaterActuator` | - | - |
| **3.3** | Testbarkeit des Regelalgorithmus | **Sprint 1** | Core / Logic | `PIDRegler` | `calculateHeatingPower()` | **UT1, UT2, UT3** |
| **4.1** | Sicherheitsfehleranzeige | - | UI | `SimpleGUI` | `zeigeZustand(...)` | - |
| **4.2** | Mehrsprachigkeit (Glossar) | - | Persistence | `LanguageManager` | `getText(key: String): String` | - |
| **5.1** | Akustisches Signal (3 Mal) | - | Hardware | `AkustikSignalgeber` | `setzeLeistung(an: bool)` | - |
| **5.2** | Protokollierung Abschaltung | - | Data / Logic | `DataLogger` | `logShutdown(time, temp)` | - |
| **5.3** | Verfügbarkeit Abschaltfunktion | - | System | `SafetyController` | - | - |