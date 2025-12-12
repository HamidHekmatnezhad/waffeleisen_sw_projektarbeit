# Design (Sprint 3)

## Klassendiagramm

Das Klassendiagramm für **Sprint 3** wurde um die Komponente für die Protokollierung erweitert. Die zentrale Neuerung ist die Klasse **`DataLogger`** in der Datenhaltungsschicht.

**Erweiterungen in Sprint 3:**
* **Neue Klasse `DataLogger`:** Diese Klasse ist für das Speichern von Temperaturverläufen (Req 2.1) und Systemereignissen (Req 5.2) zuständig.
* **Integration:** Der `WaffelController` besitzt eine Referenz auf den `DataLogger` und ruft dessen Methoden zyklisch (Messwerte) oder ereignisbasiert (Statuswechsel) auf.

![Klassendiagramm Sprint 3](/docs/referenziert/design/Klassendiagramm_3.png)
- [ref. code in mermaid](/docs/referenziert/design/Klassendiagramm_3.mmd)
- [ref. image in PNG](/docs/referenziert/design/Klassendiagramm_3.png)

## Sequenzdiagramm

Das Sequenzdiagramm visualisiert den **erweiterten Regelkreis**. Zusätzlich zur Temperaturregelung und dem akustischen Feedback (aus Sprint 2) wird nun gezeigt, wie **in jedem Zyklus** der aktuelle Messwert an den Logger übergeben wird (`log_messwert`). Am Ende des Vorgangs wird zudem ein System-Event gespeichert.

![Sequenzdiagramm Sprint 3](/docs/referenziert/design/Sequenzdiagramm_3.png)
- [ref. code in mermaid](/docs/referenziert/design/Sequenzdiagramm_3.mmd)
- [ref. image in PNG](/docs/referenziert/design/Sequenzdiagramm_3.png)

## Kommunikationsdiagramm

Das Kommunikationsdiagramm zeigt die vollständige Vernetzung des `WaffelController`. Er agiert als zentrale Schaltstelle und verteilt Daten an:
1. Die **GUI** (Anzeige).
2. Den **Regler** (Logik).
3. Den **ConfigLoader** (Input).
4. Den **DataLogger** (Output/Archivierung).
5. Die **Hardware** (Buzzer).

![Kommunikationsdiagramm Sprint 3](/docs/referenziert/design/Kommunikationsdiagramm_3.png)
- [ref. code in mermaid](/docs/referenziert/design/Kommunikationsdiagramm_3.mmd)
- [ref. image in PNG](/docs/referenziert/design/Kommunikationsdiagramm_3.png)