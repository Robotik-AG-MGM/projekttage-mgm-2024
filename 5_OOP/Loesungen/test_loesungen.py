# UNFERTIG !!!

import V_aufgabe_2
import V_aufgabe_3
import os
import subprocess


def test_aufgabe_1_exists():
    assert os.path.exists(
        "5_OOP/Loesungen/V_aufgabe_1.py"
    ), "File does not exist"


def test_aufgabe_2_exists():
    assert os.path.exists(
        "5_OOP/Loesungen/V_aufgabe_2.py"
    ), "File does not exist"


def test_aufgabe_3_exists():
    assert os.path.exists(
        "5_OOP/Loesungen/V_aufgabe_3.py"
    ), "File does not exist"


def test_aufgabe_2_output():
    try:    # Schueler-Objekt
        assert hasattr(V_aufgabe_2.Schueler, "Name") and hasattr(V_aufgabe_2.Schueler, "Noten"), "Attribute 'Name' und/oder 'Noten' nicht vorhanden, oder falsch geschrieben"
        assert hasattr(V_aufgabe_2.Schueler, "Note_erfahren") and callable(getattr(V_aufgabe_2.Schueler, "Note_erfahren")), "Methode 'Note_erfahren' existiert nicht oder ist falsch geschrieben"
        assert hasattr(V_aufgabe_2.Schueler, "Note_aendern") and callable(getattr(V_aufgabe_2.Schueler, "Note_aendern")), "Methode 'Note_aedern' existiert nicht oder ist falsch geschrieben"
        
        Test = V_aufgabe_2.Schueler("Max Mustermann")
        assert Test.Name == "Max Mustermann", "Name wurde falsch initialisiert"
        for temp in Test.Noten.items():
            assert temp == None, "Noten wurden defaultmäßig nicht alle mit None initialisiert"
        Test.Note_aendern("Mathe", 3)
        assert Test.Note_erfahren("Mathe") == 3, "'Note_aendern' oder 'Note_erfahren' funktioniert nicht richtig"
    except TypeError as e:
        if str(e).startswith("Schueler.__init__()"): assert False, "Kreator falsch definiert"
        else: assert False, str(e)
    except:
        assert False, "Irgendetwas anderes bei 'Schueler' ist schiefgelaufen. Womöglich ist das Objekt falsch geschrieben oder existiert gar nicht. Oder einige Methode nehmen nicht genug oder zu viele Parameter"
    
    try:    # Klasse-Objekt
        assert hasattr(V_aufgabe_2.Klasse, "ID") and hasattr(V_aufgabe_2.Klasse, "Schueler"), "Die Attribute 'ID' und/oder 'Schueler' existieren nicht oder sind falsch geschrieben"
        assert hasattr(V_aufgabe_2.Klasse, "Hinzufuegen") and callable(getattr(V_aufgabe_2.Klasse, "Hinzufuegen")), "Methode 'Hinzufuegen' existiert nicht oder ist falsch geschrieben"
        assert hasattr(V_aufgabe_2.Klasse, "Entfernen") and callable(getattr(V_aufgabe_2.Klasse, "Entfernen")), "Methode 'Entfernen' existiert nicht oder ist falsch geschrieben"
        assert hasattr(V_aufgabe_2.Klasse, "Noten") and callable(getattr(V_aufgabe_2.Klasse, "Noten")), "Methode 'Noten' existiert nicht oder ist falsch geschrieben"
        assert hasattr(V_aufgabe_2.Klasse, "Note_erfahren") and callable(getattr(V_aufgabe_2.Klasse, "Note_erfahren")), "Methode 'Note_erfahren' existiert nicht oder ist falsch geschrieben"
        assert hasattr(V_aufgabe_2.Klasse, "Note_aendern") and callable(getattr(V_aufgabe_2.Klasse, "Note_aendern")), "Methode 'Note_aendern' existiert nicht oder ist falsch geschrieben"
    
        Test_Klasse = V_aufgabe_2.Klasse("2a")
        assert Test_Klasse.ID =="2a", "ID wurde falsch initialisiert"
        Test_Klasse.Hinzufuegen(V_aufgabe_2.Schueler("Max Mustermann"))
        assert Test_Klasse.Schueler == [V_aufgabe_2.Schueler("Max Mustermann")], "Methode 'Hinzufügen' hat nicht funktioniert"
        dic: dict = Test_Klasse.Noten
        for elem in dic.items():
            assert elem == None, "Noten eines Schülers in Klasse wurden defaultmäßig nicht mit None belegt, oder Methode 'Noten funktioniert nicht'"
        Test_Klasse.Note_aendern("Max Mustermann", "Deutsch", 3)
        assert Test_Klasse.Note_erfahren("Max Mustermann", "Deutsch") == 3, "Methode 'Note_aendern' und/oder 'Note_erfahren' funktionieren nicht"
        Max: V_aufgabe_2.Schueler = Test_Klasse.Entfernen("Max Mustermann")
        assert Max.Name == "Max Mustermann" and Max.Note_erfahren("Deutsch") == 3, "Methode 'Enfernen hat einen falschen Schüler zurückgegeben'"
    except TypeError as e:
        if str(e).startswith("Klasse."): assert False, "Kreator falsch definiert"
        else: assert False, str(e)
    except:
        assert False, "Irgendetwas anderes bei 'Klasse' ist schiefgelaufen. Womöglich ist das Objekt falsch geschrieben oder existiert gar nicht. Oder einige Methode nehmen nicht genug oder zu viele Parameter"


def test_aufgabe_3_output():
    try:    #Objekt Position
        assert hasattr(V_aufgabe_3.Position, "X") and hasattr(V_aufgabe_3.Position, "Y") and hasattr(V_aufgabe_3.Position, "Z"), "mindestens eines der Attribute 'X', 'Y' und 'Z' aus Position existiert nicht"
        assert hasattr(V_aufgabe_3.Position, "__add__") and callable(getattr(V_aufgabe_3.Position, "__add__")), "Die Operatorüberladung für den Operator '+' in Position existiert nicht"
        assert hasattr(V_aufgabe_3.Position, "__eq__") and hasattr(getattr(V_aufgabe_3.Position, "__eq__")), "Die Operatorüberladung für den Operator '==' in Position existiert nicht"
        
        Test_Position_1 = V_aufgabe_3.Position(1, 1, 1)
        Test_Position_2 = V_aufgabe_3.Position(1, 1, 1)
        assert Test_Position_1 == Test_Position_2, "Vergleichsoperator des Objektes Position funktiniert nicht richtig."
        assert (Test_Position_1 + Test_Position_2) == V_aufgabe_3.Position(2, 2, 2), "Additionsoperator des Objektes Position funktioniert nicht richtig"
    except TypeError as e:
        if str(e).startswith("Position.__init__()"): assert False, "Kreator von Position falsch definiert"
        else: assert False, str(e)
    except:
        assert False, "Irgendetwas anderes bei 'Position' ist schiefgelaufen. Womöglich ist das Objekt falsch geschrieben oder existiert gar nicht. Oder einige Methode nehmen nicht genug oder zu viele Parameter"

    try:    # Objekt Kreatur
        assert hasattr(V_aufgabe_3.Kreatur, "Position"), "das Attribut 'Position' in Kreatur existiert nicht"
        assert hasattr(V_aufgabe_3.Kreatur, "Bewegen") and callable(getattr(V_aufgabe_3.Kreatur, "Bewegen")), "die Methode 'Bewegen' in Kreatur existiert nicht"

        Test_Kreatur = V_aufgabe_3.Kreatur(V_aufgabe_3.Position(1, 0, -1))
        assert Test_Kreatur.Position == V_aufgabe_3.Position(1, 0, -1), "Position in Kreatur wurde falsch initialisiert"
        Test_Kreatur.Bewegen(V_aufgabe_3.Position(5, 0, -5))
        assert Test_Kreatur.Position == V_aufgabe_3.Position(5, 0, -5), "Methode 'Bewegen' von Kreatur funktioniert nicht"
    except TypeError as e:
        if str(e).startswith("Kreatur.__init__()"): assert False, "Kreator von Kreatur falsch definiert"
        else: assert False, str(e)
    except:
        assert False, "Irgendetwas anderes bei 'Kreatur' ist schiefgelaufen. Womöglich ist das Objekt falsch geschrieben oder existiert gar nicht. Oder einige Methode nehmen nicht genug oder zu viele Parameter"

    try:    # Objekt Schaf: TODO
        assert hasattr(V_aufgabe_3.Schaf, )
    except TypeError as e:

    except: