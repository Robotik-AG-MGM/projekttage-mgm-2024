class Haus:
    def __init__(self, besitzer: str, baujahr: str, flaeche: int) -> None:
        self.Besitzer = besitzer
        self.Baujahr = baujahr
        self.Flaeche = flaeche

    def Wert_berechnen(self) -> float:
        return 3342 * float(self.Flaeche)

    # 3342 Euro/Quadratmeter ist in Müllheim etwa der Wohnungspreis
    # Hier Frage, wie man berechnen kann (Muss nicht den Vorgaben entsprechen)
    def __private_Methode(self):
        print("Wurde aufgerufen")

    def Zugriff_auf_private_Methode(self):
        self.__private_Methode()

    def __eq__(
        self, other: "Haus"
    ) -> bool:  # Auch zeigen, dass nicht alles übereinstimmen muss
        res = True
        if self.Besitzer != other.Besitzer:
            res = False
        if self.Baujahr != other.Baujahr:
            res = False
        if self.Flaeche != other.Flaeche:
            res = False
        return res


class Mietwohnung(Haus):
    def __init__(
        self,
        besitzer: str,
        baujahr: str,
        flaeche: int,
        zimmer: int,
        stockwerk: int = 0
    ):
        # Default-Parameter
        self.Mietpreis = self.Miete_berechnen()
        self.Zimmer = zimmer
        self.Stockwerk = stockwerk
        super().__init__(
            besitzer, baujahr, flaeche
        )  # Achtung: nicht autokreieren lassen!!

    def Miete_berechnen(self):
        return 2**2  # Dürfen SUS aussuchen

    def Wert_berechnen(self) -> float:
        return self.Mietpreis  # Dürfen SUS aussuchen

    def Schaden_reklamieren(self, beschreibung: str):
        print(f"{self.Besitzer} reklamiert folgenden Schaden: {beschreibung}")


if __name__ == "__main__":
    Anna = Haus("Anna Becker", "2001", 60)  # dürfen SUS ausdenken
    Anna.Flaeche = 70  # dürfen SUS ausdenken
    print(Anna.Flaeche)
    print(Anna.Wert_berechnen())
    Anna.__private_Methode()  # pylint: disable=protected-access
    # liefert Error, ist absicht, wird im Live-Coding entfernt
    Anna.Zugriff_auf_private_Methode()

    Peter = Haus("Peter Mustermann", "2001", 40)  # dürfen SUS ausdenken
    Anna2 = Haus("Anna Becker", "2001", 60)  # dürfen SUS ausdenken
    print(Anna == Anna2)
    print(Anna == Peter)

    Klaus = Mietwohnung("Klaus", "1998", 70, 3)  # dürfen SUS ausdenken
    Klaus1 = Haus("Klaus", "1998", 70)  # dürfen SUS ausdenken
    print(Klaus.Besitzer)  # demonstration dass erben
    print(Klaus.Wert_berechnen())
    print(Klaus1.Wert_berechnen())
    # dürfen SUS ausdenken
    Klaus.Schaden_reklamieren("Badezimmertür geht nicht")
