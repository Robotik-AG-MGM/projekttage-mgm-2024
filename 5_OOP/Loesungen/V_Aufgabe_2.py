class Schueler:
    def __init__(self, name: str,
                 mathenote=0,
                 deutschnote=0,
                 physiknote=0,
                 biologienote=0,
                 englischnote=0):
        self.Name = name
        self.Noten = {"Deutsch": deutschnote,
                      "Mathe": mathenote,
                      "Physik": physiknote,
                      "Biologie": biologienote,
                      "Englisch": englischnote}

    def Note_erfahren(self, fach: str) -> float:
        # .get ist equvalent zu [fach],
        # nur das es None zurückgibt wenn der Key nicht existiert
        return self.Noten[fach]

    def Note_aendern(self, fach: str, wert: float):
        if fach in self.Noten:
            self.Noten[fach] = wert
        else:
            # warum testest du ob das fach vorhanden ist?
            pass


class Klasse:
    def __init__(self, klasse: str, schueler: list = []):
        self.ID = klasse
        # typehints sind nicht verbindlich ind erzugen kein zwang
        # oder abgeändertes Verhalten
        self.Schueler = schueler if type(schueler) is list else [schueler]

    def Hinzufuegen(self, schueler: Schueler):
        self.Schueler.append(schueler)

    def Entfernen(self, name: str) -> Schueler:
        for schueler in self.Schueler:
            if schueler.Name == name:
                self.Schueler.remove(schueler)
                return schueler
        return None

    def Note_erfahren(self, name: str, fach: str) -> float:
        for schueler in self.Schueler:
            if schueler.Name == name:
                return schueler.Note_erfahren(fach)
        return None

    def Note_aendern(self, name: str, fach: str, wert: float):
        for schueler in self.Schueler:
            if schueler.Name == name:
                schueler.Note_aendern(fach, wert)
                return
