class Kreatur:
    def __init__(self, position: list, hitbox_size: tuple, blickrichtung: int):
        self.Position = position
        self.Hitbox_size = hitbox_size
        self.Blickrichtung = blickrichtung

    def umschauen(self, neue_blickrichtung: int) -> int:
        temp = self.Blickrichtung
        self.Blickrichtung = neue_blickrichtung
        return temp


my_kreatur = Kreatur([4, 7, -1], (1.2, 4, 1.2), 0)
print(my_kreatur.Blickrichtung)
print(my_kreatur.umschauen(40))
print(my_kreatur.Blickrichtung)
