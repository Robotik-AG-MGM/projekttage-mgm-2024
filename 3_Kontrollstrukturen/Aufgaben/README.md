# Aufgaben zu Kontrollstruckturen

Erstelle zu jeder Aufgabe eine eigene Pythondatei und benenne sie entsprechend ihrer Nummer:
`aufgabe_x.py`. Bei Aufgabe 1 z.b. `aufgabe_1.py`

## Boolsche Ausdrücke

### Aufagbe 1

1. Erstelle eine boolesche Variable `wahr` und weise ihr den Wert `True` zu.
2. Erstelle eine boolesche Variable `falsch` und weise ihr den Wert `False` zu.
3. Erstelle eine boolesche Variable `ergebnis` und weise ihr das Ergebnis von `wahr and falsch` zu. Was ist das Ergebnis?

### Aufgabe 2

1. Erstelle eine Variable `zahl1` und weise ihr den Wert 10 zu.
2. Erstelle eine Variable `zahl2` und weise ihr den Wert 5 zu.
3. Erstelle eine boolesche Variable `groesser` und weise ihr das Ergebnis von `zahl1 > zahl2` zu.
4. Erstelle eine boolesche Variable `kleiner` und weise ihr das Ergebnis von `zahl1 < zahl2` zu.
5. Erstelle eine boolesche Variable `gleich` und weise ihr das Ergebnis von `zahl1 == zahl2` zu

### Aufgabe 3

1. Erstelle eine boolesche Variable `bedingung1` und weise ihr den Wert `True` zu.
2. Erstelle eine boolesche Variable `bedingung2` und weise ihr den Wert `False` zu.
3. Erstelle eine boolesche Variable `ergebnis1` und weise ihr das Ergebnis von `bedingung1 and bedingung2` zu. Was ist das Ergebnis?
4. Erstelle eine boolesche Variable `ergebnis2` und weise ihr das Ergebnis von `bedingung1 or bedingung2` zu. Was ist das Ergebnis?

### Aufgabe 4

1. Erstelle eine boolesche Variable `bedingung` und weise ihr den Wert `True` zu.
2. Erstelle eine boolesche Variable `negation` und weise ihr das Ergebnis von `not bedingung` zu. Was ist das Ergebnis?

## Boolesche Algebra

### Aufgabe 5

1. Erstelle eine boolesche Variable `a` und weise ihr den Wert `True` zu.
2. Erstelle eine boolesche Variable `b` und weise ihr den Wert `False` zu.
3. Berechne das Ergebnis der AND-Operation von a und b und weise es der Variable `ergebnis` zu.

### Aufgabe 6

1. Erstelle eine boolesche Variable `x` und weise ihr den Wert `True` zu.
2. Erstelle eine boolesche Variable `y` und weise ihr den Wert `False` zu.
3. Berechne das Ergebnis der OR-Operation von x und y und weise es der Variable `ergebnis` zu.

### Aufgane 7

1. Erstelle eine boolesche Variable `c` und weise ihr den Wert `True` zu.
2. Verwende die NOT-Operation, um den Wert von c umzukehren, und weise das Ergebnis der Variable `negation` zu.

## Bedingungen (if, else, elif)

### Aufgabe 8

1. Erstelle eine Variable `zahl` und weise ihr den Wert `10` zu.
2. Schreibe eine Bedingung, die überprüft, ob zahl groeszer als `5` ist. Wenn die Bedingung wahr ist, gib `"Die Zahl ist groeszer als 5"` aus, sonst gib `"Die Zahl ist nicht groeszer als 5"` aus.

### Aufagbe 9

1. Erstelle eine Variable `note` und weise ihr den Wert `85` zu (angenommen, dies ist eine Schülernote).
2. Schreibe eine Bedingung, die folgende Ausgaben je nach der Note generiert:
    - Wenn die Note groeszer oder gleich `90` ist, gib `"Sehr gut!"` aus.
    - Wenn die Note zwischen `80` und `89` liegt, gib `"Gut!"` aus.
    - Wenn die Note zwischen `70` und `79` liegt, gib `"Befriedigend"` aus.
    - Wenn die Note zwischen `60` und `69` liegt, gib `"Ausreichend"` aus.
    - Wenn die Note kleiner als `60` ist, gib `"Durchgefallen"` aus.

### Aufgabe 10

1. Erstelle eine Variable `text` und weise ihr einen beliebigen Text zu.
2. Schreibe eine Bedingung, die überprüft, ob der Text `"Python"` enthaelt. Wenn ja, gib `"Der Text enthaelt Python"` aus, ansonsten gib `"Der Text enthaelt kein Python"` aus.

```python
>>> "a" in "Hallo"
True  # a ist in Hallo entahlten
```

### Aufgabe 11

1. Erstelle eine Variable `zahl` und weise ihr den Wert `15` zu.
2. Erstelle eine Variable `teiler` und weise ihr den Wert `3` zu.
3. Schreibe eine Bedingung, die überprüft, ob zahl durch teiler ohne Rest teilbar ist. Wenn ja, gib `"Die Zahl ist durch 3 teilbar"` aus. Wenn nicht, gib `"Die Zahl ist nicht durch 3 teilbar"` aus.

#### Info

Um die Teilbarkeit zu testen, benutzen wir in Python den %. Dieser berechnet den Rest einer Division. Angenommen, wir haben die Division 10 / 3. Wenn wir diese Division durchführen, erhalten wir ein Ergebnis von 3 mit einem Rest von 1. Das bedeutet, dass 3 mal 3 gleich 9 ist, und wir haben noch eine übriggebliebene 1. Um diesen Rest in Python zu berechnen, verwenden wir den Modulo-Operator:

```python
>>> 10 % 3
1
```

In diesem Beispiel gibt 10 % 3 den Wert 1 zurück, weil 10 durch 3 geteilt wird und der Rest 1 betraegt.
Hier sind einige weitere Beispiele:

```python
>>> 15 % 7
1

>>> 20 % 4
0
```

- `15 % 7` gibt 1 zurück, weil 15 durch 7 geteilt wird und der Rest 1 betraegt.
- `20 % 4` gibt 0 zurück, weil 20 durch 4 geteilt wird und es keinen Rest gibt.

Der Modulo-Operator ist besonders nützlich, wenn wir überprüfen moechten, ob eine Zahl gerade oder ungerade ist. Wenn eine Zahl modulo 2 gleich 0 ist, ist sie gerade, andernfalls ist sie ungerade.

```python
>>> 6 % 2
0  # 6 ist gerade

>>> 7 % 2
1  # 7 ist ungerade
```

### Aufgabe 12

1. Erstelle eine Variable `alter` und weise ihr den Wert `18` zu.
2. Erstelle eine Variable `ausweis` und weise ihr den Wert `True` zu (angenommen, der Benutzer hat einen Ausweis).
3. Schreibe eine Bedingung, die überprüft, ob die Person alt genug ist, um in einen Club zu gehen. Die Bedingung sollte folgende Kriterien erfüllen:
    - Die Person muss mindestens 18 Jahre alt sein.
    - Wenn die Person jünger als 18 ist, sollte sie einen Ausweis haben.
4. Gib entsprechende Ausgaben basierend auf der Bedingung aus.

## Schleifen (while, for)

### Aufgabe 13

1. Verwende eine `while`-Schleife, um die Zahlen von 1 bis 5 auszugeben.

### Aufgabe 14

1. Erstelle eine Liste `fruechte` mit den Elementen `"Apfel", "Banane", "Orange", "Erdbeere"`.
2. Verwende eine `for`-Schleife, um jede Frucht in der Liste auszugeben.

### Aufgabe 15

1. Verwende eine `for`-Schleife, um die geraden Zahlen von 2 bis 10 auszugeben.

#### Info

Um Zahlen in einer `for`-Schleife auszugeben, benutzen wir die `range(n)` Funktion. Sie gibt die Zahlen von `0` bis `n-1` aus

```python
>>> for x inn range(3):
>>>     print(x)
0
1
2
```

### Aufgabe 16

1. Verwende eine `while`-Schleife, um Zufallszahlen zwischen 1 und 10 zu generieren, bis eine 7 erreicht wird.
2. Gib die Anzahl der Versuche aus, die benoetigt wurden, um die 7 zu erreichen.

#### Info
Um Zufallszahlen zu erzeugen, müssen wir die Erweiterung `random` importieren. Das machen wir ganz am Anfang unseres Codes. Um nun eine Zufallszahl zu erzeugen benutzen wir die Funktion `random.randint(start, ende)`, die eine Zufallszahl erzeugt, die im Bereich zwischen Start und Ende, liegt (start und ende inbegriffen).

```python
>>> import random
>>> # irgend ein code hier
>>> zahl = random.randint(1, 10) # Erzeugt eine Zufalszahl zwischen 1 unnd 10. Beide beinhaltet
3  # a ist in Hallo entahlten
```

### Aufgabe 17

1. Erstelle eine verschachtelte Liste matrix mit den Elementen:

```python
matrix = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
```

2. Verwende eine `for`-Schleife, um jedes Element in der Matrix auszugeben.
