# Testdokumentation (Sprint 2)

## **1. Ziel der Tests**

Das Ziel der Tests in Sprint 2 ist die Verifikation und Validierung der neu eingeführten **Datenhaltungsschicht** und der **erweiterten Hardware-Abstraktion** im Hinblick auf:

* **Datenintegrität & Persistenz:** Sicherstellen, dass Konfigurationsdaten (Texte, Spracheinstellungen) korrekt aus externen Quellen (JSON) geladen werden (Req 1.4, 4.2).
* **Feedback-Systeme:** Überprüfung der korrekten Ansteuerung des akustischen Signalgebers bei Prozessende (Req 5.1).
* **Integration:** Sicherstellen, dass der `WaffelController` die geladenen Texte korrekt an die GUI weiterleitet und Hardware-Signale zum richtigen Zeitpunkt auslöst.

---

## **2. Testarten und Abdeckung**

### 2.1 Unit Tests 

Ziel: Isolierte Prüfung der neuen Klassen, um die Funktionsfähigkeit der Konfiguration und Hardware-Simulation sicherzustellen.

* **Abdeckung:** * Logik der `ConfigLoader`-Klasse (Laden, Fallback auf Defaults).
    * Logik der `AkustikSignalgeber`-Klasse (Simulierte Ausgabe).
* **Beispiele:** * **UT7:** Laden einer Sprachkonfiguration und Prüfung auf Vorhandensein notwendiger Keys ("BEREIT", "AUFHEIZEN").
    * **UT8:** Aufruf der `piep()`-Methode ohne Laufzeitfehler.

### 2.2 Integration Tests

Ziel: Überprüfung der Zusammenarbeit zwischen dem Controller und den neuen Komponenten.

* **Abdeckung:** * Datenfluss von `ConfigLoader` -> `WaffelController` -> `SimpleGUI` (Anzeige korrekter Texte).
    * Kontrollfluss von `WaffelController` -> `AkustikSignalgeber` (Signalton bei Zustand `BEREIT`).

---

## **3. Teststrategie**

Die Teststrategie erweitert das Vorgehen aus Sprint 1 um Dateisystem-Tests und Mocking-Techniken.

* **Automatisierte Tests:** Unit-Tests prüfen, ob die JSON-Struktur korrekt geparst wird und ob die Klassen instanziierbar sind.
* **Manuelle Tests:** Da der Summer (Buzzer) nur simuliert ist (Print-Ausgabe), muss visuell in der Konsole geprüft werden, ob "PIEP" ausgegeben wird, wenn die Waffel fertig ist. Ebenso wird geprüft, ob die GUI-Texte sich ändern, wenn die Config angepasst wird.
* **Regressionstests:** Sicherstellen, dass die bestehende Regelung (PID) durch die Umbauten im Controller nicht beeinträchtigt wurde.

### Testumgebung:

* **Simulierte Dateien:** Verwendung einer lokalen `config.json` (oder Default-Werte im Code) für Tests.
* **Simulierte Hardware:** Konsolenausgabe als Ersatz für den physischen Summer.
* **Plattform:** Python/Tkinter.

---

## **4. Testumfang**

### In-Scope:

* Laden von Sprachdaten aus JSON (Req 1.4, 4.2).
* Anzeige von Fehlermeldungen via Config (Req 4.1).
* Auslösen des akustischen Signals (Req 5.1).
* Integration der neuen Komponenten in den `WaffelController`.

### Out-of-Scope:

* Physische Hardware-Anbindung (echter GPIO-Buzzer).
* Komplexes Error-Handling bei beschädigten JSON-Dateien (nur Basic-Fallback getestet).
* Dynamisches Umschalten der Sprache zur Laufzeit (nur beim Start).

## Definition Testfälle inkl. betroffener Requirements
[Testfälle](../../tests/Testfaelle.md)

## Dokumentation der Ergebnisse
[Testergebnisse](../../tests/Testergebnisse.md)