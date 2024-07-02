class Schueler:
    def __init__(self, name: str, 
                 mathenote = 0, 
                 deutschnote = 0, 
                 physiknote = 0, 
                 biologienote = 0, 
                 englischnote = 0):
        self.Name = name
        self.Noten = {"Deutsch": deutschnote, 
                      "Mathe": mathenote, 
                      "Physik": physiknote, 
                      "Biologie": biologienote, 
                      "Englisch": englischnote}
    def Note_erfahren(self, fach: str) -> float:
        return self.Noten.get(fach)
    def Note_aendern(self, fach: str, wert: float):
        if self.Noten.get(fach) is not None:
            self.Noten[fach] = wert

class Klasse:
    def __init__(self, klasse: str, schueler: list = list()):
        self.ID = klasse
        self.Schueler: list[Schueler] = schueler
    def Hinzufuegen(self, schueler: Schueler):
        self.Schueler.append(schueler)
    def Entfernen(self, name: str) -> Schueler:
        for schueler in self.Schueler:
            if schueler.Name == name:
                temp = schueler
                self.Schueler.remove(schueler)
                return temp
    def Noten(self, name: str) -> dict:
        for schueler in self.Schueler:
            if schueler.Name == name: 
                return schueler.Noten
    def Note_erfahren(self, name: str, fach: str):
        for schueler in self.Schueler:
            if schueler.Name == name: 
                return schueler.Note_erfahren(fach)
    def Note_aendern(self, name: str, fach: str, wert: float):
        for schueler in self.Schueler:
            if schueler.Name == name:
                schueler.Note_aendern(fach, wert)
                return
