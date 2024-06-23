import os
import subprocess
import l_aufgabe_1
import l_aufgabe_2
import l_aufgabe_3
import l_aufgabe_4
import l_aufgabe_5
import l_aufgabe_6
import l_aufgabe_7
import l_aufgabe_8
import l_aufgabe_9
import l_aufgabe_10
import l_aufgabe_11
import l_aufgabe_12
import l_aufgabe_13
import l_aufgabe_14
import l_aufgabe_15
import l_aufgabe_16
import l_aufgabe_17


def test_aufgabe_1_exists():
    assert os.path.exists(
        "3_Kontrollstrukturen/Loesungen/l_aufgabe_1.py"
    ), "File does not exist"


def test_aufgabe_1():
    assert l_aufgabe_1.wahr, "Das Ergebnis ist falsch"
    assert not l_aufgabe_1.falsch, "Das Ergebnis ist falsch"
    assert not l_aufgabe_1.ergebnis, "Das Ergebnis ist falsch"


def test_aufgabe_2_exists():
    assert os.path.exists(
        "3_Kontrollstrukturen/Loesungen/l_aufgabe_2.py"
    ), "File does not exist"


def test_aufgabe_2():
    assert l_aufgabe_2.zahl1 == 10, "Variable 'zahl1' ist falsch"
    assert l_aufgabe_2.zahl2 == 5, "Variable 'zahl2' ist falsch"
    assert l_aufgabe_2.groesser, "Variable 'groesser' ist falsch"
    assert not l_aufgabe_2.kleiner, "Variable 'kleiner' ist falsch"
    assert not l_aufgabe_2.gleich, "Variable 'gleich' ist falsch"


def test_aufgabe_3_exists():
    assert os.path.exists(
        "3_Kontrollstrukturen/Loesungen/l_aufgabe_3.py"
    ), "File does not exist"


def test_aufgabe_3():
    assert l_aufgabe_3.bedingung1, "Variable 'bedingung1' ist falsch"
    assert not l_aufgabe_3.bedingung2, "Variable 'bedingung2' ist falsch"
    assert not l_aufgabe_3.ergebnis1, "Variable 'ergebnis1' ist falsch"
    assert l_aufgabe_3.ergebnis2, "Variable 'ergebnis2' ist falsch"


def test_aufgabe_4_exists():
    assert os.path.exists(
        "3_Kontrollstrukturen/Loesungen/l_aufgabe_4.py"
    ), "File does not exist"


def test_aufgabe_4():
    assert l_aufgabe_4.bedingung, "Variable 'bedingung' ist falsch"
    assert not l_aufgabe_4.negation, "Variable 'negation' ist falsch"


def test_aufgabe_5_exists():
    assert os.path.exists(
        "3_Kontrollstrukturen/Loesungen/l_aufgabe_5.py"
    ), "File does not exist"


def test_aufgabe_5():
    assert l_aufgabe_5.a, "Variable 'a' ist falsch"
    assert not l_aufgabe_5.b, "Variable 'b' ist falsch"
    assert not l_aufgabe_5.ergebnis, "Variable 'ergebnis' ist falsch"


def test_aufgabe_6_exists():
    assert os.path.exists(
        "3_Kontrollstrukturen/Loesungen/l_aufgabe_6.py"
    ), "File does not exist"


def test_aufgabe_6():
    assert l_aufgabe_6.x, "Variable 'x' ist falsch"
    assert not l_aufgabe_6.y, "Variable 'y' ist falsch"
    assert l_aufgabe_6.ergebnis, "Variable 'ergebnis' ist falsch"


def test_aufgabe_7_exists():
    assert os.path.exists(
        "3_Kontrollstrukturen/Loesungen/l_aufgabe_7.py"
    ), "File does not exist"


def test_aufgabe_7():
    assert l_aufgabe_7.c, "Variable 'c' ist falsch"
    assert not l_aufgabe_7.negation, "Variable 'negation' ist falsch"


def test_aufgabe_8_exists():
    assert os.path.exists(
        "3_Kontrollstrukturen/Loesungen/l_aufgabe_8.py"
    ), "File does not exist"


def test_aufgabe_8():
    assert l_aufgabe_8.zahl == 10, "Variable 'zahl' ist falsch"
    output = subprocess.check_output(
        ["python", "3_Kontrollstrukturen/Loesungen/l_aufgabe_8.py"]
    )
    assert output == b"Die Zahl ist groeszer als 5\n", "Output is wrong"


def test_aufgabe_9_exists():
    assert os.path.exists(
        "3_Kontrollstrukturen/Loesungen/l_aufgabe_9.py"
    ), "File does not exist"


def test_aufgabe_9():
    assert l_aufgabe_9.note == 85, "Variable 'note' ist falsch"
    output = subprocess.check_output(
        ["python", "3_Kontrollstrukturen/Loesungen/l_aufgabe_9.py"]
    )
    assert output == b"Gut!\n", "Output is wrong"

    # l_aufgabe_9.note = 100
    # output = subprocess.check_output(["python", "3_Kontrollstrukturen/Loesungen/l_aufgabe_9.py"])
    # assert output == b"Sehr gut!\n", "Output is wrong"

    # l_aufgabe_9.note = 75
    # output = subprocess.check_output(["python", "3_Kontrollstrukturen/Loesungen/l_aufgabe_9.py"])
    # assert output == b"Befriedigend\n", "Output is wrong"

    # l_aufgabe_9.note = 65
    # output = subprocess.check_output(["python", "3_Kontrollstrukturen/Loesungen/l_aufgabe_9.py"])
    # assert output == b"Ausreichend\n", "Output is wrong"

    # l_aufgabe_9.note = 55
    # output = subprocess.check_output(["python", "3_Kontrollstrukturen/Loesungen/l_aufgabe_9.py"])
    # assert output == b"Durchgefallen\n", "Output is wrong"


def test_aufgabe_10_exists():
    assert os.path.exists(
        "3_Kontrollstrukturen/Loesungen/l_aufgabe_10.py"
    ), "File does not exist"


def test_aufgabe_10():
    # l_aufgabe_10.text = "Beliebiger Text"
    # output = subprocess.check_output(["python", "3_Kontrollstrukturen/Loesungen/l_aufgabe_10.py"])
    # assert output == b"Der Text enthaelt kein Python\n", "Output is wrong"
    # l_aufgabe_10.text = "Beliebiger Python Text"
    # output = subprocess.check_output(["python", "3_Kontrollstrukturen/Loesungen/l_aufgabe_10.py"])
    # assert output == b"Der Text enthaelt Python\n", "Output is wrong"
    pass


def test_aufgabe_11_exists():
    assert os.path.exists(
        "3_Kontrollstrukturen/Loesungen/l_aufgabe_11.py"
    ), "File does not exist"


def test_aufgabe_11():
    assert l_aufgabe_11.zahl == 15, "Variable 'zahl' ist falsch"
    assert l_aufgabe_11.teiler == 3, "Variable 'teiler' ist falsch"
    output = subprocess.check_output(
        ["python", "3_Kontrollstrukturen/Loesungen/l_aufgabe_11.py"]
    )
    assert output == b"Die Zahl ist durch 3 teilbar\n", "Output is wrong"

    # l_aufgabe_11.zahl = 16
    # output = subprocess.check_output(["python", "3_Kontrollstrukturen/Loesungen/l_aufgabe_11.py"])
    # assert output == b"Die Zahl ist nicht durch 3 teilbar\n", "Output is wrong"


def test_aufgabe_12_exists():
    assert os.path.exists(
        "3_Kontrollstrukturen/Loesungen/l_aufgabe_12.py"
    ), "File does not exist"


def test_aufgabe_12():
    assert l_aufgabe_12.alter == 18, "Variable 'alter' ist falsch"
    assert l_aufgabe_12.ausweis, "Variable 'ausweis' ist falsch"


def test_aufgabe_13_exists():
    assert os.path.exists(
        "3_Kontrollstrukturen/Loesungen/l_aufgabe_13.py"
    ), "File does not exist"


def test_aufgabe_13():
    output = subprocess.check_output(
        ["python", "3_Kontrollstrukturen/Loesungen/l_aufgabe_13.py"]
    )
    assert output == b"1\n2\n3\n4\n5\n", "Output is wrong"


def test_aufgabe_14_exists():
    assert os.path.exists(
        "3_Kontrollstrukturen/Loesungen/l_aufgabe_14.py"
    ), "File does not exist"


def test_aufgabe_14():
    output = subprocess.check_output(
        ["python", "3_Kontrollstrukturen/Loesungen/l_aufgabe_14.py"]
    )
    assert output == b"Apfel\nBanane\nOrange\nErdbeere\n", "Output is wrong"


def test_aufgabe_15_exists():
    assert os.path.exists(
        "3_Kontrollstrukturen/Loesungen/l_aufgabe_15.py"
    ), "File does not exist"


def test_aufgabe_15():
    output = subprocess.check_output(
        ["python", "3_Kontrollstrukturen/Loesungen/l_aufgabe_15.py"]
    )
    assert output == b"2\n4\n6\n8\n10\n", "Output is wrong"


def test_aufgabe_16_exists():
    assert os.path.exists(
        "3_Kontrollstrukturen/Loesungen/l_aufgabe_16.py"
    ), "File does not exist"


def test_aufgabe_17_exists():
    assert os.path.exists(
        "3_Kontrollstrukturen/Loesungen/l_aufgabe_17.py"
    ), "File does not exist"


def test_aufgabe_17():
    assert l_aufgabe_17.matrix == [[1, 2, 3], [4, 5, 6], [7, 8, 9]], "Variable 'matrix' ist falsch"
    output = subprocess.check_output(
        ["python", "3_Kontrollstrukturen/Loesungen/l_aufgabe_17.py"]
    )
    assert output == b"1\n2\n3\n4\n5\n6\n7\n8\n9\n", "Output is wrong"
