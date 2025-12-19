# Testdokumentation

## **1. Ziel der Tests**

Das Ziel der Tests ist die Verifikation und Validierung des **Regelkreises** im Hinblick auf:

* **Algorithmische Korrektheit:** Sicherstellen, dass die Berechnung der Heizleistung (durch den `PIDRegler`) korrekt und präzise erfolgt (Req 3.1, 3.3).
* **Funktionale Integrität:** Sicherstellen, dass die Temperaturmessung (Req 2.2) und die Sollwert-Einstellung (Req 1.1) korrekt funktionieren.
* **Robuste Systemreaktion:** Überprüfung der Reaktion auf interne Eingaben und Zustandsübergänge (z.B. Umschalten auf `BEREIT`).

---

## **2. Testarten und Abdeckung**

### 2.1 Unit Tests 

Ziel: Prüfung der kleinstmöglichen Testeinheiten, um fehlerhafte **Kernlogik** frühzeitig zu erkennen.

* **Abdeckung:** Logik der `PIDRegler`-Klasse.
* **Beispiele:** Überprüfung der Stellgrößenbegrenzung (Clamping) und der Reaktion auf Überhitzung (UT1, UT2, UT3).

### 2.2 Integration Tests

Ziel: Überprüfung der Zusammenarbeit und korrekten Aufrufsyntax zwischen zwei oder mehr Komponenten.

* **Abdeckung:** Datenfluss von `ButtonInput` zum `WaffelController` zur `Solltabelle` (**IT6**) und von `TemperatureSensor` zum `PIDRegler` (**IT4**).

---

## **3. Teststrategie**

Die Teststrategie kombiniert die Zuverlässigkeit von automatisierten Tests mit der notwendigen manuellen Überprüfung der physikalischen UI-Interaktion.

* **Automatisierte Tests:** Fokus auf alle testbaren Codeeinheiten (insbesondere `PIDRegler` zur Erfüllung von Req 3.3).
* **Manuelle Tests:** Manuelle Überprüfung der Zustandsanzeige (`SimpleGUI`) und der Funktionalität der Tasten.
* **Regressionstests:** Nach jeder Anpassung an der Kontrolllogik muss der gesamte Satz an Unit Tests erneut durchgeführt werden.

### Testumgebung:

* **Simulierte Sensoren:** Verwendung von Software-Simulatoren zur Eingabe von Testdaten in den `PIDRegler`.
* **Plattform:** Python/Tkinter.

---

## **4. Testumfang**

### In-Scope:

* Berechnung und Regelung der Temperatur (Req 3.1).
* Messung der Ist-Temperatur (Req 2.2).
* Begrenzung der Heizleistung auf den zulässigen Bereich [0.0, 1.0].
* Reaktion auf Benutzereingaben (Knopfdrücke).

### Out-of-Scope:

* Hardwareseitiges Batterieverhalten oder Störungen.
* Langzeitverhalten oder Kalibrierungsfehler.

## Definition Testfälle inkl. betroffener Requirements
[Testfälle](/docs/referenziert/Test/testfaelle.md)

## Dokumentation der Ergebnisse
[Testergebnisse](/docs/referenziert/Test/Testergebnisse.md)
