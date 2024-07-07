import os
import pytest
from aufgabe_1 import Mensch
from aufgabe_2 import Schueler, Klasse
from aufgabe_3 import Kreatur, Position, Schaf, Kuh

# fixtures
@pytest.fixture(scope="function")
def mensch():
    yield Mensch("Luca", 17, 1.82, 75, "männlich")

@pytest.fixture(scope="function")
def klasse():
    yield Klasse("10A")

@pytest.fixture(scope="function")
def schueler_a():
    yield Schueler("Max Mustermann")

@pytest.fixture(scope="function")
def schueler_b():
    yield Schueler("Erika Mustermann")


# Test ob die Dateien existieren
def test_aufgabe_1_exists():  # Funktionsfähigkeit durch Debug hergestellt.
    assert os.path.exists(
        "5_OOP/Loesungen/V_Aufgabe_1.py"
    ), "File does not exist"


def test_aufgabe_2_exists():  # Funktionsfähigkeit durch Debug hergestellt.
    assert os.path.exists(
        "5_OOP/Loesungen/V_Aufgabe_2.py"
    ), "File does not exist"


def test_aufgabe_3_exists():  # Funktionsfähigkeit durch Debug hergestellt.
    assert os.path.exists(
        "5_OOP/Loesungen/V_Aufgabe_3.py"
    ), "File does not exist"


# teste Aufgabe 1
def test_mensch_bmi(mensch):
    lux = mensch
    assert lux.BMI() == pytest.approx(22.6, abs=0.1)


def test_mensch_name_attribute(mensch):
    lux = mensch
    assert hasattr(lux, "Name"), "Name attribute does not exist"
    assert isinstance(lux.Name, str), "Name attribute is not of type str"


def test_mensch_alter_attribute(mensch):
    lux = mensch
    assert hasattr(lux, "Alter"), "Alter attribute does not exist"
    assert isinstance(lux.Alter, int), "Alter attribute is not of type int"


def test_mensch_groesse_attribute(mensch):
    lux = mensch
    assert hasattr(lux, "Groesse"), "Groesse attribute does not exist"
    assert isinstance(lux.Groesse, float), \
        "Groesse attribute is not of type float"


def test_mensch_gewicht_attribute(mensch):
    lux = mensch
    assert hasattr(lux, "Gewicht"), "Gewicht attribute does not exist"
    assert isinstance(lux.Gewicht, int), "Gewicht attribute is not of type int"


def test_mensch_geschlecht_attribute(mensch):
    lux = mensch
    assert hasattr(lux, "Geschlecht"), "Geschlecht attribute does not exist"
    assert isinstance(lux.Geschlecht, str), \
        "Geschlecht attribute is not of type str"


def test_mensch_bmi_function(mensch):
    lux = mensch
    assert hasattr(lux, "BMI"), "BMI function does not exist"
    assert callable(lux.BMI), "BMI is not a callable function"


def test_mensch_attributes(mensch):
    lux = mensch
    assert lux.Name == "Luca"
    assert lux.Alter == 17
    assert lux.Groesse == 1.82
    assert lux.Gewicht == 75
    assert lux.Geschlecht == "männlich"


# teste Aufgabe 2
def test_schueler_name_attribute(schueler_a):
    schueler = schueler_a
    assert hasattr(schueler, "Name"), "Name attribute does not exist"
    assert isinstance(schueler.Name, str), "Name attribute is not of type str"


def test_schueler_noten_attribute(schueler_a):
    schueler = schueler_a
    assert hasattr(schueler, "Noten"), "Noten attribute does not exist"
    assert isinstance(schueler.Noten, dict), \
        "Noten attribute is not of type dict"


def test_schueler_note_erfahren():
    schueler = Schueler("Max Mustermann",
                                    mathenote=4.5,
                                    deutschnote=3.7)
    assert schueler.Note_erfahren("Mathe") == 4.5
    assert schueler.Note_erfahren("Deutsch") == 3.7


def test_schueler_note_aendern(schueler_a):
    schueler = schueler_a
    schueler.Note_aendern("Mathe", 3.8)
    assert schueler.Note_erfahren("Mathe") == 3.8


def test_klasse_hinzufuegen(klasse, schueler_a):
    k = klasse
    schueler = schueler_a
    k.Hinzufuegen(schueler)
    assert len(k.Schueler) == 1
    assert k.Schueler[0] == schueler


def test_klasse_entfernen(klasse, schueler_a, schueler_b):
    k = klasse
    schueler1 = schueler_a
    schueler2 = schueler_b
    k.Hinzufuegen(schueler1)
    k.Hinzufuegen(schueler2)
    removed_schueler = k.Entfernen("Max Mustermann")
    assert removed_schueler == schueler1
    assert len(k.Schueler) == 1
    assert k.Schueler[0] == schueler2


def test_klasse_note_erfahren(klasse, schueler_a):
    k = klasse
    schueler = schueler_a
    schueler.Note_aendern("Mathe", 4.5)
    schueler.Note_aendern("Deutsch", 3.7)
    k.Hinzufuegen(schueler)
    assert k.Note_erfahren("Max Mustermann", "Mathe") == 4.5
    assert k.Note_erfahren("Max Mustermann", "Deutsch") == 3.7


def test_klasse_note_aendern(klasse, schueler_a):
    k = klasse
    schueler = schueler_a
    schueler.Note_aendern("Mathe", 4.5)
    k.Hinzufuegen(schueler)
    k.Note_aendern("Max Mustermann", "Mathe", 3.8)
    assert k.Note_erfahren("Max Mustermann", "Mathe") == 3.8

# teste Aufgabe 3
def test_position_initialization():
    pos = Position(1, 2, 3)
    assert pos.X == 1
    assert pos.Y == 2
    assert pos.Z == 3

def test_position_addition():
    pos1 = Position(1, 2, 3)
    pos2 = Position(4, 5, 6)
    result = pos1 + pos2
    assert result.X == 5
    assert result.Y == 7
    assert result.Z == 9

def test_position_equality():
    pos1 = Position(1, 2, 3)
    pos2 = Position(1, 2, 3)
    pos3 = Position(4, 5, 6)
    assert pos1 == pos2
    assert not pos1 == pos3
def test_kreatur_initialization():
    pos = Position(1, 2, 3)
    kreatur = Kreatur(pos)
    assert kreatur.Position == pos

def test_kreatur_movement():
    pos1 = Position(1, 2, 3)
    pos2 = Position(4, 5, 6)
    kreatur = Kreatur(pos1)
    kreatur.Bewegen(pos2)
    assert kreatur.Position == pos2

def test_schaf_farbe_attribute():
    pos = Position(1, 2, 3)
    schaf = Schaf(pos, "gruen")
    assert hasattr(schaf, "Farbe"), "Farbe attribute does not exist"
    assert isinstance(schaf.Farbe, str), "Farbe attribute is not of type str"

def test_schaf_geschoren_attribute():
    pos = Position(1, 2, 3)
    schaf = Schaf(pos, "gruen")
    assert hasattr(schaf, "Geschoren"), "Geschoren attribute does not exist"
    assert isinstance(schaf.Geschoren, bool), "Geschoren attribute is not of type bool"

def test_schaf_scheeren():
    pos = Position(1, 2, 3)
    schaf = Schaf(pos, "gruen")
    assert not schaf.Geschoren, "Schaf should not be geschoren initially"
    schaf.Scheeren()
    assert schaf.Geschoren, "Schaf should be geschoren after calling Scheeren"

def test_schaf_faerben():
    pos = Position(1, 2, 3)
    schaf = Schaf(pos, "gruen")
    assert schaf.Farbe == "gruen", "Schaf's initial Farbe should be 'gruen'"
    schaf.Faerben("blau")
    assert schaf.Farbe == "blau", "Schaf's Farbe should be 'blau' after calling Faerben"

def test_schaf_bewegen():
    pos1 = Position(1, 2, 3)
    pos2 = Position(4, 5, 6)
    schaf = Schaf(pos1, "gruen")
    assert schaf.Position == pos1, "Schaf's initial Position should be pos1"
    schaf.Bewegen(pos2)
    assert schaf.Position == pos2, "Schaf's Position should be pos2 after calling Bewegen"

def test_kuh_position_attribute():
    pos = Position(1, 2, 3)
    kuh = Kuh(pos)
    assert hasattr(kuh, "Position"), "Position attribute does not exist"
    assert isinstance(kuh.Position, Position), "Position attribute is not of type Position"

def test_kuh_movement():
    pos1 = Position(1, 2, 3)
    pos2 = Position(4, 5, 6)
    kuh = Kuh(pos1)
    kuh.Bewegen(pos2)
    assert kuh.Position == pos2, "Kuh's Position should be pos2 after calling Bewegen"
