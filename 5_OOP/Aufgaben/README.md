# Aufgaben Kapitel 5: OOP
**Bevor du anfängst:** Erstelle im Ordner `5_OOP` einen Ordner names `Loesungen` dort erstellst du für jeden Aufgabenblock (sobald du anfängst die Aufgaben aus diesem Block zu bearbeiten) eine Python-Datei (Endung : `.py`). Die Namesgebung muss dabei diesem Schema folgen: `V_aufgabe_[Nr]`, Wobei `[Nr]` für die Nummer des Aufgabenblockes steht die du bearbeitest. Also `1` für Aufgabenblock 1 usw. Dies ist wichtig, damit deine Lösungen vom Computer kontrolliert werden können.

**Hinweis:** Alle Aufgabe eines Aufgabenblockes können in einem Dokument gelöst werden. Achte auf die richtige Schreibweise der Attribute und Methoden, da sich das Programm, das deine Lösungen kontrolliert sonst beschwert. Wenn du mal nicht weiterweißt, dann findest du ausführliche Erklärungen in dem Dokument README.md im Ordner 5_OOP
## Aufgabenblock 1: Dein erstes Objekt
**Ziel:** In diesem Aufgabenblock wirst du ein Objekt mit der Bezeichnung `Mensch` erstellen. Dieses Objekt soll lediglich ein paar einfache Informationen über Menschen speichern
### Aufgabe a: Der Kreator
Schreibe den Kreator für das Objekt `Mensch`. Dieser soll einen Namen als String, ein Alter als Integer, eine Körpergröße als Float, ein Gewicht in kg als Integer und ein Geschlecht als String als Parameter nehmen. Gib im Kreator die Typen für die Parameter an.
### Aufgabe b: Die Attribute
Fülle nun den Körper des Kreators von `Mensch` mit der Definition der Attribute. Das `Mensch`-Objekt soll folgende Attribuet haben:
* `Name`, hier wird der Name des Menschen, den wir erstellen gespeichert.
* `Alter`, hier wird das Alter gespeihert.
* `Groesse`, dieses Attribut speichert die Körpergröße.
* `Gewicht` dient dem Speichern des Gewichtes.
### Aufgabe c: BMI berechnen
Zu guter Letzt möchten wir das Objekt um eine Methode ergänzen, die den Body Mass Index (kurz BMI) der Person ausrechnet. Der BMI wird berechnet indem man das Gewicht (in kg) durch das Quadrat der Körpergröße (in m) teilt. Schreibe eine Methode, die den BMI ausrechnet und zurückgibt.
## Aufgabenblock 2: Schüler und Klassen als Objekte
**Ziel:** Die Objekte, die in diesem Block erstellt werden sollen Schüler und Klassen repräsentieren. Das Schüler-Objekt erhält für diese Zwecke eine Dictonary mit den Noten des Schülers und Methoden, um die Noten zu ändern.
### Aufgabe a: Die Attribute des Schüler-Objektes
Wir beginnen unsere Arbeit mit dem Schüler-Objekt. Denk daran, dass du das `ü` im Code mit `ue` ersetzt. Nun aber zu den Attributen:
* `Name`: Einen Namen, um den Namen des Schülers zu speichern
* `Noten`: Eine Dictonary in der für die Fächer `Deutsch`, `Mathe`, `Physik`, `Biologie` und `Englisch` die Noten als `float` gespeichert sind.

Schreibe einen entsprechenden Kreator, der Name und Noten des Schülers als Parameter nimmt. Schreibe für jede Note einen einzelnen Paramter. Denk daran, im Kreator die Typen für die Parameter anzugeben.
### Aufgabe b: Default-parameter im Kreator
Damit wir beim Erstellen der Schüler nicht jedesmal für jede Note einen Wert angeben müssen, wäre es doch sinvoll die Noten-Parameter des Kreators mit Default-Parametern zu besetzen. Genau das ist jetzt deine Aufgabe: Besetzte alle Noten-Parameter des Kreator mit dem Default-Parameter `0`. In unserem Fall heißt `0`, dass die Note nicht oder noch nicht eingetragen wurde (Und nicht, dass sie übermäßig gut ist).
### Aufgabe c: Methoden des Schüler-Objektes
Setze folgende Methode für das Schüler-Objekt um
* `Note_erfahren`: Diese Methode nimmt ein Fach und gibt die Note des Schülers in diesem Fach zurück
* `Note_aendern`: Diese Methode nimmt ein Fach und einen Wert. Sie setzt die Note des Schülers in diesem Fach auf den Wert.
### Aufgabe d: Das Klassen-Objekt
Erstelle nun ein neues Objekt names `Klasse`, dass eine Liste aus Schülern (`Schueler`) und einen Klassen-`ID` als Attribute hat. (Klassen-ID soll speichern, dass es sich z.B. um die 9e handelt). Der Kreator soll dabei eine Klassen-ID und eine Liste mit Schülern, die mit dem Default-Wert für eine leere Liste belegt ist, als Parameter nehmen. 
### Aufgabe e: Attribute genauer definieren:
Sorge dafür, dass der Computer weiß, dass es sich bei `Schueler` um eine Liste mit Schülern handelt. Dies gelingt dir, indem du hinter `self.Schueler` folgendes schreibst: `: list[Schueler]`. Dadurch legst du fest, dass Schueler eine Liste aus Schülern ist.
### Aufgabe f: Methoden des Klassen-Objekts:
Ergänze dein Objekt um folgende Methoden:
* `Hinzufuegen`. Diese Methode nimmt einen Schüler als Parameter und fügt diesen der Klasse hinzu
* `Entfernen`. Diese Methode nimmt einen Namen als Parameter und entfernt den Schüler mit dem angegebenen Name aus der Liste der Schüler. Außerdem soll die Methode den Schüler, der entfernt wurde zurückgeben. **Tipp:** Du kannst den Schüler zwischenspeichern bevor du ihn aus der Liste löschst und den zwischengespeicherten Wert zurückgeben.
* `Noten`. Diese Methode nimmt ebenfalls einen Namen als Parameter und gibt die Dictonary mit den Noten des angegebenen Schülers zurück.
* `Note_erfahren`. Diese Methode nimmt erneut einen Namen als Parameter, nimmt jedoch zusätzlich ein Faach und gibt die Note in dem Fach zurück. **Tipp:** Du kannst die Methoden, die du für das Schüler-Objekt geschrieben hast hier verwenden.
* `Note_aendern`. Diese Methode nimmt erneut einen Name ind ein Fach, jedoch auch eine Note (einen float) als Parameter. Sie ändert die Note des angegebenen Schülers auf den angegebenen Wert. **Tipp:** Du kannst die Methoden, die du für das Schüler-Objekt geschrieben hast hier verwenden.
## Aufgabenblock 3: Erstelle ein Schaf- und Kuh-Objekt
**Ziel:** Die Objekte, die du erstellst sollen ein Schaf und eine Kuh in einem Open World Game repräsentieren. Dazu erhalten das Schaf und die Kuh eine Position im Raum, und einige Methoden, die die Interaktion mit dem Objekt erleichtern. Außerdem wird es ein Objekt geben, dass die Arbeit mit Kuh und Schaf vereinfacht
### Aufgabe a: Das Objekt Position
Da sowohl die Kuh als auch das Schaf eine Position im Raum erhalten werden, macht es Sinn ein Objekt zu schreiben, dass eine Position im dreidimensionalem Raum repräsentiert. Das Objekt soll `Position` heißen und die Atribute `X`, `Y` und `Z` haben.
### Aufgabe b: Operatorüberladung
Überlade für das Objekt `Position` den Aditionsoperatur (+) und den Vergleichoperator (==). Hilfe findest du im Dokument README.md im Ordner 5_OOP.
### Aufgabe c: Das Objekt Kreatur
Da Schaf und Kuh beides Kreaturen sind und deshalb gewisse Gemeinsamkeiten haben (z.B. haben beide eine Position), werden wir Sie beide von dem Objekt `Kreatur` erben lassen. Wenn du nicht weißt, was erben ist, dann lies im Dokument README.md im Ordner 5_OOP nach.
Das Objekt `Kreatur` soll ein Attribut, nämlich die `Position` haben und eine Methode names `Bewegen`, die die Position der Kreatur auf die mitgegebene Position ändert. Schreibe das `Kreatur`-Objekt
### Aufgabe d: Attribute des Schaf- und Kuh-Objektes
Nun schreibst du die Schaf- und Kuh-Objekte. Stelle sicher, dass sie von `Kreatur` erben. Dies erreichst du folgendermaßen: `class Schaf(Kreatur):` sobald das getan ist kannst du die entsprechenden Kreatoren schreiben. Hier ist es besonders wichtig, dass du die Eigenschaften des Objektes `Kreatur` auch tatsächlich erbst. Dies gelingt mit dem Aufruf des Kreator von `Kreatur` im Kreator von `Schaf` bzw. `Kuh` auf diese Art: `super().__init__(parameter1, parameter2)`. Da der Kreator von `Kreatur` nur eine Position nimmt, musst du ihm nur eine Position übergeben.
Dein Kuh Objekt soll keine zusätzlichen Attribut ehaben.

In deinem Schaf-Objekt soll es folgende zusätzliche Attribute geben:
* Einen `bool` mit der Bezeichnung `Geschoren`, der speichert, ob das Schaf geschoren ist.
* Ein Attribut vom typ `str` mit der Bezeichnung `Farbe`, das die Farbe deines Schafes speichert.
Belege im Kreator des Schaf-Objektes das Attribut `Geschoren` mit dem Default-Parameter `False`
### Aufgabe e: Methoden
Das Kuh-Objekt bekommt keine zusätzlichen Methoden.
Dein Schaf-Objekt soll folgende zusätzliche Methoden haben:
* Eine Methode mit dem Name `Scheeren`, die das Schaf scheert
* Eine zweite Methode mit dem Name `Faerben`, um die Farbe des Schafes zu verändern
### Aufgabe f: Schafe und Kühe
Erstelle ein Kuh-Objekt und gib dessen Position aus. Rufe die Methode `Bewegen` auf und gib erneut die Position aus. 
Erstelle nun ein Schaf-Objekt in deiner Lieblingsfarbe. Die Position kannst du dir ebenfalls aussuchen, lasse das Schaf aber ungeschoren. Gib nun die Farbe, Position und den Geschoren-Zustand des Schafes aus. Rufe anschließend die Methoden `Faerben` und `Scheeren`, sowie `Bewegen` auf und gib erneut Farbe, Position und den Geschoren-Zustand aus.
Gib zuletzt das Ergebnis des Vergleichs der Positioinen deiner Kuh und deines Schafes aus.