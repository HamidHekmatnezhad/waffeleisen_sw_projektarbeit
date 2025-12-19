# Sprint 2: Erweiterung (Safety, Feedback & Performance)

## **1. Sprint Planning**

**Ziel:** Erweiterung des Waffeleisens um Sicherheitsfunktionen, akustisches Feedback, Performance-Optimierung und ein Konfigurationssystem (Persistence).

**Ausgewählte Hauptfunktionen:**

1.  **Konfigurierbare Texte & Mehrsprachigkeit (Req 1.4, 4.2):**
    * **Beschreibung:** Einführung des `ConfigLoader`, um Texte (z. B. "BEREIT", "AUFHEIZEN") aus einer externen JSON-Datei zu laden.
    * **Begründung:** Trennung von Code und Inhalten; ermöglicht eine einfache Lokalisierung ohne Eingriff in die Programmlogik.

2.  **Akustisches Signal (Buzzer) (Req 5.1):**
    * **Beschreibung:** Integration einer Hardware-Abstraktion (`AkustikSignalgeber`), die einen Signalton ausgibt, sobald der Backvorgang beendet ist.
    * **Begründung:** Erhöhung der **Usability**; der Benutzer wird aktiv informiert, ohne das Display ständig beobachten zu müssen.

3.  **Sicherheitsfehleranzeige (Req 4.1):**
    * **Beschreibung:** Implementierung einer Logik, die bei kritischen Fehlern (z. B. Sensorausfall) den Zustand sofort auf "FEHLER" setzt und dies visuell ausgibt.
    * **Begründung:** Zentrale **Sicherheitsfunktion** zum Schutz des Systems und des Benutzers.

4.  **System-Performance & Reaktionszeit (Req 1.3):**
    * **Beschreibung:** Optimierung der Eingabeverarbeitung, um eine Reaktionszeit von unter 2 Sekunden zu gewährleisten.
    * **Begründung:** Sicherstellung der **Echtzeitfähigkeit** und einer flüssigen Benutzererfahrung.

---

## **2. Review: Soll-Ist-Vergleich**

Nach Abschluss der Implementierung wurden die geplanten Erweiterungen mit der tatsächlichen Umsetzung verglichen:

| Bereich | Geplantes Design (Soll) | Tatsächliche Implementierung (Ist) | Grund für die Abweichung |
| :--- | :--- | :--- | :--- |
| **Datenhaltung** | Geplante Nutzung einer Datenbank oder komplexer CSV-Strukturen. | Umsetzung mittels **JSON-Konfiguration** (`config.json`). | JSON bietet eine bessere hierarchische Struktur für Sprachpakete und eine einfachere Handhabung in Python. |
| **Sprachumschaltung** | Dynamisches Umschalten der Sprache während des laufenden Betriebs. | Sprache wird initial **beim Systemstart** geladen. | Die Komplexität einer Live-Umschaltung stand in keinem angemessenen Verhältnis zum Nutzen für das aktuelle MVP. |
| **Buzzer-Hardware** | Ansteuerung eines physischen GPIO-Pins am Mikrocontroller. | **Simulierte Ausgabe** über die Konsole (`print("PIEP")`). | Da keine physische Hardware zur Verfügung stand, wurde die Schnittstelle für die Simulation optimiert, um die Logik zu testen. |

---

## **3. Erkenntnisse & Ausblick**

Basierend auf den Erfahrungen aus Sprint 2 ergeben sich folgende Erkenntnisse für den finalen Sprint 3:

1.  **Bedeutung von Integration Tests:**
    * **Erkenntnis:** Unit Tests allein reichen nicht aus, um das Zusammenspiel zwischen `ConfigLoader`, `WaffelController` und `SimpleGUI` vollständig abzusichern.
    * **Maßnahme:** Einführung dedizierter **Integration Tests (IT5, IT11)** im Testkonzept, um die gesamte Kette von der Eingabe bis zur Anzeige zu verifizieren.

2.  **Robustheit der Konfiguration:**
    * **Erkenntnis:** Eine fehlerhafte JSON-Datei kann zum Systemabsturz führen.
    * **Maßnahme:** Implementierung eines **Fallback-Mechanismus** im `ConfigLoader`, der bei Dateifehlern auf interne Standardwerte zurückgreift.

3.  **Vorbereitung auf Sprint 3 (Logging):**
    * **Erkenntnis:** Die Architektur ist nun stabil genug, um eine umfassende Protokollierung zu integrieren.
    * **Ausblick:** Im nächsten Sprint wird der `DataLogger` implementiert, um alle Systemzustände und Messwerte revisionssicher zu erfassen.