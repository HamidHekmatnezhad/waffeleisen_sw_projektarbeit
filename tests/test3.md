# Testdokumentation (Sprint 3)

## **1. Ziel der Tests**

Das Ziel der Tests in Sprint 3 ist die Verifikation und Validierung der neu eingeführten **Protokollierungskomponente (Logging)** sowie der Abschlussprüfung des Gesamtsystems im Hinblick auf:

* **Datenintegrität:** Sicherstellen, dass Messwerte (Temperatur) kontinuierlich und korrekt aufgezeichnet werden (Req 2.1).
* **Ereignisverfolgung:** Überprüfung, ob wichtige Systemzustände (Start, Ende, Abschaltung) mit einem korrekten Zeitstempel protokolliert werden (Req 5.2).
* **Systemstabilität:** Sicherstellen, dass der zusätzliche Logging-Prozess die Echtzeitfähigkeit des Regelkreises nicht negativ beeinflusst.

---

## **2. Testarten und Abdeckung**

### 2.1 Unit Tests 

Ziel: Isolierte Prüfung der `DataLogger`-Klasse, um sicherzustellen, dass Daten korrekt in den internen Speicherstrukturen (Listen/Ringpuffer) abgelegt werden.

* **Abdeckung:** * Logik der `DataLogger`-Klasse.
    * Funktion des Ringpuffers (Begrenzung der Einträge).
    * Formatierung von Zeitstempeln.
* **Beispiele:** * **UT9:** Aufruf von `log_messwert()` und Prüfung, ob der Wert in der Liste gespeichert wurde.
    

### 2.2 Integration Tests

Ziel: Überprüfung der Zusammenarbeit zwischen dem `WaffelController` und dem `DataLogger`.

* **Abdeckung:** * Datenfluss vom Regelkreis (`runRegelkreisIteration`) zum Logger (zyklisches Speichern).
    * Auslösen von Events im Controller (z.B. bei Zustandswechsel zu `BEREIT`) und Weiterleitung an den Logger.
    * **Hinweis:** Dies stellt sicher, dass der Controller die Instanz des Loggers korrekt nutzt (Integration).
* **IT10**: Verifikation, dass System-Events vom Controller korrekt an den DataLogger übergeben werden

---

## **3. Teststrategie**

Die Teststrategie in Sprint 3 konzentriert sich auf die **Datenvalidierung** im Speicher und die visuelle Prüfung der Konsolenausgaben.

* **Automatisierte Tests:** Unit-Tests instanziieren den Logger, schreiben Testdaten und validieren anschließend den Inhalt der Listen.
* **Manuelle Tests:** Während des Programmablaufs wird die Konsole überwacht. Es wird geprüft, ob Log-Nachrichten synchron zu den Aktionen erscheinen.
* **Regressionstests:** Ein vollständiger Durchlauf aller bisherigen Unit- und Integrationstests (**UT1-UT3, UT7-UT8 sowie IT4-IT6 und IT10**) stellt sicher, dass die neuen Logging-Funktionen keine bestehenden Features beschädigt haben.

### Testumgebung:

* **In-Memory Storage:** Die Tests nutzen Listen im Arbeitsspeicher zur Simulation der Datenspeicherung.
* **Zeit-Simulation:** Für Unit-Tests wird die Systemzeit als gegeben angenommen.
* **Plattform:** Python/Tkinter.

---

## **4. Testumfang**

### In-Scope:

* Protokollierung der Ist-Temperatur in jedem Regelungszyklus (Req 2.1).
* Simulation eines Ringpuffers.
* Protokollierung von "Start" und "Ende" Ereignissen (Req 5.2).
* Integration des Loggers in den Haupt-Controller.

### Out-of-Scope:

* Persistente Speicherung in einer Datenbank (SQL).
* Langzeit-Performance-Tests (> 24 Stunden).

## Definition Testfälle inkl. betroffener Requirements
[Testfälle](/docs/referenziert/Test/testfaelle.md)

## Dokumentation der Ergebnisse
[Testergebnisse](/docs/referenziert/Test/Testergebnisse.md)