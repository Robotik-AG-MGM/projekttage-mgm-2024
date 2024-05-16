import pytest
from Lösungen import l_aufgabe_1, l_aufgabe_2, l_aufgabe_3, l_aufgabe_4, l_aufgabe_5

def test_aufgabe_1(capfd):
    l_aufgabe_1.hallo_welt()
    out = capfd.readouterr()
    assert out.out == 'Hallo Welt!\n'

def test_aufgabe_2():
    l_aufgabe_2.addiere(1, 2) == 3
    l_aufgabe_2.addiere(3, 4) == 7
    l_aufgabe_2.addiere(5, 6) == 11

def test_aufgabe_3():
    l_aufgabe_3.ist_positiv(1) == True
    l_aufgabe_3.ist_positiv(0) == False
    l_aufgabe_3.ist_positiv(-1) == False

def test_aufgabe_4():
    l_aufgabe_4.ist_teilbar(4, 2) == True
    l_aufgabe_4.ist_teilbar(4, 3) == False
    l_aufgabe_4.ist_teilbar(4, 4) == True

def test_aufgabe_5(capfd):
    l_aufgabe_5.drucke_bis_zehn()
    out = capfd.readouterr()
    assert out.out == '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n'