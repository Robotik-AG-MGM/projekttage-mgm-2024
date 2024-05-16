import pytest

import l_aufgabe_1
import l_aufgabe_2
import l_aufgabe_3
import l_aufgabe_4
import l_aufgabe_5

def test_aufgabe_1(capfd):
    l_aufgabe_1.hallo_welt()
    out = capfd.readouterr()
    assert out.out == 'Hallo Welt!\n'


def test_aufgabe_2():
    assert l_aufgabe_2.addiere(1, 2) == 3
    assert l_aufgabe_2.addiere(3, 4) == 7
    assert l_aufgabe_2.addiere(5, 6) == 11


def test_aufgabe_3():
    assert l_aufgabe_3.ist_positiv(1) is True
    assert l_aufgabe_3.ist_positiv(0) is False
    assert l_aufgabe_3.ist_positiv(-1) is False


def test_aufgabe_4():
    assert l_aufgabe_4.ist_teilbar(4, 2) is True
    assert l_aufgabe_4.ist_teilbar(4, 3) is False
    assert l_aufgabe_4.ist_teilbar(4, 4) is True


def test_aufgabe_5(capfd):
    l_aufgabe_5.drucke_bis_zehn()
    out = capfd.readouterr()
    assert out.out == '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n'
