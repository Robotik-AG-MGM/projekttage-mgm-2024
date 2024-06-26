class Position:
    def __init__(self, x_value: int, y_value: int, z_value: int):
        self.X = x_value
        self.Y = y_value
        self.Z = z_value
    def __add__(self, value):
        return Position(self.X + value.X, self.Y + value.Y, self.Z + value.Z)
    def __eq__(self, value) -> bool:
        if self.X == value.X and self.Y == value.Y and self.Z == value.Z: return True
        else: return False

class Kreatur:
    def __init__(self, position: Position) -> None:
        self.Position = position
    def Bewegen(self, neue_position: Position):
        self.Position = neue_position

class Schaf(Kreatur):
    def __init__(self, position: Position, farbe: str, geschoren = False)
        self.Farbe = farbe
        self.Geschoren = geschoren
        super().__init__(position)
    def scheeren(self):
        self.geschoren = False
    def faerben(self, farbe: str):
        self.Farbe = farbe
    def Warscheinlichkeit(self, item: str) -> float:
        return self.Ausbeute.get(item)
    
blue = Schaf(Position(0, 0, 0), "blau")