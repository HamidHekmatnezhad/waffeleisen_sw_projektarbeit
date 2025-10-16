# Pflichtenheft: Bräunungsgradsteuerung für Waffeleisen

## 1. Anzeige des Bräunungsgrads

* **Implementierung der Anzeige (TF 4):** Implementierung einer gut sichtbaren, intuitiv verständlichen Anzeige des aktuell **eingestellten** und des **erreichten** Bräunungsgrades (z.B. Segmentanzeige, Farbcodes oder LED-Balken).
* **Anzeigekomplexität:** Die Anzeige der Bräunungssteuerung **darf nicht** überladen oder komplex wirken.
* **Aktualisierung:** Verzögerungsfreie Aktualisierung des Back-Status (z.B. Wechsel von "Aufheizen" zu "Bereit") mit einer maximalen Reaktionszeit von **200ms**.

## 2. Statusanzeige des Backvorgangs

* **Zwei Hauptanzeigen (TF 4):**
    * **"Aufheizen aktiv"** (z.B. blinkendes Symbol oder Animation), bis die Backtemperatur erreicht ist.
        * **"Backvorgang abgeschlossen"** (z.B. dauerhaft leuchtendes Symbol + akustisches Signal).
        * **Zustandserkennung:** Die Zustandserkennung erfolgt über den **Temperatur-Regelungsalgorithmus (TF 3)** und die **Sensorwerte (TF 2)**.

        ## 3. Warnfunktion bei Überhitzung

        * **Benutzerdefinierbare Warnschwelle (TF 5):** Es **muss** eine **kritische Temperaturschwelle** definiert werden (z.B. $10^{\circ} C$ über dem Maximum des höchsten Bräunungsgrades), bei deren Überschreitung eine Warnung ausgelöst wird.
        * **Signalsystem:** Visuelles (blinkende Fehlermeldung) und akustisches Signal bei Unterschreitung der Sicherheitsschwelle.

        ## 4. Zugänglichkeit der Anzeige

        * **Abrufbarkeit der Einstellung (TF 1):** Der **zuletzt eingestellte Bräunungsgrad** **muss** abrufbar sein (Speicherung im EEPROM).
        * **Barrierefreiheit:** Die Anzeige **sollte** barrierefrei für Farbenblinde und ältere Nutzer gestaltet sein.

        ## 5. Information bei technischen Fehlern (Safety)

        * **Fehlermeldung (TF 5):** Eine Fehlermeldung **muss** bei einem Problem in der Heizsteuerung oder Sensorik ausgegeben werden (z.B. "Temperaturfehler").
        * **Ursachen:** Mögliche Ursachen sind z.B. Sensor-Defekt, Überhitzung oder Defekt des Heizelements.

        ## 6. Robustheit und Zuverlässigkeit

        * **Umgebungsbedingungen (TF 2):** Die Steuerung **muss** bei Umgebungstemperaturen von **$0^{\circ} C – 45^{\circ} C$** korrekt arbeiten.
        * **Langzeitstabilität:** Die Bräunungsgradkontrolle **soll** auch nach längerer Nichtbenutzung zuverlässig starten.

        ## 7. Anzeige der Back-Restlaufzeit (Soll-Feature)

        * **Dynamische Berechnung (TF 4):** Dynamische Berechnung und Anzeige der **ungefähr verbleibenden Backzeit** in Minuten, basierend auf dem eingestellten Bräunungsgrad und der aktuellen Temperaturdifferenz (IST- zu SOLL-Temperatur).

        ## 8. Komfort und Ergonomie

        * **Bedienkomplexität:** Keine zusätzliche Komplexität durch die Anzeige im Backprozess.
        * **Displayhelligkeit:** Die Displayhelligkeit **soll** dimmbar sein (z.B. für den Gebrauch in dunklen Küchen).

        ## 9. Steuerungsparameter (Basis der Regelung)

        * **Regelungsart:** PID-Regler (Proportional-Integral-Derivative).
        * **Zielspannung des Sensors:** 3,7 Volt.
        * **Reaktionszeit (Regelung):** Der Regelzyklus des PID-Algorithmus **muss** mindestens **alle 50ms** durchlaufen.

        ## 10. Sensorik und Schwellwerte (Analog zur Batterieerkennung)

        | Bräunungsgrad (Stufe) | Zieltemperatur (SOLL, z.B.) | Anzeigelogik (Status) |
        | :--- | :--- | :--- |
        | **Level 5 (Max.)** | ca. $195^{\circ} C$ | **Fertig:** Signalisierung bei Erreichen der Zieltemperatur. |
        | **Level 3 (Medium)** | ca. $170^{\circ} C$ | **Bereit:** Signalisierung, wenn die Temperatur $170^{\circ} C \pm 3^{\circ} C$ erreicht. |
        | **Level 1 (Min.)** | ca. $145^{\circ} C$ | **Backen:** Status aktiv, wenn Heizelement unter Kontrolle des Reglers steht. |
        | **Sicherheitsabschaltung** | $\mathbf{> 210^{\circ} C}$ | **Kritisch:** System schaltet ab und gibt Fehler aus (Notabschaltung). |

        ## 11. Schutzmechanismen für Langlebigkeit und Sicherheit (TF 5)

        * **Sensordefekt:** Bei Ausfall des Temperatursensors **muss** die Stromzufuhr sofort unterbrochen werden.
        * **Überhitzungsschutz:** Die Heizelemente **dürfen** die maximale Sicherheitstemperatur von $210^{\circ} C$ **nicht überschreiten** (Hardware-Sicherung erforderlich).
        * **Funktionale Sicherheit:** Ein **Hardware-Watchdog** **muss** die korrekte Ausführung des Regelungsalgorithmus überwachen.
        
