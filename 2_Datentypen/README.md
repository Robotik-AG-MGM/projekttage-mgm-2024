# **Primitive Datentypen**

Hier ist der Spickzettel für `Datentypen` in Python 

## **1.1 Strings**
Strings können `Buchstaben`,`Zeichen` und `Zahlen` beeinhalten.
Sie dienen in Python hauptsächlich dafür Text darzustellen. Diese stehen in `"Anführungszeichen"`

Mit `Strings` kann man **<ins>NICHT</ins>** rechnen. Sollte man das tun, so reiht es die Wörter/Zahlen aneinander.

Um Dinge in Python anzuzeigen Verwenden wir `print()`
<p>z.B.:</p>

```python
print("Hello 10!")
```


## **1.2 Intenger**
Intenger können **<ins>NUR</ins>** `ganze Zahlen`beeinhalten und diese Schreibt man ohne Anführungszeichen.
Sie sind für das Rechnen in Python gemacht. Um es anzuzeigen, verwenden wir auch `print()`
<p>z.B.:</p>

```python
print(4 + 9)
```

Das Ergebnis wird `13`.

## **1.3 Float**
Floats sind `Kommazahlen`, mit ihnen kann man auch Rechnen. Sie stehen auch ohne Anführungszeichen.

<ins>`Floats` funktionieren genau so wie `Intenger`</ins>

## **1.4 Booleans**
Booleans haben **<ins>2</ins>** Werte:
**<p>True** und **False</p>**

# **Komplexe Datentypen**

## **2.1 Variablen**
Variablen speichern Werte. Man kann die Variablen beliebig benennen

z.B.:

```python
x = 3
y = "5"
```

Die Variable `x` speichert den `Intenger-Wert` 3

Die `y`speichert den `String-Wert` 5

## **2.2 Listen**
Listen funktionieren wie eine Variable, jedoch kann eine Liste mehrere Werte speichern. Die Liste kann man auch beliebig benennen. 

Für Listen verwendet man `[eckige Klammern]` (alt gr + 8)

z.B.:

```python
liste_x = [1,2,3,4]
```

## **2.3 Tuples**
Tuples sind wie `Listen`, man kann Werte speichern, die man nicht ändern kann. Tuples laufen schneller beim Rechnen. 

Tuples schreibt man in `(normalen Klammern)`

z.B.:

```python
tuple_x = (1,2,3,4)
```

## **2.4 Dictionaries**
Dictionaries sind wie `Listen und Tuples` aber jeder Wert speichert einen eigenen. Schreibt man in {geschwungenen Klammern}.


z.B.:

```python
dict_x = {"Alter": 43, "Name": "Tobi", "Job":"Busfahrer"}
```
Um den Wert "Alter" aufzurufen, schreiben wir `dict_x["Alter"]`

```python
dict_x = {"Alter": 13, "Name": "Fynn", "beschreibendesWort":"obdachlos"}
dict_x["Alter"]
```
