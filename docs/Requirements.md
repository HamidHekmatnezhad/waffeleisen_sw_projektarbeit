# Requirements: Bräunungsgradsteuerung für Waffeleisen

### 1. Funktionale Requirements

|Nr.||Bedeutung|Title|Beschreibung|
|---|---|---|---|---|
|1.1||**MUSS**|Bräunungsgrad Einstellung|Der Benutzer **muss** den Bräunungsgrad über seperate Tasten ('+' und '-' ) in fünf Stufen (1-5) einstellen können.|
|1.2||**SOLL**|Anzeige des aktuellen Bräunungsgrades|Die aktuell gewählte Stufe (z.B. '3') **soll** auf dem Display angezeigt werden.|
|2.1||**SOLL**|Protokollierung der Messwerte|Die Messwerte **sollen** für mindenstens 60 Sekunden in einem Ringpuffer protokolliert werden.|
|2.2||**MUSS**|Temperaturmessung|Die Temperatur **muss** alle 100ms über den Sensor eingelesen werden.|
|3.1||**MUSS**|Temperaturregelung|Der Regelungsalgorithmus **muss** die Zieltemperatur mit einer maximalen Abweichung von 3&deg;C aufrechterhalten.|
|4.1||**MUSS**|Sicherheitsfehleranzeige| Bei einem Sicherheitsfehler **muss** das Display blinkend "FEHLER" anzeigen.|
|5.1||**MUSS**|Akustisches Signal bei Bräunungsgrad| Das akustische Signal **muss** nach Erreichen des Bräunungsgrades 3 Mal.|
|5.2||**SOLL**|Protokollierung Abschaltung|Das System soll den Zeitpunkt und die Temperatur der automatischen Abschaltung protokollieren.|

### 2. Nicht-Funktionale Requirements

|Nr.||prioritet|Title|Beschreibung|
|---|---|---|---|---|
|1.3||**SOLL**|Reaktionszeit der Bräunungsgrad Auswahl|Die Dauer für die Auswahl des maximalen Bräunungsgrades **sollte** 2 Sekunden nicht überschreiten.|
|1.4||**SOLL**|Konfigurierbare Stufenanzeige Texte|Die Texte der Stufenanzeige **sollen** über eine Konfigurationsdatei änderbar sein.|
|2.3||**MUSS**|Sensorfunktion bei Umgebungstemperatur|Der Temperatursensor **muss** bei Umgebungstemperaturen bis 40&deg;C funktionsfähig bleiben.|
|3.2||**SOLL**|Energieverbrauch bei Temperaturhaltung|Nach Erreichen der Zieltemperatur **soll** der Stromverbrauch zur Haltung der Temperatur unter 100W liegen.|
|3.3||**MUSS**|Testbarkeit des Regelungsalgorithmus|Der Regelungsalgorithmus **muss** isoliert mittels simulierter Temperatursignale testbar sein.|
|4.2||**MUSS**|Mehrsprachigkeit der Zustandstexte|Alle Zustandstexte **müssen** in einem externen Glossar für die Mehrsprachigkeit gespeichert sein.|
|5.3||**SOLL**|Verfügbarkeit der Abschaltfunktion|Die Abschaltfunktion **sollte** eine Verfügbarkeit von 99.999% aufweisen.|

