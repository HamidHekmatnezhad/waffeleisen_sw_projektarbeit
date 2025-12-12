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

### UT4 – Temperaturmessung: Sensor-Controller-Integration

**Ziel:** Verifikation der Methode `leseTemperatur()`, dass der `WaffelController` die Daten des `TemperatureSensor` (Singleton) korrekt abruft.

**Eingabe:** Simulation des zyklischen Controller-Aufrufs.

**Erwartete Reaktion:** Der Controller empfängt den simulierten Startwert ($25^\circ C$).

**Ergebnis:** Der Controller verarbeitete den Wert korrekt. Die Aufrufsyntax (`PIDRegler` -> `Sensor`) war fehlerfrei.

**Status:** Bestanden

**Requirement:** 2.2

### UT5 – Anzeige des aktuellen Zustands korrekt durchgeführt

**Ziel:** Prüfung, ob die Anzeige (`SimpleGUI`) korrekt auf den Zustandswechsel (`AUFHEIZEN`) reagiert.

**Eingabe:** Auslösen der Methode `starteBackvorgang()`.

**Erwartete Reaktion:** Die Methode `zeigeZustand()` in der GUI wird mit dem Text "AUFHEIZEN" aufgerufen.

**Ergebnis:** Der Status wurde korrekt an die GUI übergeben und das Display aktualisiert (z.B. durch Tkinter-Update).

**Status:** Bestanden

**Requirement:** 1.2

### UT6 – Sollwert-Umrechnung funktioniert wie vorgesehen

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

---