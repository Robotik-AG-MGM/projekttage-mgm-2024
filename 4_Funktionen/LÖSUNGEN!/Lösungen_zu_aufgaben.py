
## Lösungen zu Python-Funktionsaufgaben

1.  **Grundlegende Funktionen:**
    
    -   Funktion  `hallo_welt()`:
        
        
        
        ```python
        def hallo_welt():
            print("Hallo Welt!")
        
        hallo_welt()
        
        ```
        
2.  **Funktionen mit Parametern:**
    
    -   Funktion  `addiere(a, b)`:
        
        
        
        ```python
        def addiere(a, b):
            return a + b
        
        summe = addiere(3, 4)
        print(summe)  # Ausgabe: 7
        
        ```
        
3.  **Funktionen mit Rückgabewerten:**
    
    -   Funktion  `ist_positiv(zahl)`:
        
        
        
        ```python
        def ist_positiv(zahl):
            if zahl > 0:
                return True
            else:
                return False
        
        print(ist_positiv(-2))  # Ausgabe: False
        
        ```
        
4.  **Funktionen mit Bedingungen:**
    
    -   Funktion  `ist_teilbar(durch, zahl)`:
        
        
        
        ```python
        x = zahl / durch

    if type(x) == int:
        print(zahl,"ist durch",durch,"teilbar")
    else:
        print("Ist nicht teilbar :c")
        
        print(ist_teilbar(3, 9))  # Ausgabe: True
        
        ```
        
5.  **Funktionen mit Schleifen:**
    
    -   Funktion  `drucke_bis_zehn()`:
        
        
        
        ```python
        def drucke_bis_zehn():
            for i in range(1, 11):
                print(i, end=' ')
            print()
        
        drucke_bis_zehn()  # Ausgabe: 1 2 3 4 5 6 7 8 9 10
        ```