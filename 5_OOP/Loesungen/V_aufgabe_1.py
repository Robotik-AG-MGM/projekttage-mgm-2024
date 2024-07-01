class Mensch:
    def __init__(self, name: str, alter: int, groesse: float, gewicht_in_kg: int, geschlecht: str):
        self.Name = name
        self.Alter = alter
        self.Groesse = groesse
        self.Gewicht = gewicht_in_kg
        self.Geschlecht = geschlecht
    def BMI(self) -> float:
        return self.Gewicht / (self.Groesse ** 2)
    
Lux = Mensch("Luca", 17, 1.82, 75, "männlich", "braun")
print(f"{Lux.Name}'s Alter:        {Lux.Alter}")
print(f"{Lux.Name}'s Größe:        {Lux.Groesse}")
print(f"{Lux.Name}'s Gewicht:      {Lux.Gewicht}")
print(f"{Lux.Name}'s Geschlecht:   {Lux.Geschlecht}")
print(f"{Lux.Name}'s BMI:          {Lux.BMI()}")