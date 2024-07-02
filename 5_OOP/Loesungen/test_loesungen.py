import os
import V_aufgabe_1
import V_aufgabe_2
import V_aufgabe_3

def test_aufgabe_1_exists(): # Funktionsfähigkeit durch Debug hergestellt.
    assert os.path.exists(
        "5_OOP/Loesungen/V_aufgabe_1.py"
    ), "File does not exist"


def test_aufgabe_2_exists(): # Funktionsfähigkeit durch Debug hergestellt.
    assert os.path.exists(
        "5_OOP/Loesungen/V_aufgabe_2.py"
    ), "File does not exist"


def test_aufgabe_3_exists(): # Funktionsfähigkeit durch Debug hergestellt.
    assert os.path.exists(
        "5_OOP/Loesungen/V_aufgabe_3.py"
    ), "File does not exist"


def test_aufgabe_1_output(): # Funktionsfähigkeit durch Debug hergestellt.
    try:
        Test_Mensch = V_aufgabe_1.Mensch("Max", 20, 1.7, 70, "männlich")
        assert hasattr(Test_Mensch, "Name") and hasattr(Test_Mensch, "Alter") and hasattr(Test_Mensch, "Groesse") and hasattr(Test_Mensch, "Gewicht") and hasattr(Test_Mensch, "Geschlecht"), "mindestend eines der Attribute 'Name','Alter','Groesse','Gewicht','Geschlecht' und 'Augenfarbe' existiert niht oder ist falsch geschrieben."
        assert hasattr(Test_Mensch, "BMI") and callable(getattr(Test_Mensch, "BMI")), "Methode 'BMI' existiert nicht oder ist falsch geschrieben"

        assert Test_Mensch.Name == "Max", "Attribut 'Name' wurde falsch initialisiert."
        assert Test_Mensch.Alter == 20, "Attribut 'Alter' wurde falsch initialisiert."
        assert Test_Mensch.Groesse == 1.7, "Attribut 'Groesse' wurde falsch initialisiert."
        assert Test_Mensch.Gewicht == 70, "Attribut 'Gewicht' wurde falsch initialisiert."
        assert Test_Mensch.Geschlecht == "männlich", "Attribut 'Geschlecht' wurde falsch initialisiert"
        Test_Mensch_BMI_1 = Test_Mensch.BMI()
        Test_Mensch_BMI_2 = Test_Mensch.Gewicht / (Test_Mensch.Groesse ** 2)
        assert Test_Mensch_BMI_1 > (Test_Mensch_BMI_2 - 0.1) or Test_Mensch_BMI_1 < (Test_Mensch_BMI_2 + 0.1), "Methode 'BMI' funktioniert nicht richtig"
    except TypeError as e:
        if str(e).startswith("Mensch.__init__()"): 
            assert False, "Kreator falsch definiert"
        else: assert False, str(e)
    except:
        assert False, "Irgendetwas anderes bei 'Mensch' ist schiefgelaufen. Womöglich ist das Objekt falsch geschrieben oder existiert gar nicht. Oder einige Methode nehmen nicht genug oder zu viele Parameter"


def test_aufgabe_2_output(): # Funktionsfähigkeit durch Debug hergestellt.
    try:    # Schueler-Objekt
        Test_Schueler = V_aufgabe_2.Schueler("Max Mustermann")

        assert hasattr(Test_Schueler, "Name") and hasattr(Test_Schueler, "Noten"), "Attribute 'Name' und/oder 'Noten' nicht vorhanden, oder falsch geschrieben"
        assert hasattr(Test_Schueler, "Note_erfahren") and callable(getattr(Test_Schueler, "Note_erfahren")), "Methode 'Note_erfahren' existiert nicht oder ist falsch geschrieben"
        assert hasattr(Test_Schueler, "Note_aendern") and callable(getattr(Test_Schueler, "Note_aendern")), "Methode 'Note_aedern' existiert nicht oder ist falsch geschrieben"

        assert Test_Schueler.Name == "Max Mustermann", "Name wurde falsch initialisiert"
        for temp in Test_Schueler.Noten.items():
            assert temp[1] == 0, "Noten wurden defaultmäßig nicht alle mit 0 initialisiert"
        Test_Schueler.Note_aendern("Mathe", 3)
        assert Test_Schueler.Note_erfahren("Mathe") == 3, "'Note_aendern' oder 'Note_erfahren' funktioniert nicht richtig"
    except TypeError as e:
        if str(e).startswith("Schueler.__init__()"): 
            assert False, "Kreator falsch definiert"
        else: 
            assert False, str(e)
    except:
        assert False, "Irgendetwas anderes bei 'Schueler' ist schiefgelaufen. Womöglich ist das Objekt falsch geschrieben oder existiert gar nicht. Oder einige Methode nehmen nicht genug oder zu viele Parameter"

    try:    # Klasse-Objekt
        Test_Klasse = V_aufgabe_2.Klasse("2a")

        assert hasattr(Test_Klasse, "ID") and hasattr(Test_Klasse, "Schueler"), "Die Attribute 'ID' und/oder 'Schueler' existieren nicht oder sind falsch geschrieben"
        assert hasattr(Test_Klasse, "Hinzufuegen") and callable(getattr(Test_Klasse, "Hinzufuegen")), "Methode 'Hinzufuegen' existiert nicht oder ist falsch geschrieben"
        assert hasattr(Test_Klasse, "Entfernen") and callable(getattr(Test_Klasse, "Entfernen")), "Methode 'Entfernen' existiert nicht oder ist falsch geschrieben"
        assert hasattr(Test_Klasse, "Noten") and callable(getattr(Test_Klasse, "Noten")), "Methode 'Noten' existiert nicht oder ist falsch geschrieben"
        assert hasattr(Test_Klasse, "Note_erfahren") and callable(getattr(Test_Klasse, "Note_erfahren")), "Methode 'Note_erfahren' existiert nicht oder ist falsch geschrieben"
        assert hasattr(Test_Klasse, "Note_aendern") and callable(getattr(Test_Klasse, "Note_aendern")), "Methode 'Note_aendern' existiert nicht oder ist falsch geschrieben"

        assert Test_Klasse.ID =="2a", "ID wurde falsch initialisiert"
        Test_Klasse.Hinzufuegen(V_aufgabe_2.Schueler("Max Mustermann"))
        assert Test_Klasse.Schueler != [] and Test_Klasse.Schueler[0].Name == "Max Mustermann", "Methode 'Hinzufügen' hat nicht funktioniert"
        dic: dict = Test_Klasse.Noten("Max Mustermann")
        for elem in dic.items():
            assert elem[1] == 0, "Noten eines Schülers in Klasse wurden defaultmäßig nicht mit 0 belegt, oder Methode 'Noten funktioniert nicht'"
        Test_Klasse.Note_aendern("Max Mustermann", "Deutsch", 3)
        assert Test_Klasse.Note_erfahren("Max Mustermann", "Deutsch") == 3, "Methode 'Note_aendern' und/oder 'Note_erfahren' funktionieren nicht"
        Max: V_aufgabe_2.Schueler = Test_Klasse.Entfernen("Max Mustermann")
        assert Max.Name == "Max Mustermann" and Max.Note_erfahren("Deutsch") == 3, "Methode 'Enfernen hat einen falschen Schüler zurückgegeben'"
    except TypeError as e:
        if str(e).startswith("Klasse."): 
            assert False, "Kreator falsch definiert"
        else: 
            assert False, str(e)
    except:
        assert False, "Irgendetwas anderes bei 'Klasse' ist schiefgelaufen. Womöglich ist das Objekt falsch geschrieben oder existiert gar nicht. Oder einige Methode nehmen nicht genug oder zu viele Parameter"


def test_aufgabe_3_output(): # Funktionsfähigkeit durch Debug hergestellt.
    try:    #Objekt Position
        Test_Position_1 = V_aufgabe_3.Position(1, 1, 1)
        assert hasattr(Test_Position_1, "X") and hasattr(Test_Position_1, "Y") and hasattr(Test_Position_1, "Z"), "mindestens eines der Attribute 'X', 'Y' und 'Z' aus Position existiert nicht oder ist falsch geschrieben (Die Buchstaben müssen groß geschrieben sein)"
        assert hasattr(Test_Position_1, "__add__") and callable(getattr(Test_Position_1, "__add__")), "Die Operatorüberladung für den Operator '+' in Position existiert nicht"
        assert hasattr(Test_Position_1, "__eq__") and hasattr(Test_Position_1, "__eq__"), "Die Operatorüberladung für den Operator '==' in Position existiert nicht"

        Test_Position_2 = V_aufgabe_3.Position(1, 1, 1)
        assert Test_Position_1 == Test_Position_2, "Vergleichsoperator des Objektes Position funktiniert nicht richtig."
        assert (Test_Position_1 + Test_Position_2) == V_aufgabe_3.Position(2, 2, 2), "Additionsoperator des Objektes Position funktioniert nicht richtig"
    except TypeError as e:
        if str(e).startswith("Position.__init__()"): 
            assert False, "Kreator von Position falsch definiert"
        else: 
            assert False, str(e)
    except:
        assert False, "Irgendetwas anderes bei 'Position' ist schiefgelaufen. Womöglich ist das Objekt falsch geschrieben oder existiert gar nicht. Oder einige Methode nehmen nicht genug oder zu viele Parameter"

    try:    # Objekt Kreatur
        Test_Kreatur = V_aufgabe_3.Kreatur(V_aufgabe_3.Position(1, 0, -1))
        assert hasattr(Test_Kreatur, "Position"), "das Attribut 'Position' in Kreatur existiert nicht oder ist falsch geschrieben"
        assert hasattr(Test_Kreatur, "Bewegen") and callable(getattr(Test_Kreatur, "Bewegen")), "die Methode 'Bewegen' in Kreatur existiert nicht oder ist falsch geschrieben"

        assert Test_Kreatur.Position == V_aufgabe_3.Position(1, 0, -1), "Position in Kreatur wurde falsch initialisiert"
        Test_Kreatur.Bewegen(V_aufgabe_3.Position(5, 0, -5))
        assert Test_Kreatur.Position == V_aufgabe_3.Position(5, 0, -5), "Methode 'Bewegen' von Kreatur funktioniert nicht"
    except TypeError as e:
        if str(e).startswith("Kreatur.__init__()"): 
            assert False, "Kreator von Kreatur falsch definiert"
        else: 
            assert False, str(e)
    except:
        assert False, "Irgendetwas anderes bei 'Kreatur' ist schiefgelaufen. Womöglich ist das Objekt falsch geschrieben oder existiert gar nicht. Oder einige Methode nehmen nicht genug oder zu viele Parameter"

    try:    # Objekt Kuh
        Test_Kuh = V_aufgabe_3.Kuh(V_aufgabe_3.Position(3, 0, 3))
        assert hasattr(Test_Kuh, "Position") and hasattr(Test_Kuh, "Bewegen") and callable(getattr(Test_Kuh, "Bewegen")), "Kuh erbt nicht von Kreatur, Attribut 'Position' und/oder Methode 'Bewegen' sind nicht vorhanden"

        assert Test_Kuh.Position == V_aufgabe_3.Position(3, 0, 3), "Attribut 'Position' in Kuh wurde falsch initialisiert"
        Test_Kuh.Bewegen(V_aufgabe_3.Position(-3, 0, -3))
        assert Test_Kuh.Position == V_aufgabe_3.Position(-3, 0, -3), "Methode 'Bewegen' in Kuh funktioniert nicht richtig"
    except TypeError as e:
        if str(e).startswith("Schaf.__init__()"): 
            assert False, "Kreator von Schaf falsch definiert"
        else: 
            assert False, str(e)
    except:
        assert False, "Irgendetwas anderes bei 'Schaf' ist schiefgelaufen. Womöglich ist das Objekt falsch geschrieben oder existiert gar nicht. Oder einige Methode nehmen nicht genug oder zu viele Parameter"

    try:    # Objekt Schaf:
        Test_Schaf = V_aufgabe_3.Schaf(V_aufgabe_3.Position(-5, 0, 5), "gruen")
        assert hasattr(Test_Schaf, "Position") and hasattr(Test_Schaf, "Bewegen") and callable(getattr(Test_Schaf, "Bewegen")), "Attribut 'Position' und/oder Methode 'Bewegen' in Schaf wurden nicht von Kreatur geerbt"
        assert hasattr(Test_Schaf, "Farbe") and hasattr(Test_Schaf, "Geschoren"), "Attribute 'Farbe' und/oder 'Geschoren' in Schaf existieren nicht oder sind falsch geschrieben"

        assert Test_Schaf.Farbe == "gruen", "Attribut 'Farbe' in Schaf wurde falsch initialisiert"
        assert Test_Schaf.Position == V_aufgabe_3.Position(-5, 0, 5), "Attribut 'Position' in Schaf wurde falsch initialisiert"
        assert Test_Schaf.Geschoren is False, "Attribut 'Geschoren' in Schaf wurde falsch initialisiet, sollte per default False sein"
        Test_Schaf.Bewegen(V_aufgabe_3.Position(1, 0, -1))
        assert Test_Schaf.Position == V_aufgabe_3.Position(1, 0, -1), "Methode 'Bewegen' in Schaf funktioniert nicht richtig"
        Test_Schaf.Faerben("dunkelgruen")
        Test_Schaf.Scheeren()
        assert Test_Schaf.Farbe == "dunkelgruen" and Test_Schaf.Geschoren is True, "Methode 'Faerben' und oder 'Scheeren' in Schaf funktioniert nicht richtig"
    except TypeError as e:
        if str(e).startswith("Schaf.__init__()"): 
            assert False, "Kreator von Schaf falsch definiert"
        else: 
            assert False, str(e)
    except:
        assert False, "Irgendetwas anderes bei 'Schaf' ist schiefgelaufen. Womöglich ist das Objekt falsch geschrieben oder existiert gar nicht. Oder einige Methode nehmen nicht genug oder zu viele Parameter"



test_aufgabe_1_exists()
test_aufgabe_2_exists()
test_aufgabe_3_exists()

test_aufgabe_1_output()
test_aufgabe_2_output()
test_aufgabe_3_output()
