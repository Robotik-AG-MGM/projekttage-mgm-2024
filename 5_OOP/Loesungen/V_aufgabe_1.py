class Schaf:
    def __init__(self, x_position, y_position, z_position, farbe, geschoren):
        self.X = x_position
        self.Y = y_position
        self.Z = z_position
        self.Farbe = farbe
        self.Geschoren = geschoren
    def scheeren(self):
        self.geschoren = False
    def faerben(self, farbe):
        self.Farbe = farbe
