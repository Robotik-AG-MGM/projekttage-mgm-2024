## **Python Datentypen und Variablen**

Dieses Dokument bietet eine Übersicht über Datentypen und Variablen in Python und enthält Aufgaben, um das Gelernte zu üben.

## **Variablen**

Variablen speichern Werte, die später im Programm verwendet werden können. Sie können beliebige Namen haben, die aus Buchstaben, Zahlen und Unterstrichen bestehen, aber sie müssen mit einem Buchstaben oder Unterstrich beginnen.

Beispiel:

```python
x = 3
y = "Hallo"
z = 4.5
```

In diesem Beispiel speichert `x` den Integer-Wert 3, `y` den String-Wert "Hallo" und `z` den Float-Wert 4.5.

---

## **Primitive Datentypen**

### **Strings**

Strings können Buchstaben, Zeichen und Zahlen enthalten. Sie werden hauptsächlich zur Darstellung von Text verwendet und stehen in Anführungszeichen.

```python
print("Hello 10!")
```

Strings können nicht direkt für Berechnungen verwendet werden. Stattdessen werden sie aneinandergereiht.

#### **Zugriff auf einzelne Elemente**

Man kann auf einzelne Zeichen eines Strings zugreifen, indem man den Index des gewünschten Zeichens in eckigen Klammern angibt. Der Index beginnt bei 0.

```python
text = "Python"
print(text[0])  # Ausgabe: P
print(text[1])  # Ausgabe: y
```

#### **Spezielle Funktionen**

- `len(string)`: Gibt die Länge des Strings zurück.
- `string.upper()`: Wandelt den String in Großbuchstaben um.
- `string.lower()`: Wandelt den String in Kleinbuchstaben um.
- `string.replace("alt", "neu")`: Ersetzt im String alle Vorkommen von "alt" durch "neu".

### **Integer**

Integer sind ganze Zahlen ohne Anführungszeichen und werden für Berechnungen verwendet.

```python
print(4 + 9)  # Ergebnis: 13
```

#### **Spezielle Funktionen**

- `int(x)`: Wandelt `x` in einen Integer um.

### **Float**

Floats sind Kommazahlen und können ebenfalls für Berechnungen verwendet werden.

```python
print(4.5 + 3.2)  # Ergebnis: 7.7
```

#### **Spezielle Funktionen**

- `float(x)`: Wandelt `x` in einen Float um.
- `round(x, n)`: Rundet `x` auf `n` Dezimalstellen.

### **Booleans**

Booleans haben zwei Werte: `True` und `False`.

---

## **Komplexe Datentypen**

### **Listen**

Listen können mehrere Werte speichern und werden in eckigen Klammern notiert.

```python
wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"]
wochentage.append("Sonntag")
print(wochentage)
```

#### **Zugriff auf einzelne Elemente**

Man kann auf einzelne Elemente einer Liste zugreifen, indem man den Index des gewünschten Elements in eckigen Klammern angibt.

```python
print(wochentage[0])  # Ausgabe: Montag
print(wochentage[1])  # Ausgabe: Dienstag
```

#### **Spezielle Funktionen**

- `len(liste)`: Gibt die Länge der Liste zurück.
- `liste.append(x)`: Fügt `x` am Ende der Liste hinzu.
- `liste.remove(x)`: Entfernt das erste Vorkommen von `x` in der Liste.
- `liste.index(x)`: Gibt den Index des ersten Vorkommens von `x` in der Liste zurück.

### **Tuples**

Tuples sind wie Listen, aber ihre Werte können nicht verändert werden. Sie werden in runden Klammern notiert.

```python
zahlen_tuple = (1, 2, 3, 4)
print(zahlen_tuple)
```

#### **Zugriff auf einzelne Elemente**

Man kann auf einzelne Elemente eines Tuples zugreifen, indem man den Index des gewünschten Elements in eckigen Klammern angibt.

```python
print(zahlen_tuple[0])  # Ausgabe: 1
print(zahlen_tuple[1])  # Ausgabe: 2
```

### **Dictionaries**

Dictionaries speichern Paare aus Schlüssel und Wert und werden in geschweiften Klammern notiert.

```python
person = {"Name": "Tobi", "Alter": 43, "Beruf": "Busfahrer"}
print(person["Alter"])
```

#### **Zugriff auf einzelne Elemente**

Man kann auf einzelne Werte eines Dictionaries zugreifen, indem man den entsprechenden Schlüssel in eckigen Klammern angibt.

```python
print(person["Name"])  # Ausgabe: Tobi
print(person["Alter"])  # Ausgabe: 43
```

#### **Spezielle Funktionen**

- `dict.keys()`: Gibt eine Liste aller Schlüssel im Dictionary zurück.
- `dict.values()`: Gibt eine Liste aller Werte im Dictionary zurück.
- `dict.items()`: Gibt eine Liste aller Schlüssel-Wert-Paare im Dictionary zurück.
- `dict.get(x)`: Gibt den Wert für den Schlüssel `x` zurück.

---

## **Aufgaben**

### **Variablen**

1. **Erstelle eine String-Variable, die das Wort "Hallo, Welt" enthält und gib sie aus.**

    ```python
    gruss = "Hallo, Welt"
    print(gruss)
    ```

2. **Erstelle eine Integer-Variable und eine Float-Variable, addiere diese und gib das Ergebnis als dritte Variable aus.**

    ```python
    int_var = 5
    float_var = 7.3
    ergebnis = int_var + float_var
    print(ergebnis)
    ```

3. **Erstelle eine Boolean-Variable und gib den Wert in der Konsole aus.**

    ```python
    ist_wahr = True
    print(ist_wahr)
    ```

### **Listen**

1. **Erstelle eine Liste, die `wochentage` heißt.**
    - Schreibe die Tage von Montag bis Samstag in die Liste und gib die Liste aus.
    - Füge mit `wochentage.append()` Sonntag hinzu und gib die Liste nochmal aus.

    ```python
    wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"]
    print(wochentage)
    wochentage.append("Sonntag")
    print(wochentage)
    ```

2. **Erstelle eine Liste von Zahlen, finde die maximale und minimale Zahl und gib sie aus.**

    ```python
    zahlen = [3, 5, 7, 2, 8, 1, 4]
    max_zahl = max(zahlen)
    min_zahl = min(zahlen)
    print("Maximale Zahl:", max_zahl)
    print("Minimale Zahl:", min_zahl)
    ```

3. **Erstelle eine Liste von Namen und sortiere die Liste alphabetisch.**

    ```python
    namen = ["Anna", "Bernd", "Clara", "David"]
    namen.sort()
    print(namen)
    ```

### **Tuples**

1. **Erstelle ein Tuple mit verschiedenen Zahlen und gib es aus.**

    ```python
    zahlen_tuple = (1, 3, 5, 7)
    print(zahlen_tuple)
    ```

2. **Erstelle ein Tuple von Farben und greife auf die zweite Farbe zu.**

    ```python
    farben = ("Rot", "Blau", "Grün", "Gelb")
    print(farben[1])  # Ausgabe: Blau
    ```

### **Dictionary**

1. **Erstelle ein Dictionary mit Namen und Alter einer Person und gib das Alter aus.**

    ```python
    person = {"Name": "Anna", "Alter": 30}
    print(person["Alter"])
    ```

2. **Erstelle ein Dictionary, das die Telefonnummern von Personen speichert. Greife auf die Telefonnummer einer Person zu.**

    ```python
    telefonbuch = {"Anna": "1234", "Bernd": "5678", "Clara": "91011"}
    print(telefonbuch["Bernd"])  # Ausgabe: 5678
    ```

3. **Füge einem bestehenden Dictionary ein neues Schlüssel-Wert-Paar hinzu und gib das Dictionary aus.**

    ```python
    person = {"Name": "Anna", "Alter": 30}
    person["Beruf"] = "Lehrerin"
    print(person)
    ```
