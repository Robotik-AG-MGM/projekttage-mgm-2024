import os
import pytest
import V_Aufgabe_1
import V_Aufgabe_2
# import V_Aufgabe_3


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
def test_mensch_bmi():
    lux = V_Aufgabe_1.Mensch("Luca", 17, 1.82, 75, "männlich")
    assert lux.BMI() == pytest.approx(22.6, abs=0.1)


def test_mensch_name_attribute():
    lux = V_Aufgabe_1.Mensch("Luca", 17, 1.82, 75, "männlich")
    assert hasattr(lux, "Name"), "Name attribute does not exist"
    assert isinstance(lux.Name, str), "Name attribute is not of type str"


def test_mensch_alter_attribute():
    lux = V_Aufgabe_1.Mensch("Luca", 17, 1.82, 75, "männlich")
    assert hasattr(lux, "Alter"), "Alter attribute does not exist"
    assert isinstance(lux.Alter, int), "Alter attribute is not of type int"


def test_mensch_groesse_attribute():
    lux = V_Aufgabe_1.Mensch("Luca", 17, 1.82, 75, "männlich")
    assert hasattr(lux, "Groesse"), "Groesse attribute does not exist"
    assert isinstance(lux.Groesse, float), \
        "Groesse attribute is not of type float"


def test_mensch_gewicht_attribute():
    lux = V_Aufgabe_1.Mensch("Luca", 17, 1.82, 75, "männlich")
    assert hasattr(lux, "Gewicht"), "Gewicht attribute does not exist"
    assert isinstance(lux.Gewicht, int), "Gewicht attribute is not of type int"


def test_mensch_geschlecht_attribute():
    lux = V_Aufgabe_1.Mensch("Luca", 17, 1.82, 75, "männlich")
    assert hasattr(lux, "Geschlecht"), "Geschlecht attribute does not exist"
    assert isinstance(lux.Geschlecht, str), \
        "Geschlecht attribute is not of type str"


def test_mensch_bmi_function():
    lux = V_Aufgabe_1.Mensch("Luca", 17, 1.82, 75, "männlich")
    assert hasattr(lux, "BMI"), "BMI function does not exist"
    assert callable(lux.BMI), "BMI is not a callable function"


def test_mensch_attributes():
    lux = V_Aufgabe_1.Mensch("Luca", 17, 1.82, 75, "männlich")
    assert lux.Name == "Luca"
    assert lux.Alter == 17
    assert lux.Groesse == 1.82
    assert lux.Gewicht == 75
    assert lux.Geschlecht == "männlich"


# teste Aufgabe 2
def test_schueler_name_attribute():
    schueler = V_Aufgabe_2.Schueler("Max Mustermann")
    assert hasattr(schueler, "Name"), "Name attribute does not exist"
    assert isinstance(schueler.Name, str), "Name attribute is not of type str"


def test_schueler_noten_attribute():
    schueler = V_Aufgabe_2.Schueler("Max Mustermann")
    assert hasattr(schueler, "Noten"), "Noten attribute does not exist"
    assert isinstance(schueler.Noten, dict), \
        "Noten attribute is not of type dict"


def test_schueler_note_erfahren():
    schueler = V_Aufgabe_2.Schueler("Max Mustermann",
                                    mathenote=4.5,
                                    deutschnote=3.7)
    assert schueler.Note_erfahren("Mathe") == 4.5
    assert schueler.Note_erfahren("Deutsch") == 3.7


def test_schueler_note_aendern():
    schueler = V_Aufgabe_2.Schueler("Max Mustermann", mathenote=4.5)
    schueler.Note_aendern("Mathe", 3.8)
    assert schueler.Note_erfahren("Mathe") == 3.8


def test_klasse_hinzufuegen():
    klasse = V_Aufgabe_2.Klasse("10A")
    schueler = V_Aufgabe_2.Schueler("Max Mustermann")
    klasse.Hinzufuegen(schueler)
    assert len(klasse.Schueler) == 1
    assert klasse.Schueler[0] == schueler


def test_klasse_entfernen():
    pass
    pass
    klasse = V_Aufgabe_2.Klasse("10A")
    schueler1 = V_Aufgabe_2.Schueler("Max Mustermann")
    schueler2 = V_Aufgabe_2.Schueler("Erika Musterfrau")
    klasse.Hinzufuegen(schueler1)
    klasse.Hinzufuegen(schueler2)
    removed_schueler = klasse.Entfernen("Max Mustermann")
    assert removed_schueler == schueler1
    assert len(klasse.Schueler) == 1
    assert klasse.Schueler[0] == schueler2


def test_klasse_note_erfahren():
    klasse = V_Aufgabe_2.Klasse("10A")
    schueler = V_Aufgabe_2.Schueler("Max Mustermann",
                                    mathenote=4.5,
                                    deutschnote=3.7)
    klasse.Hinzufuegen(schueler)
    assert klasse.Note_erfahren("Max Mustermann", "Mathe") == 4.5
    assert klasse.Note_erfahren("Max Mustermann", "Deutsch") == 3.7


def test_klasse_note_aendern():
    klasse = V_Aufgabe_2.Klasse("10A")
    schueler = V_Aufgabe_2.Schueler("Max Mustermann", mathenote=4.5)
    klasse.Hinzufuegen(schueler)
    klasse.Note_aendern("Max Mustermann", "Mathe", 3.8)
    assert klasse.Note_erfahren("Max Mustermann", "Mathe") == 3.8

# teste Aufgabe 3
