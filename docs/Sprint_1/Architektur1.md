# Architektur

## Komponentendiagramm

```markdown
+------------------------------------------------------+
|                 Benutzeroberfläche                   |
|  +-----------------------------------------------+   |
|  | DisplayController | SoundController           |   |
|  +-----------------------------------------------+   |
+------------------------------------------------------+
                            |
                            ▼
+------------------------------------------------------+
|                 Anwendungsschicht                    |
|  +-----------------------------------------------+   |
|  | BrowningController | StateManager | ConfigMgr |   |
|  +-----------------------------------------------+   |
+------------------------------------------------------+
                            |
                            ▼
+------------------------------------------------------+
|              Steuerungs-/Regelungsschicht            |
|  +-----------------------------------------------+   |
|  | TemperatureController | HeaterController      |   |
|  | SafetyController       | Regulator (PID)      |   |
|  +-----------------------------------------------+   |
+------------------------------------------------------+
                            |
                            ▼
+------------------------------------------------------+
|           Hardware-Abstraktionsschicht               |
|  +-------------------------------------------------+ |
|  | TempSensorDriver | HeaterDriver | DisplayDriver | |
|  | LEDDriver | BuzzerDriver | ButtonDriver         | |
|  +-------------------------------------------------+ |
+------------------------------------------------------+
```



|**Komponente**|**Zugehörige Requirements**|
|--------------|---------------------------|
|**Benutzeroberfläche (userInterface)**|Req. 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7 |
|**Anwendungsschicht (controlLogic)**|Req. 1.1, 1.2, 1.3, 3.1|
|**Regelungsschicht (controlLogic intern)**|Req. 3.1, 3.2|
|**Hardware-Abstraktion (hardwareAbstraction)**|Req. 3.2, 3.3|

### Verantwortlichkeiten der Komponenten:
|**Komponente**|**Rolle**|**Verantwortlichkeiten**|
|--------------|---------|------------------------|
|**Benutzeroberfläche**|Präsentationsschicht|Anzeige des Betriebszustands (Aufheizen, Backen, Fertig), Eingabe über Tasten, akustische Signale, LED-/Displaysteuerung|
|**Anwendungsschicht**|Steuerungs- und Logikschicht|Verwaltung des Bräunungsgrads, Steuerung der Temperaturziele, Ablaufkontrolle des Backvorgangs|
|**Regelungsschicht**|Regelungslogik| Umsetzung der Temperaturregelung (PID-Regler), Ansteuerung der Heizelemente|
|**Hardware-Abstraktion**|Hardware-Interface|Verbindung zwischen Software und Sensorik/Aktorik (Temperaturfühler, Heizspirale, Display, LEDs, Tasten, Buzzer)|


## Schnittstellen 

| Interface (Methode) | Sender (Absender) | Empfänger (Empfänger) | **Syntax (Kommunikationsart)** | **Semantik (Werte, Einheiten & Bereiche)** |
| :--- | :--- | :--- | :--- | :--- |
| **`leseTemperatur()`** | `PIDRegler` | `TemperatureSensor` | **Synchroner Funktionsaufruf** (In-Process) | **Output:** `float` (Aktuelle Temperatur in **°C**). |
| **`calculateHeatingPower()`** | `WaffelController` | `PIDRegler` | **Synchroner Funktionsaufruf** (Regelberechnung) | **Input:** `istTemp: float` (Aktuelle Temperatur in **°C**). **Output:** `float` (Stellgröße, Bereich **0.0 - 1.0**). |
| **`setzeSolltemperatur()`** | `WaffelController` | `PIDRegler` | Synchroner Funktionsaufruf | **Input:** `temp: int` (Zieltemperatur in **°C**). |
| **`setzeLeistung()`** | `PIDRegler` | `HeaterActuator` | Synchroner Funktionsaufruf (Hardware-Ansteuerung) | **Input:** `leistung: float` (Leistungsvorgabe im Bereich **$0.0$ bis $1.0$**). |
| **`verarbeiteEingabe()`** | `ButtonInput` | `WaffelController` | **Asynchroner Event** (Callback/Interrupt) | **Input:** `grad: int` (Der vom Benutzer gewählte Bräunungsgrad, Bereich **$1$ bis $5$**). |