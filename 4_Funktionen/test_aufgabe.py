import pytest
from Aufgaben import aufgabe_1, aufgabe_2, aufgabe_3, aufgabe_4, aufgabe_5

def test_aufgabe_1():
    assert aufgabe_1.hallo_welt() == "Hallo Welt!"

def test_aufgabe_2():
    aufgabe_2.addiere(1, 2) == 3
    aufgabe_2.addiere(3, 4) == 7
    aufgabe_2.addiere(5, 6) == 11

def test_aufgabe_3():
    aufgabe_3.ist_positiv(1) == True
    aufgabe_3.ist_positiv(0) == False
    aufgabe_3.ist_positiv(-1) == False

def test_aufgabe_4():
    aufgabe_4.ist_teilbar(4, 2) == True
    aufgabe_4.ist_teilbar(4, 3) == False
    aufgabe_4.ist_teilbar(4, 4) == True

def test_aufgabe_5():
    aufgabe_5.drucke_bis_zehn() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]