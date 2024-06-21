# Python - OOP
## Objekte- Attribute und Methoden
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
    def mit_rueckgabe(self):
        return self.name

max_mustermann = Adresse("Max Mustermann", 12, "Beispielallee", "Musterhausingen", 89989)
max_mustermann.eineMethode()
print(max_mustermann.mit_rueckgabe())
```