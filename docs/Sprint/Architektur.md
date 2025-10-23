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
