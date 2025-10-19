# **Pflichtenheft: Bräunungsgradsteuerung für Waffeleisen**

### 1. **Einstellbarer Bräunungsgrad**
- Der Benutzer kann den gewünschten Bräunungsgrad über die „+“- und „–“-Tasten einstellen.  
- Es stehen fünf Stufen (1–5) zur Auswahl.  
- Die Auswahl reagiert verzögerungsfrei, spätestens innerhalb von 2 Sekunden.  

### 2. **Anzeige des Bräunungsgrades**
- Der aktuell gewählte Bräunungsgrad wird gut sichtbar auf dem Display angezeigt (z. B. Zahl oder Text).  
- Die Texte der Anzeige sind über eine Konfigurationsdatei anpassbar.  
- Alle Texte müssen in einem externen Glossar gespeichert werden, um Mehrsprachigkeit zu ermöglichen.  

### 3. **Temperaturmessung und Protokollierung**
- Der Temperatursensor misst die Temperatur alle 100 ms.  
- Die Messwerte werden für mindestens 60 Sekunden in einem Ringpuffer gespeichert.  
- Der Sensor muss auch bei Umgebungstemperaturen bis 40 °C zuverlässig funktionieren.  

### 4. **Temperaturregelung**
- Die Regelung hält die Zieltemperatur mit einer maximalen Abweichung von ±3 °C.  
- Der Algorithmus ist testbar durch simulierte Temperatursignale.  
- Nach Erreichen der Zieltemperatur soll der Energieverbrauch unter 100 W bleiben.  

### 5. **Sicherheitsfunktionen**
- Bei einem Sicherheitsfehler zeigt das Display blinkend „FEHLER“ an.  
- Das System protokolliert Zeitpunkt und Temperatur bei einer automatischen Abschaltung.  
- Die Abschaltfunktion soll eine Verfügbarkeit von 99,999 % besitzen.  

### 6. **Akustische Signale**
- Nach Erreichen des gewünschten Bräunungsgrades ertönt ein akustisches Signal (dreimal kurz).  
- Das Signal informiert den Benutzer, dass die Waffeln fertig sind.  

### 7. **Komfort und Benutzerfreundlichkeit**
- Alle Anzeigen und Signale sind klar, einfach und verständlich.  
- Die Steuerung darf den Bedienvorgang nicht unnötig verkomplizieren.  
- Einstellungen bleiben auch nach einer kurzen Trennung vom Strom erhalten.  
