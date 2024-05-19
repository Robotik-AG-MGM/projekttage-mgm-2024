import os
import subprocess


def test_aufgabe_1_exists():
    assert os.path.exists(
        "1_Einführung/Loesungen/l_aufgabe_1.py"
    ), "File does not exist"


def test_aufgabe_2_exists():
    assert os.path.exists(
        "1_Einführung/Loesungen/l_aufgabe_2.py"
    ), "File does not exist"


def test_aufgabe_1_output():
    output = (
        subprocess.check_output(["python", "1_Einführung/Loesungen/l_aufgabe_1.py"])
        .decode("utf-8")
        .strip()
    )
    assert output == "Hallo, Welt!", "Output is not 'Hallo, Welt!'"


def test_aufgabe_2_output():
    output = (
        subprocess.check_output(["python", "1_Einführung/Loesungen/l_aufgabe_2.py"])
        .decode("utf-8")
        .strip()
    )
    assert output == "Name: Max , Alter: 20", "Output is not 'Name: Max , Alter: 20'"
