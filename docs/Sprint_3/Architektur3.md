# Architektur (Sprint 3)

## Komponentendiagramm

Das Diagramm wurde in Sprint 3 um die Komponente **DataLogger** in der Datenhaltungsschicht erweitert. Diese Komponente ist für die Protokollierung von Messwerten und Systemereignissen zuständig.

![Komponentendiagramm Sprint 3](/docs/referenziert/design/Komponentendiagramm_3.png)
- [ref. code in mermaid](/docs/referenziert/design/Komponentendiagramm_3.mmd)
- [ref. image in PNG](/docs/referenziert/design/Komponentendiagramm_3.png)

---

## Zuordnung der Requirements zu Komponenten

| **Komponente / Schicht** | **Zugehörige Requirements** |
| :--- | :--- |
| **Benutzeroberfläche (UI)** | Req. 1.1, 1.2, 4.1 |
| **Anwendungsschicht (App)** | Req. 1.1, 1.3, 3.1 |
| **Regelungsschicht (Core)** | Req. 3.1, 3.3 |
| **Hardware-Abstraktion (HAL)** | Req. 2.2, 5.1 |
| **Datenhaltungsschicht (Persistence)** | Req. 1.4, 4.2, **2.1 (Messwert-Log), 5.2 (Event-Log)** |

---

## Verantwortlichkeiten der Komponenten

| **Komponente** | **Rolle** | **Verantwortlichkeiten** |
| :--- | :--- | :--- |
| **Benutzeroberfläche** | Präsentationsschicht | Anzeige von Status, Fehlern und Bedienung. |
| **Anwendungsschicht** | Steuerungslogik | Koordination des Gesamtablaufs. Nutzt nun den Logger zur Aufzeichnung des Backprozesses. |
| **Regelungsschicht** | Regelungslogik | Berechnung der Heizleistung (PID). |
| **Hardware-Abstraktion** | Treiber | Zugriff auf Sensoren, Heizelement und Buzzer. |
| **Datenhaltungsschicht** | Persistence & Logging | **Erweitert:** Neben der Konfiguration (`ConfigLoader`) übernimmt diese Schicht nun auch die Protokollierung (`DataLogger`) von Temperaturen und Events. |

---

## Schnittstellen (Aktualisiert für Sprint 3)

| Interface (Methode) | Sender (Aufrufer) | Empfänger (Klasse) | **Beschreibung** | **Daten / Signatur** |
| :--- | :--- | :--- | :--- | :--- |
| **`log_messwert()`** | `WaffelController` | `DataLogger` | **NEU:** Speichert die aktuelle Ist-Temperatur im Protokoll. | **Input:** `temp: float`. |
| **`log_system_event()`** | `WaffelController` | `DataLogger` | **NEU:** Protokolliert wichtige Ereignisse (Start/Stopp/Fehler). | **Input:** `nachricht: str`. |
| **`laod_lang()`** | `WaffelController` | `ConfigLoader` | Lädt GUI-Texte. | **Input:** `lang: str`. **Output:** `dict`. |
| **`piep()`** | `WaffelController` | `AkustikSignalgeber` | Löst Signalton aus. | **Input:** `anzahl: int`. |
| **`leseTemperatur()`** | `PIDRegler` | `TemperatureSensor` | Liest Hardware-Temperatur. | **Output:** `float`. |
| **`calculateHeatingPower()`** | `WaffelController` | `PIDRegler` | Berechnet Stellgröße. | **Input:** `ist: float`. **Output:** `float`. |