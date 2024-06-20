## Aufgabe 1: Erstelle ein Objekt, das ein Schaf in Minecraft represäntieren könnte
### Grundkonzept
* In Python kann man sogenannte Objekte programmieren und Instanzen  dieser Objekte erstellen.
* Objekte dienen der einfacheren und gesammelten Verarbeitung von Datengruppen wie z.B. der Adresse einer Person
* Objekte bestehen aus Attributen und Methoden
* Attribute speichern jeweils einen Wert. Es kann sich um Zahlenwerte, Text, oder Listen, Tupel und Dictonarys handeln. Auch Instanzen anderer Objekte können Attribute sein.
*  Methoden operieren auf Instanzen eines Objektes. Sie funktionieren wie Funktionen, werden jedoch mit der Instanz und dem Punktoperator aufgerufen
### Syntax
```python
class Adresse:
    def __init__(self, name, hausnummer, strasse, ort, postleitzahl):
        self.name = name
        self.hausnr = hausnummer
        self.strasse = strasse
        self.ort = ort
        self.plz = postleitzahl
    def eine_Methode(self):
        print(f"{self.name} wohnt in {self.ort} in der Straße {self.strasse} Hausnummer {self.hausnr}")
```
### Anforderungen an dein Schaf-Objekt
In deinem Schaf-Objekt soll es folgende Attribute geben:
* Eine Position im dreidimensionalem Raum, also mit x-, y- und z-Richtung
* Einen Bool, der speichert, ob das Schaf geschoren ist
* Ein Attribut, dass die Farbe deines Schafes speichert
## Aufgabe 2: Füge deinem Objekt Methoden hinzu
Füge deinem Objekt eine Methode hinzu, die das Schaf scheert, und eine die die Farbe des Schafes ändert