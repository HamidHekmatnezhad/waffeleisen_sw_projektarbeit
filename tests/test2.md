# Testdokumentation (Sprint 2)

## **1. Ziel der Tests**

Das Ziel der Tests in Sprint 2 ist die Verifikation der erweiterten Hardware-Abstraktion, der Benutzerschnittstelle und der Echtzeit-Performance des Systems:

* **Datenintegrität & Persistenz:** Sicherstellen, dass Konfigurationsdaten (Texte, Spracheinstellungen) korrekt geladen werden (Req 1.4, 4.2).
* **Feedback-Systeme:** Überprüfung der korrekten Ansteuerung des akustischen Signalgebers bei Prozessende (Req 5.1).
* **Performance (Echtzeitfähigkeit):** Verifikation, dass die Systemreaktionszeit auf Benutzereingaben unter 2 Sekunden liegt (Req 1.3).
* **Integration:** Sicherstellen, dass der `WaffelController` die geladenen Texte korrekt an die GUI weiterleitet und die Eingabekette performant verarbeitet wird.

---

## **2. Testarten und Abdeckung**

### 2.1 Unit Tests 

Ziel: Isolierte Prüfung der neuen Klassen zur Sicherstellung der korrekten internen Logik.

* **Abdeckung:** * Logik der `ConfigLoader`-Klasse (Erfolgreiches Laden und Fallback-Mechanismen).
    * Logik der `AkustikSignalgeber`-Klasse (Korrekte Simulation der Tonausgabe).
* **Beispiele:** * **UT7:** Validierung der geladenen Sprach-Keys aus der JSON-Konfiguration.
    * **UT8:** Aufruf der `piep()`-Methode und Prüfung der Konsolenausgabe.

### 2.2 Integration Tests

Ziel: Überprüfung des Zusammenspiels zwischen Controller, GUI und der Eingabeverarbeitung.

* **Abdeckung:** * **IT5:** Datenfluss von `ConfigLoader` -> `WaffelController` -> `SimpleGUI` (Anzeige sprachspezifischer Texte).
    * **IT11:** Zeitmessung der gesamten Verarbeitungskette: `ButtonInput` -> `WaffelController` (Sicherstellung der Reaktionszeit).
    * Kontrollfluss von `WaffelController` -> `AkustikSignalgeber` (Auslösen des Signals bei Zustandswechsel zu BEREIT).

---

## **3. Teststrategie**

Die Teststrategie kombiniert funktionale Prüfungen mit Performance-Messungen.

* **Automatisierte Tests:** Durchführung einer Zeitmessung mittels `time.time()` für IT11, um die Verarbeitungsgeschwindigkeit objektiv zu validieren.
* **Manuelle Tests:** Visuelle Kontrolle der GUI-Texte bei verschiedenen Konfigurationsdateien und Überwachung der Konsolenausgabe für den simulierten Buzzer.
* **Regressionstests:** Sicherstellen, dass die Einführung der Konfigurationsschicht die Stabilität des PID-Regelkreises aus Sprint 1 nicht negativ beeinflusst.

### Testumgebung:

* **Zeit-Simulation:** Verwendung von System-Timern zur Messung der Millisekunden-Reaktion.
* **Simulierte Hardware:** Konsolenausgabe als Ersatz für den physischen Summer.
* **Plattform:** Python/Tkinter.

---

## **4. Testumfang**

### In-Scope:

* Laden von Sprachdaten aus JSON (Req 1.4, 4.2).
* **Einhaltung der maximalen Reaktionszeit von 2 Sekunden (Req 1.3).**
* Auslösen des akustischen Signals (Req 5.1).
* Anzeige von Fehlermeldungen via Config (Req 4.1).

### Out-of-Scope:

* Anbindung physischer GPIO-Hardware (echter Buzzer).
* Dynamisches Umschalten der Sprache während des laufenden Betriebs (nur Initialisierung).

## Definition Testfälle inkl. betroffener Requirements
[Testfälle](/docs/referenziert/Test/testfaelle.md)

## Dokumentation der Ergebnisse
[Testergebnisse](/docs/referenziert/Test/Testergebnisse.md)