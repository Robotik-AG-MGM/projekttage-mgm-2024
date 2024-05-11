## Python-Funktionsaufgaben

1.  **Grundlegende Funktionen:**
    
    -   Schreibe eine Funktion  `hallo_welt()`, die "Hallo Welt!" ausgibt.
        
        
        
        ```python
        def hallo_welt():
            print("Hallo Welt!")
        
        hallo_welt()
        
        ```
        
2.  **Funktionen mit Parametern:**
    
    -   Definiere eine Funktion  `addiere(a, b)`, die zwei Zahlen addiert und das Ergebnis zurückgibt.
        
        
        
        ```python
        def addiere(a, b):
            return a + b
        
        summe = addiere(3, 4)
        print(summe)  # Ausgabe: 7
        
        ```
        
3.  **Funktionen mit Rückgabewerten:**
    
    -   Erstelle eine Funktion  `ist_positiv(zahl)`, die überprüft, ob eine Zahl positiv ist und  `True`  oder  `False`  zurückgibt.
        
       
        
        ```python
        def ist_positiv(zahl):
            if zahl > 0:
                return True
            else:
                return False
        
        print(ist_positiv(-2))  # Ausgabe: False
        
        ```
        
4.  **Funktionen mit Bedingungen:**
    
    -   Schreibe eine Funktion  `ist_teilbar(durch, zahl)`, die prüft, ob eine Zahl durch eine andere teilbar ist.
        
       
        
        ```python
        def ist_teilbar(durch, zahl):
            if zahl % durch == 0:
                return True
            else:
                return False
        
        print(ist_teilbar(3, 9))  # Ausgabe: True
        
        ```
        
5.  **Funktionen mit Schleifen:**
    
    -   Definiere eine Funktion  `drucke_bis_zehn()`, die die Zahlen von 1 bis 10 ausgibt.
        
       
        
        ```python
        def drucke_bis_zehn():
            for i in range(1, 11):
                print(i, end=' ')
            print()
        
        drucke_bis_zehn()  # Ausgabe: 1 2 3 4 5 6 7 8 9 10
        ```