import variablen_aufgaben
import listen_aufgaben
import tuples_aufgaben
import dictionary_aufgaben


def test_gruss():
    assert variablen_aufgaben.gruss == "Hallo, Welt"


def test_ergebnis():
    assert variablen_aufgaben.ergebnis == 12.3


def test_ist_wahr():
    assert variablen_aufgaben.ist_wahr is True


def test_wochentage():
    assert listen_aufgaben.wochentage == [
        "Montag",
        "Dienstag",
        "Mittwoch",
        "Donnerstag",
        "Freitag",
        "Samstag",
        "Sonntag",
    ]


def test_max_zahl():
    assert listen_aufgaben.max_zahl == 8


def test_min_zahl():
    assert listen_aufgaben.min_zahl == 1


def test_namen():
    assert listen_aufgaben.namen == ["Anna", "Bernd", "Clara", "David"]


def test_zahlen_tuple():
    assert tuples_aufgaben.zahlen_tuple == (1, 3, 5, 7)


def test_farbe():
    assert tuples_aufgaben.farben[1] == "Blau"


def test_person_alter():
    assert dictionary_aufgaben.person["Alter"] == 30


def test_telefonnummer():
    assert dictionary_aufgaben.telefonbuch["Bernd"] == "5678"


def test_person_beruf():
    assert dictionary_aufgaben.person["Beruf"] == "Lehrerin"
