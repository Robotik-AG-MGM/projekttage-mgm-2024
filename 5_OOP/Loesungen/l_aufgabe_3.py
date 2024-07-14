class Position:
    def __init__(self, x_value: int, y_value: int, z_value: int):
        self.X = x_value
        self.Y = y_value
        self.Z = z_value

    def __add__(self, value: "Position"):
        return Position(self.X + value.X, self.Y + value.Y, self.Z + value.Z)

    def __eq__(self, value: "Position") -> bool:
        if self.X == value.X and self.Y == value.Y and self.Z == value.Z:
            return True
        return False


class Kreatur:
    def __init__(self, position: Position) -> None:
        self.Position = position

    def Bewegen(self, neue_position: Position):
        self.Position = neue_position


class Schaf(Kreatur):
    def __init__(self,
                 position: Position,
                 farbe: str,
                 geschoren: bool = False):
        self.Farbe = farbe
        self.Geschoren = geschoren
        super().__init__(position)

    def Scheeren(self):
        self.Geschoren = True

    def Faerben(self, farbe: str):
        self.Farbe = farbe


class Kuh(Kreatur):
    def __init__(self, position: Position, gemolken: bool = False):
        self.Gemolken = gemolken
        super().__init__(position)

    def Melken(self):
        self.Gemolken = True


if __name__ == "__main__":
    my_cow = Kuh(Position(0, 0, 0))
    print(
        f"\nPosition X: {my_cow.Position.X}, Y: {
            my_cow.Position.Y}, Z: {my_cow.Position.Z}"
    )
    my_cow.Bewegen(Position(5, 0, -5))

    my_sheep = Schaf(Position(0, 0, 0), "gruen")
    print(
        f"Position X: {my_sheep.Position.X}, Y: {
            my_sheep.Position.Y}, Z: {my_sheep.Position.Z}"
    )
    print(f"Farbe: {my_sheep.Farbe}")
    print(f"Geschoren: {my_sheep.Geschoren}")
    my_sheep.Bewegen(Position(5, 0, -5))
    my_sheep.Faerben("dunkelgruen")
    my_sheep.Scheeren()
    print(
        f"Position X: {my_sheep.Position.X}, Y: {
            my_sheep.Position.Y}, Z: {my_sheep.Position.Z}"
    )
    print(f"Farbe: {my_sheep.Farbe}")
    print(f"Geschoren: {my_sheep.Geschoren}")

    print(
        f"\nKuh und Schaf an der selben Position? {
            my_cow.Position == my_sheep.Position}"
    )
