from variablen_aufgaben import (
    gruss,
    teilwort,
    gruss_upper,
    ergebnis_1,
    ergebnis_2,
    ergebnis_3,
    ist_wahr,
)
from listen_aufgaben import (
    wochentage,
    m,
    k,
    d,
    neuer_durchschnitt,
    zahlen,
    Namen,
    matrix,
    element,
)
from tuples_aufgaben import Zahlen, Farben
from dictionary_aufgaben import kontakte, nummern


# Variablen Aufgaben Tests
def test_variablen_aufgabe_1():
    assert gruss == "Hallo, Welt"
    assert teilwort == "Welt"
    assert gruss_upper == "HALLO, WELT"


def test_variablen_aufgabe_2():
    assert isinstance(ergebnis_1, float)
    assert isinstance(ergebnis_2, float)
    assert isinstance(ergebnis_3, float)


def test_variablen_aufgabe_3():
    assert ist_wahr is True


# Listen Aufgaben Tests
def test_listen_aufgabe_1():
    assert wochentage == [
        "Montag",
        "Dienstag",
        "Mittwoch",
        "Freitag",
        "Samstag",
        "Sonntag",
    ]


def test_listen_aufgabe_2():
    assert m == max(zahlen)
    assert k == min(zahlen)
    assert d == sum(zahlen) / len(zahlen)
    assert neuer_durchschnitt == sum(zahlen) / len(zahlen)


def test_listen_aufgabe_3():
    tmp = Namen.copy()
    tmp.sort()

    assert Namen == tmp


def test_listen_aufgabe_4():
    assert matrix[1][2] == element


# Tuples Aufgaben Tests
def test_tuples_aufgabe_1():
    assert isinstance(Zahlen, tuple)


def test_tuples_aufgabe_2():
    assert isinstance(Farben, tuple)


# Dictionary Aufgaben Tests
def test_dictionary_aufgabe_1():
    assert isinstance(kontakte, dict)


def test_dictionary_aufgabe_2():
    assert sorted(nummern) == nummern
