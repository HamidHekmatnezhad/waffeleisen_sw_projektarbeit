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
---
---

### 2. Review: Soll-Ist-Vergleich

Nach Abschluss der Implementierung wurden Architektur und Design mit dem tatsächlichen Code verglichen. Dabei wurden folgende Abweichungen festgestellt und dokumentiert:

| Bereich | Geplantes Design (Soll) | Tatsächliche Implementierung (Ist) | Grund für die Abweichung |
| :--- | :--- | :--- | :--- |
| **Concurrency / Threading** | Ursprünglich war geplant, die GUI und den Controller in separaten **Threads** laufen zu lassen (siehe erste Sequenzdiagramme). | Die Umsetzung erfolgte **Single-Threaded** mittels eines Schedulers (`root.after()` in Tkinter). | Vermeidung von komplexen Synchronisationsproblemen und Race Conditions in der GUI-Bibliothek (Tkinter ist nicht Thread-safe). Die Lösung ist stabiler. |
| **Singleton Pattern** | Klassische Implementierung über eine `getInstance()` Methode in einer Klasse. | Umsetzung mittels **Modul-basierter Funktion** (`get_sensor_instance`) und privatem Konstruktor-Check. | Anpassung an die Idiome der Programmiersprache **Python**, um den Code pythonischer und einfacher lesbar zu machen. |
| **PID-Regler** | Vollständiger PID-Algorithmus (Proportional, Integral, Differential). | Fokus auf **PI-Verhalten** (D-Anteil initial auf 0 gesetzt). | Für die thermische Trägheit des Waffeleisens reichte im ersten Schritt ein PI-Regler aus; der D-Anteil erhöhte die Komplexität ohne direkten Nutzen in der Simulation. |

---

### 3. Erkenntnisse & Ausblick 

Basierend auf den Erfahrungen aus Sprint 1 ergeben sich folgende Erkenntnisse für die Planung von Sprint 2:

1.  **Wichtigkeit der Traceability:**
    * **Erkenntnis:** Die Traceability Matrix muss *parallel* zur Entwicklung gepflegt werden, nicht erst am Ende. Das Fehlen von Design-Links (Methodennamen) führte zu Feedback-Schleifen.
    * **Maßnahme Sprint 2:** Bei der Implementierung neuer Features (z.B. Akustik) wird die Matrix sofort um die neuen Klassen/Methoden erweitert.

2.  **Komplexität der Simulation:**
    * **Erkenntnis:** Das Testen des Reglers ohne echte Hardware erfordert eine gute Simulation der Temperaturkurve im `TemperatureSensor`.
    * **Maßnahme Sprint 2:** Die Simulationslogik im Sensor muss ggf. verfeinert werden (Abkühlkurven), um realistischere Tests zu ermöglichen.

3.  **Architektur-Bestätigung:**
    * **Erkenntnis:** Die 4-Schichten-Architektur hat sich bewährt. Änderungen an der GUI (z.B. Threading-Umbau) hatten keine Auswirkungen auf den Kern-Regler.
    * **Maßnahme:** Beibehaltung der strikten Schichtentrennung für kommende Features.