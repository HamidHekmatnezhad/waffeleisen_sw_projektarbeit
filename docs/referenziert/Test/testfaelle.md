# Testfälle
## **Unit Tests**

### UT1 – Heizleistung bei Kaltstart (Maximalleistung)

* **Ziel:** Sicherstellen, dass der Regler bei großer Temperaturdifferenz (Kaltstart) die maximale Heizleistung (1.0 bzw. 100%) anfordert.
* **Ausgangszustand:** `PIDRegler` ist initialisiert. Zieltemperatur (`SetPoint`) ist auf 180°C gesetzt. Integraler Fehler ist 0.
* **Ereignis:** Zyklische Berechnung der Stellgröße.
* **Eingabe:** `istTemp` = 25°C (Raumtemperatur).
* **Erwartete Reaktion:** `calculateHeatingPower()` gibt `1.0` zurück.
* **Erwarteter Folgezustand:** Interne Fehlerwerte (P-Anteil) sind positiv.
* **Klasse:** `PIDRegler`
* **Requirement:** 3.1 (Temperaturregelung), 3.3 (Testbarkeit)

### UT2 – Abschaltung bei Überhitzung (Negative Abweichung)

* **Ziel:** Verifikation, dass die Heizung komplett abschaltet (0.0), wenn die Ist-Temperatur die Soll-Temperatur überschreitet.
* **Ausgangszustand:** `PIDRegler` ist initialisiert. Zieltemperatur (`SetPoint`) ist auf 180°C gesetzt.
* **Ereignis:** Temperatur überschreitet das Ziel (z.B. durch Restwärme).
* **Eingabe:** `istTemp` = 190°C.
* **Erwartete Reaktion:** `calculateHeatingPower()` gibt `0.0` zurück (keine negativen Werte erlaubt).
* **Erwarteter Folgezustand:** Heizung bleibt aus (Stellgröße 0).
* **Klasse:** `PIDRegler`
* **Requirement:** 3.1 (Temperaturregelung / Energieverbrauch)

### UT3 – Begrenzung der Stellgröße (Clamping)

* **Ziel:** Prüfung, ob der Algorithmus den Rückgabewert korrekt auf den Bereich [0.0, 1.0] begrenzt, auch wenn die mathematische Berechnung (P+I+D) theoretisch höhere Werte liefert.
* **Ausgangszustand:** `PIDRegler` mit sehr aggressiven Parametern (hoher Kp) oder extrem großer Regelabweichung.
* **Ereignis:** Berechnung der Stellgröße bei extremen Werten.
* **Eingabe:** `istTemp` = 0°C, `sollTemp` = 250°C.
* **Erwartete Reaktion:** Rückgabewert ist exakt `1.0` (nicht größer als 1).
* **Erwarteter Folgezustand:** Systemstabilität gewährleistet.
* **Klasse:** `PIDRegler`
* **Requirement:** 3.1 (Regelungslogik)

### UT4 – Zusammenspiel Sensor und Controller _(Integrationsebene)_

* **Ziel:** Prüfung, ob der `WaffelController` korrekt auf die Singleton-Instanz des `TemperatureSensor` zugreift und Daten verarbeitet.
* **Ausgangszustand:** System befindet sich im Zustand `AUFHEIZEN`. `TemperatureSensor` liefert simulierten Wert `25.0`.
* **Ereignis:** Aufruf der Methode `runRegelkreisIteration()` im Controller.
* **Eingabe:** Keine direkte Benutzereingabe (zyklischer Aufruf).
* **Erwartete Reaktion:** Controller liest `25.0` vom Sensor, berechnet eine positive Heizleistung (> 0) und übergibt diese an den Aktor.
* **Erwarteter Folgezustand:** `istTemp` im Controller entspricht dem Sensorwert.
* **Klassen:** `WaffelController`, `TemperatureSensor`, `PIDRegler`
* **Requirement:** 2.2 (Temperaturmessung), 3.1 (Regelung)

### UT5 – Aktualisierung der GUI durch Controller _(Integrationsebene)_

* **Ziel:** Sicherstellen, dass Statusänderungen im `WaffelController` (Logik) korrekt an die `SimpleGUI` (Anzeige) propagiert werden.
* **Ausgangszustand:** System ist im `STANDBY`. GUI zeigt "STANDBY".
* **Ereignis:** Benutzer startet den Backvorgang (`starteBackvorgang()`).
* **Eingabe:** Methodenaufruf `starteBackvorgang()`.
* **Erwartete Reaktion:** Controller wechselt intern auf `AUFHEIZEN` und ruft `zeigeZustand("AUFHEIZEN")` an der GUI auf.
* **Erwarteter Folgezustand:** GUI-Property `aktueller_zustand` ist "AUFHEIZEN".
* **Klassen:** `WaffelController`, `SimpleGUI`
* **Requirement:** 1.2 (Anzeige), 4.x (Zustandsanzeige)

### UT6 – Eingabeverarbeitungskette (Button -> Controller -> Solltabelle) _(Integrationsebene)_

* **Ziel:** Verifikation der kompletten Kette von der Benutzereingabe bis zur Änderung der Zieltemperatur.
* **Ausgangszustand:** Aktueller Grad ist 3 (entspricht 180°C).
* **Ereignis:** Benutzer drückt die Plustaste.
* **Eingabe:** Aufruf `simuliereTaste('+')` am `ButtonInput`.
* **Erwartete Reaktion:** 1. `ButtonInput` ruft `verarbeiteEingabe(1)` am Controller.
    2. Controller erhöht Grad auf 4.
    3. Controller fragt `Solltabelle` nach Temperatur für Grad 4.
    4. `Solltabelle` liefert `195`.
* **Erwarteter Folgezustand:** `_sollTemp` im Controller ist `195`.
* **Klassen:** `ButtonInput`, `WaffelController`, `Solltabelle`
* **Requirement:** 1.1 (Einstellung), 3.1 (Zieltemperatur)

---

### UT7 – Laden der Konfiguration und Mehrsprachigkeit (Sprint 2)

* **Ziel:** Verifikation der Klasse `ConfigLoader`, um sicherzustellen, dass Texte dynamisch geladen werden können (Persistence Layer).
* **Ausgangszustand:** `ConfigLoader` ist initialisiert. Keine Konfiguration im Speicher.
* **Ereignis:** Aufruf der Methode `laod_lang("DE")`.
* **Eingabe:** Sprachkürzel "DE".
* **Erwartete Reaktion:** Die Methode gibt ein Dictionary zurück, das zwingend die Schlüssel "BEREIT", "AUFHEIZEN" und "FEHLER" enthält.
* **Erwarteter Folgezustand:** Der `WaffelController` verfügt über die korrekten Anzeigetexte.
* **Klasse:** `ConfigLoader`
* **Requirement:** 1.4 (Konfigurierbare Texte), 4.2 (Mehrsprachigkeit)

### UT8 – Akustische Signalausgabe / Buzzer (Sprint 2)

* **Ziel:** Überprüfung der Hardware-Abstraktion `AkustikSignalgeber` und der Methode `piep()`.
* **Ausgangszustand:** `AkustikSignalgeber` ist initialisiert.
* **Ereignis:** Der Backvorgang ist abgeschlossen (Zustand wechselt zu `BEREIT`).
* **Eingabe:** Aufruf der Methode `piep(anzahl=3)`.
* **Erwartete Reaktion:** Die Methode führt die simulierte Signalausgabe (Konsolen-Print) ohne Laufzeitfehler aus.
* **Erwarteter Folgezustand:** Der Benutzer erhält akustisches Feedback.
* **Klasse:** `AkustikSignalgeber`
* **Requirement:** 5.1 (Akustisches Signal)

---

### UT9 – Protokollierung von Messwerten (Sprint 3)
* **Ziel:** Verifikation, dass Temperaturwerte korrekt im Speicher abgelegt werden.
* **Eingabe:** `log_messwert(180.5)`
* **Erwartete Reaktion:** Der Wert 180.5 wird der Liste `messwerte` hinzugefügt.
* **Requirement:** 2.1

### UT10 – Protokollierung von System-Events (Sprint 3)
* **Ziel:** Verifikation, dass Ereignisse (Start/Stopp) mit Zeitstempel gespeichert werden.
* **Eingabe:** `log_system_event("Test")`
* **Erwartete Reaktion:** Ein String mit Zeitstempel und "Test" landet in `system_logs`.
* **Requirement:** 5.2