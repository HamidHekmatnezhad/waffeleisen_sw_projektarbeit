## Sprint 1

**Ziel:** Implementierung der geschlossenen Regelschleife (Temperaturmessung und Heizleistungsregelung) als Basis für das Waffelbacken.

**Ausgewählte Hauptfunktionen:**

1.  **Auswahl des Bräunungsgrads (Req 1.1, 1.2):**
    * **Beschreibung:** Der Benutzer kann den Bräunungsgrad über Tasten einstellen. Die aktuelle Stufe wird angezeigt.
    * **Begründung:** Stellt die notwendige **Solltemperatur-Vorgabe** und die minimale Benutzerinteraktion bereit.

2.  **Temperaturmessung und -überwachung (Req 2.2):**
    * **Beschreibung:** Die Temperatur muss alle 100ms über den Sensor eingelesen werden.
    * **Begründung:** Essentiell für die **Regelungslogik**.

3.  **Heizleistungsregelung (Req 3.1, 3.3):**
    * **Beschreibung:** Der Regelungsalgorithmus hält die Zieltemperatur mit maximal 3°C Abweichung. Die **Testbarkeit** des Algorithmus (Req 3.3) wird in diesem Sprint ebenfalls adressiert.
    * **Begründung:** Die zentrale **Steuerungsfunktion** des Geräts.

4.  **Zustandsanzeige (Minimal, Teil von 4.x):**
    * **Beschreibung:** Anzeige der Zustände "Aufheizen" und "Bereit".
    * **Begründung:** Minimales Feedback, um dem Benutzer zu signalisieren, dass der Prozess läuft.