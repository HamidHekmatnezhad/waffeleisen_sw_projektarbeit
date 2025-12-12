# Testdokumentation (Sprint 3)

## **1. Ziel der Tests**

Das Ziel der Tests in Sprint 3 ist die Verifikation und Validierung der neu eingeführten **Protokollierungskomponente (Logging)** sowie der Abschlussprüfung des Gesamtsystems im Hinblick auf:

* **Datenintegrität:** Sicherstellen, dass Messwerte (Temperatur) kontinuierlich und korrekt aufgezeichnet werden (Req 2.1).
* **Ereignisverfolgung:** Überprüfung, ob wichtige Systemzustände (Start, Ende, Abschaltung) mit einem korrekten Zeitstempel protokolliert werden (Req 5.2).
* **Systemstabilität:** Sicherstellen, dass der zusätzliche Logging-Prozess die Echtzeitfähigkeit des Regelkreises (100ms Takt) nicht negativ beeinflusst.

---

## **2. Testarten und Abdeckung**

### 2.1 Unit Tests 

Ziel: Isolierte Prüfung der `DataLogger`-Klasse, um sicherzustellen, dass Daten korrekt in den internen Speicherstrukturen (Listen/Ringpuffer) abgelegt werden.

* **Abdeckung:** * Logik der `DataLogger`-Klasse.
    * Funktion des Ringpuffers (Begrenzung der Einträge).
    * Formatierung von Zeitstempeln.
* **Beispiele:** * **UT9:** Aufruf von `log_messwert()` und Prüfung, ob der Wert in der Liste gespeichert wurde.
    * **UT10:** Aufruf von `log_system_event()` und Prüfung, ob der Eintrag den Zeitstempel und die Nachricht enthält.

### 2.2 Integration Tests

Ziel: Überprüfung der Zusammenarbeit zwischen dem `WaffelController` und dem `DataLogger`.

* **Abdeckung:** * Datenfluss vom Regelkreis (`runRegelkreisIteration`) zum Logger (zyklisches Speichern).
    * Auslösen von Events im Controller (z.B. bei Zustandswechsel zu `BEREIT`) und Weiterleitung an den Logger.

---

## **3. Teststrategie**

Die Teststrategie in Sprint 3 konzentriert sich auf die **Datenvalidierung** im Speicher und die visuelle Prüfung der Konsolenausgaben.

* **Automatisierte Tests:** Unit-Tests instanziieren den Logger, schreiben Testdaten und validieren anschließend den Inhalt der Listen (`messwerte`, `system_logs`).
* **Manuelle Tests:** Während des Programmablaufs wird die Konsole überwacht. Es wird geprüft, ob Log-Nachrichten (z.B. "++ LOG: ...") synchron zu den Aktionen (Backen starten/beenden) erscheinen.
* **Regressionstests:** Ein vollständiger Durchlauf aller bisherigen Tests (UT1-UT8) stellt sicher, dass die neuen Logging-Funktionen keine bestehenden Features (PID, Config, Buzzer) beschädigt haben.

### Testumgebung:

* **In-Memory Storage:** Die Tests nutzen Listen im Arbeitsspeicher zur Simulation der Datenspeicherung.
* **Zeit-Simulation:** Für Unit-Tests wird die Systemzeit als gegeben angenommen.
* **Plattform:** Python/Tkinter.

---

## **4. Testumfang**

### In-Scope:

* Protokollierung der Ist-Temperatur in jedem Regelungszyklus (Req 2.1).
* Simulation eines Ringpuffers (Begrenzung auf die letzten N Werte).
* Protokollierung von "Start" und "Ende" Ereignissen mit Zeitstempel (Req 5.2).
* Integration des Loggers in den Haupt-Controller.

### Out-of-Scope:

* Persistente Speicherung in einer Datenbank (SQL) oder Datei (CSV/TXT) – im aktuellen Sprint erfolgt die Speicherung flüchtig (In-Memory).
* Langzeit-Performance-Tests (> 24 Stunden).
* Datenschutz/Verschlüsselung der Logs.

## Definition Testfälle inkl. betroffener Requirements
[Testfälle](/docs/referenziert/Test/testfaelle.md)

## Dokumentation der Ergebnisse
[Testergebnisse](/docs/referenziert/Test/Testergebnisse.md)