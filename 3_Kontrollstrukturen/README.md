# Boolesche Ausdrücke

## Was sind Boolesche Ausdrücke?

Boolesche Ausdrücke sind Ausdrücke, die entweder wahr (True) oder falsch (False) sind. In Python werden sie häufig verwendet, um Bedingungen auszudrücken oder Entscheidungen zu treffen.

## Wann ergibt ein logisches Gatter "wahr"?

Um zu verstehen, wann ein logisches Gatter wahr ergibt, betrachten wir die grundlegenden logischen Operatoren:

1. **AND (und) - and**: Das logische Gatter "and" ergibt "wahr" (True), wenn beide Operanden "wahr" sind. Andernfalls ergibt es "falsch" (False). Beispiel: `True and True` ergibt True, `True and False` ergibt False.

2. **OR (oder) - or**: Das logische Gatter "or" ergibt "wahr", wenn mindestens einer der Operanden "wahr" ist. Es ergibt "falsch", wenn beide Operanden "falsch" sind. Beispiel: `True or False` ergibt True, `False or False` ergibt False.

3. **NOT (nicht) - not**: Das logische Gatter "not" kehrt den Wert des Operanden um. Wenn der Operand "wahr" ist, ergibt "not" False, und wenn der Operand "falsch" ist, ergibt "not" True. Beispiel: `not True` ergibt False, `not False` ergibt True.

### Vergleichsoperatoren

Vergleichsoperatoren werden verwendet, um Werte zu vergleichen und boolesche Ausdrücke zu erstellen.

Wichtige Vergleichsoperatoren:

- **Größer als (>)**: Vergleicht, ob der linke Wert größer ist als der rechte Wert. Beispiel: `5 > 3` ergibt True.
- **Kleiner als (<)**: Vergleicht, ob der linke Wert kleiner ist als der rechte Wert. Beispiel: `2 < 7` ergibt True.
- **Größer oder gleich (>=)**: Vergleicht, ob der linke Wert größer oder gleich dem rechten Wert ist. Beispiel: `10 >= 10` ergibt True.
- **Kleiner oder gleich (<=)**: Vergleicht, ob der linke Wert kleiner oder gleich dem rechten Wert ist. Beispiel: `4 <= 3` ergibt False.
- **Gleich (==)**: Vergleicht, ob die beiden Werte gleich sind. Beispiel: `5 == 5` ergibt True.
- **Ungleich (!=)**: Vergleicht, ob die beiden Werte ungleich sind. Beispiel: `3 != 7` ergibt True.

# Boolesche Algebra

In diesem Notebook werden wir die Boolesche Algebra in Python kennenlernen. Boolesche Algebra ist ein wichtiger Teil der Logik und wird in der Programmierung häufig verwendet.

## Boolesche Operatoren in Python

- **AND (und) - and**: Gibt True zurück, wenn beide Operanden True sind, andernfalls False.
- **OR (oder) - or**: Gibt True zurück, wenn mindestens einer der Operanden True ist, andernfalls False.
- **NOT (nicht) - not**: Kehrt den Wert des Operanden um. True wird zu False und False wird zu True.

## Wahrheitstabelle

Eine Wahrheitstabelle zeigt alle möglichen Kombinationen von Eingaben und das Ergebnis einer booleschen Operation. Hier ist eine Wahrheitstabelle für die AND-Operation:

| Eingabe A | Eingabe B | A AND B |
|-----------|-----------|---------|
| True      | True      | True    |
| True      | False     | False   |
| False     | True      | False   |
| False     | False     | False   |

# Bedingungen (if, else, elif)

In diesem Notebook werden wir die Verwendung von Bedingungen (if, else, elif) in Python kennenlernen. Bedingungen ermöglichen es uns, Codeblöcke nur dann auszuführen, wenn bestimmte Bedingungen erfüllt sind.

## Grundsyntax:

```python
if Bedingung:
    # Code wird ausgeführt, wenn die Bedingung wahr ist
else:
    # Code wird ausgeführt, wenn die Bedingung falsch ist
```

## Erweiterte Bedingungen mit `elif`:

Wir können auch `elif` verwenden, um zusätzliche Bedingungen zu überprüfen. Wenn die erste Bedingung falsch ist, aber die `elif`-Bedingung wahr ist, wird der zugehörige Codeblock ausgeführt.

```python
if Bedingung1:
    # Code wird ausgeführt, wenn Bedingung1 wahr ist
elif Bedingung2:
    # Code wird ausgeführt, wenn Bedingung1 falsch, aber Bedingung2 wahr ist
else:
    # Code wird ausgeführt, wenn keine der Bedingungen wahr ist
```

### Teilbarkeit

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

# Schleifen (while, for)

In diesem Notebook werden wir die Verwendung von Schleifen in Python kennenlernen. Schleifen ermöglichen es uns, Codeblöcke mehrmals auszuführen.


## while-Schleife:

# Schleifen (while, for)

In diesem Notebook werden wir die Verwendung von Schleifen in Python kennenlernen. Schleifen ermöglichen es uns, Codeblöcke mehrmals auszuführen.

## while-Schleife:

Eine while-Schleife wird verwendet, um einen Codeblock solange zu wiederholen, wie eine bestimmte Bedingung wahr ist. Die Bedingung wird vor jeder Iteration überprüft. Wenn die Bedingung wahr ist, wird der Codeblock ausgeführt. Wenn die Bedingung falsch ist, wird die Schleife beendet und die Ausführung wird fortgesetzt.

Die allgemeine Syntax einer while-Schleife in Python lautet:

```python
while Bedingung:
    # Code wird wiederholt ausgeführt, solange die Bedingung wahr ist
```

Hier ist ein einfaches Beispiel, das die Funktionsweise einer while-Schleife veranschaulicht:

```python
counter = 0
while counter < 5:
    print("Counter:", counter)
    counter += 1
```

In diesem Beispiel wird der Codeblock solange wiederholt, wie der Wert von `counter` kleiner als 5 ist. Bei jeder Iteration wird der Wert von `counter` um 1 erhöht und der aktuelle Wert von `counter` wird ausgegeben. Die Schleife wird beendet, wenn der Wert von `counter` 5 erreicht.

Die Ausgabe dieses Beispiels wäre:

```
Counter: 0
Counter: 1
Counter: 2
Counter: 3
Counter: 4
```

Die while-Schleife bietet eine flexible Möglichkeit, Codeblöcke zu wiederholen, solange eine bestimmte Bedingung erfüllt ist. Es ist wichtig sicherzustellen, dass die Bedingung irgendwann falsch wird, um eine Endlosschleife zu vermeiden.

## for-Schleife:

Eine for-Schleife wird verwendet, um einen Codeblock für jedes Element in einer Sequenz auszuführen. Die Sequenz kann eine Liste, ein Tupel, ein String oder ein anderer iterierbarer Datentyp sein.

Die allgemeine Syntax einer for-Schleife in Python lautet:

```python
for Element in Sequenz:
    # Code wird für jedes Element in der Sequenz ausgeführt
```

Hier ist ein einfaches Beispiel, das die Funktionsweise einer for-Schleife veranschaulicht:

```python
fruits = ["Apple", "Banana", "Orange"]
for fruit in fruits:
    print(fruit)
```

In diesem Beispiel wird der Codeblock für jedes Element in der Liste `fruits` ausgeführt. Das aktuelle Element wird in der Variablen `fruit` gespeichert und ausgegeben. Die Schleife wird beendet, wenn alle Elemente in der Sequenz verarbeitet wurden.

Die Ausgabe dieses Beispiels wäre:

```
Apple
Banana
Orange
```

Die for-Schleife ist besonders nützlich, wenn Sie eine bestimmte Aktion für jedes Element in einer Sequenz ausführen möchten.

