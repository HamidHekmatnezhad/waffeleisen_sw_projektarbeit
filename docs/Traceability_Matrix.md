## Traceability Matrix: Anforderung zu Implementierung (Stand Sprint 3)

| Requirement-ID | Beschreibung (Kurz) | **Sprint** | **Komponenten** | Klasse(n) (SW Design) | Schnittstelle(n) (Methode) | Testfall(e) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1.1** | Bräunungsgrad Einstellung | **Sprint 1** | UI / App | `WaffelController`, `ButtonInput` | `verarbeiteEingabe(grad: int)` | **UT6** |
| **1.2** | Anzeige des aktuellen Bräunungsgrades | **Sprint 1** | UI | `SimpleGUI` | `zeigeZustand(text: String)` | **UT5** |
| **1.3** | Reaktionszeit Auswahl (< 2s) | - | System / UI | `WaffelController` | - | - |
| **1.4** | Konfigurierbare Texte (Config) | **Sprint 2** | Persistence | `ConfigLoader` | `laod_lang(lang: String)` | **UT7** |
| **2.1** | Protokollierung Messwerte (Ringpuffer) | **Sprint 3** | Data / Logging | `DataLogger` | `log_messwert(temp: float)` | **UT9** |
| **2.2** | Temperaturmessung (MUSS) | **Sprint 1** | Hardware | `TemperatureSensor` | `leseTemperatur(): float` | **UT4** |
| **2.3** | Sensorfunktion bei Umgebungstemp. | - | Hardware | `TemperatureSensor` | - | - |
| **3.1** | Temperaturregelung (MUSS) | **Sprint 1** | Core / Logic | `PIDRegler` | `calculateHeatingPower(...)` | **UT1-UT3** |
| **3.2** | Energieverbrauch (< 100W) | - | Hardware | `HeaterActuator` | - | - |
| **3.3** | Testbarkeit des Regelalgorithmus | **Sprint 1** | Core / Logic | `PIDRegler` | `calculateHeatingPower()` | **UT1-UT3** |
| **4.1** | Sicherheitsfehleranzeige | **Sprint 2** | UI / Config | `SimpleGUI`, `ConfigLoader` | `zeigeZustand(...)` | **UT7** |
| **4.2** | Mehrsprachigkeit (Glossar) | **Sprint 2** | Persistence | `ConfigLoader` | `laod_lang(lang: String)` | **UT7** |
| **5.1** | Akustisches Signal (3 Mal) | **Sprint 2** | Hardware | `AkustikSignalgeber` | `piep(anzahl: int)` | **UT8** |
| **5.2** | Protokollierung Abschaltung | **Sprint 3** | Data / Logging | `DataLogger` | `log_system_event(msg: String)` | **UT10** |
| **5.3** | Verfügbarkeit Abschaltfunktion | - | System | `SafetyController` | - | - |