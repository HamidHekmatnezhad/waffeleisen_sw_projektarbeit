# Testergebnisse

## Unit Tests

Umgesetzt in src/tests/PIDReglerTest.py (Simulierte Umgebung).

### UT1 – Stellgrößenbegrenzung: Minimalwert

**Ziel:** Sicherstellen, dass die berechnete Stellgröße nicht unter 0.0 fällt (Überhitzungsschutz).

**Ergebnis:** Die Methode behandelte negative Regelfehler korrekt. Bei Ist > Soll wurde der Rückgabewert wie erwartet auf **0.0** korrigiert.

**Status:** Bestanden

**Requirement:** 3.1

### UT2 – Stellgrößenbegrenzung: Maximalwert

**Ziel:** Sicherstellen, dass die berechnete Stellgröße nicht über 1.0 steigt (Begrenzung der Heizleistung).

**Ergebnis:** Extreme positive Fehler wurden ordnungsgemäß erkannt und behandelt. Der Rückgabewert blieb im gültigen Bereich **1.0**.

**Status:** Bestanden

**Requirement:** 3.1

### UT3 – P-Anteil Korrektheit (Kaltstart)

**Ziel:** Verifikation, dass der Proportional-Anteil bei Kaltstart (großer Fehler) eine hohe Stellgröße liefert.

**Eingabe:** Ist-Temperatur = 25°C. Soll-Temperatur = 180°C.

**Erwartung:** Berechnung liefert maximalen Stellwert (1.0).

**Ergebnis:** Die Methode `calculateHeatingPower()` lieferte korrekt einen Wert, der auf **1.0** begrenzt wurde.

**Status:** Bestanden

**Requirement:** 3.3

### IT4 – Temperaturmessung: Sensor-Controller-Integration

**Ziel:** Verifikation der Methode `leseTemperatur()`, dass der `WaffelController` die Daten des `TemperatureSensor` (Singleton) korrekt abruft.

**Eingabe:** Simulation des zyklischen Controller-Aufrufs.

**Erwartete Reaktion:** Der Controller empfängt den simulierten Startwert ($25^\circ C$).

**Ergebnis:** Der Controller verarbeitete den Wert korrekt. Die Aufrufsyntax (`PIDRegler` -> `Sensor`) war fehlerfrei.

**Status:** Bestanden

**Requirement:** 2.2

### IT5 – Anzeige des aktuellen Zustands korrekt durchgeführt

**Ziel:** Prüfung, ob die Anzeige (`SimpleGUI`) korrekt auf den Zustandswechsel (`AUFHEIZEN`) reagiert.

**Eingabe:** Auslösen der Methode `starteBackvorgang()`.

**Erwartete Reaktion:** Die Methode `zeigeZustand()` in der GUI wird mit dem Text "AUFHEIZEN" aufgerufen.

**Ergebnis:** Der Status wurde korrekt an die GUI übergeben und das Display aktualisiert (z.B. durch Tkinter-Update).

**Status:** Bestanden

**Requirement:** 1.2

### IT6 – Sollwert-Umrechnung funktioniert wie vorgesehen

**Ziel:** Prüfung der internen Logik zur Umrechnung des Bräunungsgrads in die Soll-Temperatur.

**Eingabe:** Eingabe von Bräunungsgrad 4.

**Erwartete Reaktion:** Der Controller setzt die interne Soll-Temperatur auf $195^\circ C$.

**Ergebnis:** Die Umrechnung erfolgte korrekt, der Sollwert im `PIDRegler` wurde korrekt aktualisiert.

**Status:** Bestanden

**Requirement:** 1.1

---

### UT7 – Laden der Konfiguration und Mehrsprachigkeit

**Ziel:** Verifikation der Klasse `ConfigLoader`, um sicherzustellen, dass Texte korrekt aus der externen Datenquelle (JSON oder Fallback) geladen werden.

**Eingabe:** Aufruf der Methode `laod_lang("DE")`.

**Erwartete Reaktion:** Rückgabe eines Dictionaries, das die notwendigen Schlüssel ("BEREIT", "AUFHEIZEN", "FEHLER") enthält.

**Ergebnis:** Die Konfiguration wurde erfolgreich geladen. Der `WaffelController` konnte auf die Texte zugreifen und diese in der GUI anzeigen.

**Status:** Bestanden

**Requirement:** 1.4, 4.2

### UT8 – Akustische Signalausgabe (Buzzer)

**Ziel:** Überprüfung der Hardware-Abstraktion `AkustikSignalgeber` und der Methode `piep()`.

**Eingabe:** Aufruf der Methode `piep(anzahl=1)`.

**Erwartete Reaktion:** Die Methode führt die simulierte Signalausgabe (Konsolen-Print) ohne Laufzeitfehler aus.

**Ergebnis:** Der Aufruf erfolgte fehlerfrei. Die Integration im Controller (Auslösen bei Zustand `BEREIT`) war erfolgreich.

**Status:** Bestanden

**Requirement:** 5.1

### IT11 – Überprüfung der Systemreaktionszeit (Sprint 2)

**Ziel:** Verifikation, dass die Verzögerung zwischen einer Benutzereingabe (Tastendruck) und der Systemreaktion (Zustandsänderung) unter 2 Sekunden liegt (Requirement 1.3).

**Vorgehen:** 1. Starten eines Timers mittels `time.time()` unmittelbar vor dem Aufruf der Methode `verarbeiteEingabe()` durch die UI-Komponente.
2. Ausführung der vollständigen Logik-Kette: `ButtonInput` -> `WaffelController` -> `Zustandsaktualisierung`.
3. Stoppen des Timers nach Abschluss der Verarbeitung und Berechnung der Differenz.

**Ergebnis:** Die gemessene Zeit für die gesamte Verarbeitungskette betrug im Durchschnitt **0,0018 Sekunden**. Damit wird der geforderte Grenzwert von 2,0 Sekunden (Requirement 1.3) deutlich unterschritten. Die Integration zwischen UI-Eingabe und Logیک-Verarbeitung ist performant.

**Status:** Bestanden

**Requirement:** 1.3

---

### UT9 – DataLogger Messwerte
**Ziel:** Testen der Speicherung von Temperaturen.

**Ergebnis:** Werte wurden korrekt in die Liste geschrieben.

**Status:** Bestanden (Requirement 2.1)

### IT10 – DataLogger Events
**Ziel:** Testen der Event-Logs.

**Ergebnis:** Nachrichten wurden korrekt mit Zeitstempel formatiert und gespeichert.

**Status:** Bestanden (Requirement 5.2)

### IT12 – Sensor-Plausibilität bei Umgebungstemperatur (Sprint 3)

**Ziel:** Verifikation, dass der `WaffelController` die Rohdaten des `TemperatureSensor` beim Systemstart korrekt empfängt und als plausible Umgebungstemperatur interpretiert (Requirement 2.3).

**Vorgehen:** Simulation eines Systemstarts (Kaltstart). Der Controller fragt zyklisch den Sensor-Status ab, bevor der Heizvorgang aktiviert wird.

**Ergebnis:** Der Sensor lieferte einen stabilen Wert von **22,4°C**. Der Controller verarbeitete diesen Wert korrekt und blieb erwartungsgemäß im Zustand `STANDBY`. Die Kommunikation zwischen Hardware-Simulation (Sensor-Singleton) und der Logikschicht (Controller) ist fehlerfrei.

**Status:** Bestanden

**Requirement:** 2.3

### UT13 – Mathematische Leistungsbegrenzung (Sprint 3)

**Ziel:** Verifikation der physikalischen Begrenzung der Heizleistung auf maximal 100W (Requirement 3.2).

**Vorgehen:** Die Methode `calculateHeatingPower()` innerhalb der Klasse `PIDRegler` wurde isoliert getestet. Es wurde untersucht, wie die Methode auf verschiedene Eingabewerte der Stellgröße ($u$) reagiert, insbesondere bei Werten außerhalb des Standardbereichs [0.0, 1.0].

**Ergebnis:** * Bei einer Stellgröße von $u = 0.5$ wurde eine Leistung von **50.0W** berechnet.
* Bei der maximal zulässigen Stellgröße von $u = 1.0$ betrug die Leistung exakt **100.0W**.
* Bei einem fehlerhaften theoretischen Eingangswert von $u = 1.5$ griff die interne Begrenzung (Saturation), und der Rückgabewert blieb stabil bei **100.0W**.
Damit ist nachgewiesen, dass das System die Hardware-Anforderungen zum Energieverbrauch softwareseitig strikt einhält.

**Status:** Bestanden

**Requirement:** 3.2    

### IT14 – Verfügbarkeit der Sicherheitsabschaltung (Sprint 3)

**Ziel:** Nachweis der sofortigen Deaktivierung der Heizleistung bei Systemstopp oder manuellem Abbruch (Requirement 5.3).

**Vorgehen:** Während eines aktiven Aufheizvorgangs (simulierte Stellgröße > 0) wurde die Methode `stoppeProzess()` über die Benutzeroberfläche (STOP-Button) aufgerufen. Dabei wurde die Reaktion des `HeaterActuator`, der Zustandswechsel im `WaffelController` sowie die Protokollierung im `DataLogger` überprüft.

**Ergebnis:** Nach Auslösen der Funktion wurde die Heizleistung unmittelbar auf **0.0W** herabgesetzt. Der Systemstatus wechselte korrekt von `AUFHEIZEN` zu `STANDBY`. Die Anzeige in der GUI wurde verzögerungsfrei aktualisiert. Das Ereignis wurde zudem erfolgreich im `DataLogger` mit dem Zeitstempel "MANUAL_STOP" hinterlegt. Die Sicherheitskette zwischen UI, Logik und Hardware-Abstraktion funktioniert einwandfrei.

**Status:** Bestanden

**Requirement:** 5.3

