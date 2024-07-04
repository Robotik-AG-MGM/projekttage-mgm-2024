# Python - OOP
## Objekte- ein kleiner Überblick
### Grundkonzept
* In Python kann man sogenannte Objekte programmieren und Instanzen  dieser Objekte erstellen.
* Objekte dienen der einfacheren und gesammelten Verarbeitung von Datengruppen wie z.B. der Adresse einer Person
* Objekte bestehen aus Attributen und Methoden
* Attribute speichern jeweils einen Wert. Es kann sich um Zahlenwerte, Text, oder Listen, Tupel und Dictonarys handeln. Auch Instanzen anderer Objekte können Attribute sein.
*  Methoden operieren auf Instanzen eines Objektes. Sie funktionieren wie Funktionen, werden jedoch mit der Instanz und dem Punktoperator aufgerufen
### Syntax
```python
class Buch:
    def __init__(self, titel: str, untertitel: str, autor: str):
        self.Titel = titel
        self.Untertitel = untertitel
        self.Autor = autor
    def eine_Methode(self):
        print(f"Das Buch '{self.Titel} : {self.Untertitel}' wurde von {self.Autor} geschrieben.")
    def Methode_mit_Rueckgabe(self, autor: str) -> bool:
        if self.Autor == autor:
            print("Die Autoren sind identisch")
            return True
        else:
            print("Die Autoren sind nicht identisch")
            return False

Harry_Potter_1 = Buch("Harry Potter", "", "Joanne K. Rowling")
Harry_Potter_1.Untertitel = "Stein der Weisen"
Harry_Potter_1.eine_Methode()
print(Harry_Potter_1.Methode_mit_Rueckgabe("Joanne K. Rowling")) # Ausgabe: True
```
### Attribute
Attribute sind Variablen die innerhalb eines Objektes Werte speichern. Jede Instanz eines Objektes speichert für alle Attribute dieses Objektes einen Wert. Attribute werden in der Funktion `__init__()` auch Kreator genannt erstellt. Der Syntax dafür sieht so aus: `self.[Attribut] = Value`. Den Name des Attributes könnt ihr genauso wie den Wert selber festlegen. den Wert legt man meistens mithilfe von Parametern des Kreators fest, allerdings ist es auch möglich dem Attribut direkt einen festgelegten Wert zuzuweisen. z. B.: `self.Value = 4`. Liegt eine Instanz eines Objektes vor, so kann man auf die Attribute so zugreifen: `[Instanz].[Attribut]`. `[Instanz]` ersetzt ihr mit dem Name der Instanz und `[Attribut]` mit dem Namen des Attributes. So könnt ihr Werte innerhalb einer Instanz lesen, aber auch verändern.
### Methoden
Methoden funktionieren genauso wie Funktionen, mit dem einzigen Unterschied, dass sie immer `self` als Parameter nehmen. Das liegt daran, dass Methoden mit einer Instanz des Objektes aufgerufen werden, etwa so: `Instanz.Methode(Parameter)`. Damit man innerhalb der Methode zugriff auf die Instanz hat, mit der die Methode aufgerufen wurde muss man `self` bei der Definition mit als Parameter angeben, aber nicht beim Aufruf in den Klammern dazuschreiben.

**Typen in Funktionen/Methoden angeben:** Falls man beim Definieren einer Methode für die einzelnen Parameter angeben möchte, welchen Typ diese haben sollen, macht man das so: `def Funktion(parameter1: int, parameter2: str, parameter3: bool)`. parameter1 ist in diesem Beispiel ein Integer, parameter2 ein String und parameter3 ein Boolean. Dies wird häufig in der `__init__()`-Methode (genannt Kreator) eines Objektes gemacht, um klarzustellen, was für einen Datentyp man erwartet.

## Objekte - etwas ausführlicher
### Syntax
``` python
class Adresse:
    def __init__(self, name: str, hausnummer: int, strasse: str, ort= "Musterhausingen", postleitzahl = "09989"): # Default-Parameter
        self.name = name
        self.hausnr = hausnummer
        self.strasse = strasse
        self.ort = ort
        self.plz = postleitzahl
    def __eq__(self, other) -> bool:    # Operator-Überladung
        if self.hausnr == other.hausnr and 
            self.strasse == other.strasse and 
            self.ort == other.ort and 
            self.plz == other.plz: return True
        else: return False

max_mustermann = Adresse("Max Mustermann", 12, "Beispielallee", "Musterhausingen", "09989")
felix_mustermann = Adresse("Felix Mustermann", 12, "Beispielallee")     # Default-Parameter angewandt
if max_mustermann == felix_mustermann:      # Operator-Überladung angewandt
    print("Die Adressen von Max und Felix sind identisch") 
else: 
    print("Die Adressen von Max und Felix sind nicht identisch")
```
### Attribute
Eines über Attribute solltet ihr noch wissen: Möchte man einem Attribut einen Typ zuweisen, so kann man das folgendermaßen: `self.[Attribut]: int = value`. Das Attribut hat jetzt also den Typ int. ähnlich funktioniert es mit Listen, jedoch muss man manchmal festlegen, welchen Typ die Objekte in einer Liste haben, um entsprechende Methoden aufrufen zu können. Auf das Attribut `self.List = []`, in das sspäter Adressen kommen sollen wäre es z.B. nicht möglich self.List.Name aufzurufen, weil der Computer nicht weiiß, dass es eine Liste mit Adressen ist. Dies lässt sich ändern, indem man schreibt `self.List: list[Adresse] = []`. So weiß der Computer, dass es sich um eine Liste mit Adressen handelt.
### Methoden
**Default-Parameter:** Wenn man einer Funktion oder Methode sehr häufig denselben Wert als Parameter gibt, z.B. Wenn man nur Adressen aus demselben Ort sammelt, dann kann man den Parameter bei Funktions- bzw. Methodendefinition mit einem Default-Parameter belegen. Das sieht dann so aus:
`def Funktion(parameter1, parameter2 = False)`. Beim Aufruf der Funktion bzw. der Methode muss man für parameter2 nun keinen Wert mehr übergeben, kann es jedoch tun: beispeilsweise wäre dieser dieser Aufruf `Funktion(7)` gleichbedeutend mit diesem `Funktion(7, False)`

**besondere Methoden:**
Es gibt in python einige besondere Methoden, die bestimmte Zwecke erfüllen. Die `__init__()`-Methode gehört dazu.
Darüber hinaus ist mit diesen besonderen Methoden eine Überladung von Operatoren möglich. Was heißt das: Im Normalfall können Ausdrücke wie `Objekt1 + Objekt2` oder `Objekt1 == Objekt2` nicht ausgeführt werden. Man kann jedoch durch überladen dieser Operatoren erreichen, dass oben stehende Ausdrücke ausgeführt werden können. Dazu müsst ihr zunächt einmal wissen, dass `Integer1 + Integer2` gleichbedeutend ist mit `Integer1.__add__(Integer2)` oder `__add__(Integer1, Integer2)`. Operatoren sind also nichts anderes als Funktionen, die die jeweiligen Zahlen als Parameter nehmen. Schreibt man nun eine Funktion, die genauso heißt wie eine andere, jedoch andere Parameter nimmt, so überlädt man die Funktion. Genau das kann man mit den Operatoren machen, sodass diese auch das von euch geschriebene Objekt als Parameter nehmen. Beispiel:
```python
class Zahl:
    def __init__(self, zahl: int):
        self.Zahl = zahl
    def __add__(self, other: Zahl) -> Zahl:
        return Zahl(self.Zahl + other.Zahl)
```
Im folgenden findet sich eine Liste mit allen Operator-Funktionen
* `__eq__(self, other)`: Diese Methode überlädt den Operator `==`. Die Methode muss einen Boolean zurückgeben.
* `__ne__(self, other)`: Diese Methode überlädt den Operator `!=`. Die Methode muss einen Boolean zurückgeben.
* `__ge__(self, other)`: Diese Methode überlädt den Operator `>=`. Die Methode muss einen Boolean zurückgeben.
* `__gt__(self, other)`: Diese Methode überlädt den Operator `>`. Die Methode muss einen Boolean zurückgeben.
* `__le__(self, other)`: Diese Methode überlädt den Operator `<=`. Die Methode muss einen Boolean zurückgeben.
* `__lt__(self, other)`: Diese Methode überlädt den Operator `<`. Die Methode muss einen Boolean zurückgeben.
* `__add__(self, other)`: Diese Methode überlädt den Operator `+`
* `__mul__(self, other)`: Diese Methode überlädt den Operator `*`.
* `__sub__(self, other)`: Diese Methode überlädt den Operator `-`.
* `__truediv__(self, other)`: Diese Methode überlädt den Operator `/`.
### Erben
**Syntax:**
``` python
class Haustier:
    def __init__(self, besitzer: str, gewicht: int):
        self.Besitzer = besitzer
        self.Gewicht = gewicht
    def gewicht(self):
        print(self.Gewicht)
        return self.Gewicht

class Hamster(Haustier):
    def __init__(self, besitzer: str, gewicht: int, niedlich: bool, nachtaktiv: bool):
        self.Niedlich = niedlich
        self.Nachtaktiv = nachtaktiv
        super().__init__(besitzer, gewicht)
    def ist_niedlich(self) -> bool:
        return self.Niedlich

Putzi = Hamster("Max", 50, True, True)
print(Putzi.Besitzer)       # Ausgabe: Max
print(Putzi.Gewicht)        # Ausgabe: 50
Putzi.gewicht()             # Ausgabe: 50
print(Putzi.Niedlich)       # Ausgabe: True
print(Putzi.Nachtaktiv)     # Ausgabe: True
print(Putzi.ist_niedlich)   # Ausgabe: True
```
In Python kann man von anderen Objekten erben. Erben bedeutet, dass (alle) Attribute und Methoden des Objektes von dem man erbt auf das Objekt, das man erbt übergehen. Wenn man z.B. ein Objekt `Haustier` hat, dass die Attribute `Besitzer` und `Gewicht` hat. Schreibt man nun ein Objekt `Hamster` und lässt es von Haustier erben, dann haben alle Instanzen von Hamster automatisch die Attribute `Besitzer` und `Gewicht`, ohne dass du diese im Kreator angeben musst. Du kannst nun in `Hamster` weitere Attribute und Methoden definieren, und so das Objekt `Hamster` erweitern, ohne dass du etwas an `Haustier` änderst. Das ist bsonders dann sinvoll, wenn man viele Objekte erstellen will, die sich nur minimal unterscheiden, aber einige gemeinsame Attribute und/oder Methoden haben.

Im Code erbt man von einem anderen Objekt, indem man das Objekt, von dem man erbt in Klammern hinter dem Objektnnamen ergänzt. etwa so:
`class Objekt(erbt_von_Objekt)`. Ganz Wichtig ist anschließend, dass man im Kreator der Klasse die erbt den Kreator des Objektes von dem man erbt auf etwas besondere Weise aufruft. nämlich so: `super().__init__(parameter1, parameter2, ...)`. Damit sagt man dem Computer, dass man alle Attribute und Methoden vom ErbObjekt erben möchte. Nun hat jede Instanz des Objektes Zugriff auf die Attribute und Methoden von dem Objekt, von dem man erbt.