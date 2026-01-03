# Sprint 3: Systemabschluss (Logging, Sicherheit & Qualitätssicherung)

## **1. Sprint Planning**

**Ziel:** Finalisierung der Softwarearchitektur, Implementierung einer umfassenden Prozessdatenerfassung (Logging) und Validierung kritischer Sicherheits- und Hardware-Anforderungen.

**Ausgewählte Hauptfunktionen:**

1.  **Datenprotokollierung & DataLogger (Req 2.1, 5.2):**
    * **Beschreibung:** Implementierung des `DataLogger`, um Temperaturverläufe (Messwerte) und Systemereignisse (Events wie Start/Stopp) revisionssicher zu erfassen.
    * **Begründung:** Ermöglicht die nachträgliche Analyse des Backprozesses und dient der Qualitätssicherung sowie Fehlerdiagnose.

2.  **Mathematische Leistungsbegrenzung (Req 3.2):**
    * **Beschreibung:** Integration einer Sättigungsfunktion (Saturation) in den Regelalgorithmus (`calculateHeatingPower`), um die Heizleistung auf maximal 100W zu deckeln.
    * **Begründung:** Strikte Einhaltung der physischen Hardwarespezifikationen und Schutz vor elektrischer Überlastung im Simulationsmodell.

3.  **Verfügbarkeit der Sicherheitsabschaltung (Req 5.3):**
    * **Beschreibung:** Einführung einer sofortigen Stopp-Funktion (Not-Aus) über die GUI, die alle Heizprozesse unmittelbar unterbricht und das System erdet.
    * **Begründung:** Zentrale **Safety-Anforderung**; der Benutzer muss jederzeit die physikalische Kontrolle über den thermischen Prozess ausüben können.

4.  **Abschluss der Traceability & Verifikation:**
    * **Beschreibung:** Durchführung der finalen Integration Tests (IT12, IT14) und Unit Tests (UT13), um die Übereinstimmung von Code und Requirements zu beweisen.

---

## **2. Review: Soll-Ist-Vergleich**

Nach Abschluss der Implementierung wurden die Ziele von Sprint 3 mit der tatsächlichen Umsetzung verglichen:

| Bereich | Geplantes Design (Soll) | Tatsächliche Implementierung (Ist) | Grund für die Abweichung |
| :--- | :--- | :--- | :--- |
| **Datenarchivierung** | Speicherung der Logs CSV. | Protokollierung über eine **Listen-Struktur im DataLogger** mit Zeitstempeln. | Für die aktuelle Simulationsumgebung ist eine In-Memory-Lösung performanter und ermöglicht eine direktere Validierung der Testfälle. |
| **Leistungsbegrenzung** | Hardwareseitige Begrenzung durch eine physische Sicherung. | **Softwareseitiges Clamping** (Begrenzung) im `PIDRegler` auf den Wert 1.0 (entspricht 100W). | Eine algorithmische Begrenzung bietet eine schnellere Reaktionszeit und verhindert präventiv das Auslösen physischer Schutzmechanismen. |
| **Initialisierung** | Statische Verbindung aller Komponenten beim Programmstart (Instanziierung). | **Late-Binding** (Nachträgliche Injektion) des Controllers in class `SimpleGUI`. | Notwendig, um die zirkuläre Abhängigkeit (Circular Dependency) zwischen GUI und Controller-Logik stabil aufzulösen. |

---

## **3. Erkenntnisse & Ausblick**

Mit Abschluss des Sprints 3 ist das Projekt "Feature Complete". Folgende Erkenntnisse wurden gewonnen:

1.  **Bedeutung der Sicherheitskette (Safety Chain):**
    * **Erkenntnis:** Die Implementierung der Not-Aus-Funktion (Req 5.3) erforderte eine saubere Kommunikation über alle Schichten (GUI -> Controller -> Actuator).
    * **Maßnahme:** Durch den Integration Test **IT14** wurde nachgewiesen, dass die Abschaltung verzögerungsfrei innerhalb eines Regelzyklus erfolgt.

2.  **Herausforderung der zirkulären Abhängigkeiten:**
    * **Erkenntnis:** Die bidirektionale Interaktion zwischen Anzeige (Display) und Logik (WaffelController) führte initial zu Instabilitäten beim Systemstart.
    * **Maßnahme:** Die Einführung einer **Schnittstellen-Injektion** in der `main()`-Funktion löste das Problem und stellt einen sauberen Boot-Vorgang sicher.

3.  **Projektfazit:**
    * **Status:** Alle funktionalen Anforderungen (Temperaturregelung) und nicht-funktionalen Anforderungen (Sicherheit, Performance, Logging) sind erfüllt.
    * **Ergebnis:** Das virtuelle Waffeleisen ist voll einsatzbereit و durch die Traceability Matrix vollständig verifiziert.