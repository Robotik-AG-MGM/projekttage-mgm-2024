# UNFERTIG !!!

import V_aufgabe_1
import os
import subprocess


def test_aufgabe_1_exists():
    assert os.path.exists(
        "5_OOP/Loesungen/V_aufgabe_1.py"
    ), "File does not exist"


# def test_aufgabe_2_exists():
#     assert os.path.exists(
#         "1_Einfuehrung/Loesungen/l_aufgabe_2.py"
#     ), "File does not exist"


def test_aufgabe_1_output():
    Test = V_aufgabe_1.Schaf(0, 0, 0, "blau", False)
    assert Test.X == 0 and Test.Y == 0 and Test.X == 0, "Error whilst controlling the coordinates"
    assert Test.Farbe == "blau" and Test.Geschoren == False, "Error whilst controlling 'Farbe' and 'Geschoren' Attribut"
    Test.faerben("rot")
    Test.scheeren()
    assert Test.Farbe == "rot" and Test.Geschoren == True, "At least one of the methods 'faerben' and 'scheeren' does not work"


# def test_aufgabe_2_output():
#     output = (
#         subprocess.check_output(["python", "1_Einfuehrung/Loesungen/l_aufgabe_2.py"])
#         .decode("utf-8")
#         .strip()
#     )
#     assert output == "Name: Max , Alter: 20", "Output is not 'Name: Max , Alter: 20'"