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

---
