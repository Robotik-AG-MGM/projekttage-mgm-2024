# Python-Funktionen erklärt

In  Python  sind Funktionen eine Möglichkeit, Code zu organisieren und wiederzuverwenden. Funktionen führen spezifische Aufgaben aus, wenn sie aufgerufen werden. Hier sind die Grundlagen, die Schüler über  Python-Funktionen wissen sollten:

## Was sind Funktionen in  Python?

-   **Funktionen**  sind benannte Codeblöcke, die eine spezifische Aufgabe ausführen, wenn sie aufgerufen werden.
-   Sie helfen dabei, Code zu strukturieren, zu organisieren und wiederzuverwenden.

## Funktionen definieren

Um eine Funktion in  Python  zu definieren, verwenden Sie das Schlüsselwort  `def`, gefolgt vom Funktionsnamen und den Klammern  `()`.

Beispiel:


```python
def begrüßung():
    print("Hallo! Willkommen zur Python-Welt.")
    
```

## Funktionen aufrufen

Um eine Funktion aufzurufen, geben Sie einfach den Funktionsnamen gefolgt von Klammern  `()`  ein.

Beispiel:


```python
gruss()

```

## Funktionen mit Parametern

Funktionen können auch Parameter akzeptieren, die ihnen helfen, spezifische Daten zu verarbeiten.

Beispiel:


```python
def sag_hallo(name: str) -> None:
    print("Hallo,", name, "!")

```

Aufruf der Funktion mit einem Parameter:


```python
sag_hallo("Max")

```

## Funktionen mit Rückgabewerten

Funktionen können auch Werte zurückgeben, die von anderen Teilen des Codes verwendet werden können.

Beispiel:


```python
def verdopple_zahl(zahl: int) -> int:
    return zahl * 2

```

Aufruf der Funktion und Speichern des Rückgabewerts:


```python
ergebnis = verdopple_zahl(5)
print(ergebnis)  # Ausgabe: 10

```
