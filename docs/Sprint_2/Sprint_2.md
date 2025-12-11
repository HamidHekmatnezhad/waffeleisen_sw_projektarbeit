# Sprint 2: Erweiterung (Safety, Feedback & Persistence)

### 1. Sprint Planning

**Ziel:** Erweiterung des Waffeleisens um Sicherheitsfunktionen, akustisches Feedback und Datenhaltung (Persistence).

**Ausgewählte Requirements für Sprint 2:**

1.  **Sicherheitsfehleranzeige (Req 4.1):**
    * **Beschreibung:** Bei Fehlern (z.B. Sensor ausfall) muss das Display "FEHLER" anzeigen.
    * **Priorität:** Hoch (Sicherheit).

2.  **Akustisches Signal (Req 5.1):**
    * **Beschreibung:** Ein Summer (Buzzer) soll ertönen, wenn der Backvorgang beendet ist.
    * **Priorität:** Hoch (Usability).

3.  **Datenhaltung & Konfiguration (Req 1.4, 4.2, 2.1):**
    * **Beschreibung:** Einführung einer Persistenz-Schicht (`ConfigLoader`, `DataLogger`), um Texte extern zu laden und Messwerte zu speichern.
    * **Priorität:** Mittel (Architektur-Erweiterung).
