import aufgabe_1
import aufgabe_2
import aufgabe_3
import aufgabe_4
import aufgabe_5


def test_aufgabe_1(capfd):
    aufgabe_1.hallo_welt()
    out = capfd.readouterr()
    assert out.out == 'Hallo Welt!\n'


def test_aufgabe_2():
    assert aufgabe_2.addiere(1, 2) == 3
    assert aufgabe_2.addiere(3, 4) == 7
    assert aufgabe_2.addiere(5, 6) == 11


def test_aufgabe_3():
    assert aufgabe_3.ist_positiv(1) == True
    assert aufgabe_3.ist_positiv(0) == False
    assert aufgabe_3.ist_positiv(-1) == False


def test_aufgabe_4():
    assert aufgabe_4.ist_teilbar(4, 2) == True
    assert aufgabe_4.ist_teilbar(4, 3) == False
    assert aufgabe_4.ist_teilbar(4, 4) == True


def test_aufgabe_5(capfd):
    aufgabe_5.drucke_bis_zehn()
    out = capfd.readouterr()
    assert out.out == '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n'
