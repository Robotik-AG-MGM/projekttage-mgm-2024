# Variablen Aufgaben Tests
def test_variablen_aufgabe_1():
    from variablen_aufgaben import gruss, teilwort, gruss_upper

    assert gruss == "Hallo, Welt"
    assert teilwort == "Welt"
    assert gruss_upper == "HALLO, WELT"


def test_variablen_aufgabe_2():
    from variablen_aufgaben import ergebnis_1, ergebnis_2, ergebnis_3

    assert isinstance(ergebnis_1, float)
    assert isinstance(ergebnis_2, float)
    assert isinstance(ergebnis_3, float)


def test_variablen_aufgabe_3():
    from variablen_aufgaben import ist_wahr

    assert ist_wahr is True


# Listen Aufgaben Tests
def test_listen_aufgabe_1():
    from listen_aufgaben import wochentage

    assert wochentage == [
        "Montag",
        "Dienstag",
        "Mittwoch",
        "Freitag",
        "Samstag",
        "Sonntag",
    ]


def test_listen_aufgabe_2():
    from listen_aufgaben import m, k, d, neuer_durchschnitt, zahlen

    assert m == max(zahlen)
    assert k == min(zahlen)
    assert d == sum(zahlen) / len(zahlen)
    assert neuer_durchschnitt == sum(zahlen) / len(zahlen)


def test_listen_aufgabe_3():
    from listen_aufgaben import Namen

    tmp = Namen.copy()
    tmp.sort()

    assert Namen == tmp


def test_listen_aufgabe_4():
    from listen_aufgaben import matrix, element

    assert matrix[1][2] == element


# Tuples Aufgaben Tests
def test_tuples_aufgabe_1():
    from dictionary_aufgaben import Zahlen

    assert isinstance(Zahlen, tuple)


def test_tuples_aufgabe_2():
    from tuples_aufgaben import Farben

    assert isinstance(Farben, tuple)


# Dictionary Aufgaben Tests
def test_dictionary_aufgabe_1():
    from dictionary_aufgaben import kontakte

    assert isinstance(kontakte, dict)


def test_dictionary_aufgabe_2():
    from dictionary_aufgaben import nummern

    assert sorted(nummern) == nummern
