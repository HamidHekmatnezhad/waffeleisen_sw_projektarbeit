## Dokumentation des Design Patterns (Singleton)

### 1. Wahl des Entwurfsmusters

Ich habe mich für das **Singleton Entwurfsmuster** entschieden. Das ist ein Erzeugungsmuster (Creation Pattern).

Der Grundgedanke ist: Ich muss sicherstellen, dass die Klasse, die ich als Singleton designe, **nur ein einziges Objekt** im gesamten System erzeugt. Alle anderen Codeteile sollen denselben zentralen Zugriffspunkt nutzen.

### 2. Anwendung im Waffeleisen-Projekt

Ich nutze das Singleton-Muster für meine Klasse **`TemperatureSensor`**.

Mein Waffeleisen hat physikalisch nur einen Temperatursensor. Es wäre falsch, wenn ich im Code aus Versehen an verschiedenen Stellen neue Sensorobjekte erstellen würde. Das Singleton löst dieses Problem, weil es garantiert, dass immer mit demselben, korrekten Objekt gearbeitet wird.

### 3. Technische Umsetzung (Das Konzept)

Um zu verhindern, dass jemand versehentlich eine neue Instanz erstellt, mache ich zwei Dinge:

1. Der **Konstruktor** der Klasse (`-TemperatureSensor()`) wird **privat** gemacht. Das ist wie eine verschlossene Tür, die verhindert, dass andere Klassen das Objekt direkt erstellen.
2. Ich füge eine **öffentliche, statische Methode** (`+getInstance()`) hinzu. Dies ist der **einzige Zugang** zu der Instanz.

Wenn der Code die Methode **`getInstance()`** aufruft:

* Beim **ersten Aufruf** wird das Objekt intern erstellt und gespeichert.
* Bei **allen weiteren Aufrufen** wird einfach das bereits existierende Objekt zurückgegeben.

So wird das Singleton realisiert und ich vermeide Fehler mit mehreren Sensor-Instanzen.