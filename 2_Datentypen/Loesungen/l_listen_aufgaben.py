# Aufgabe 1
wochentage = ["Montag",
              "Dienstag",
              "Mittwoch",
              "Donnerstag",
              "Freitag",
              "Samstag"]
print(wochentage)
wochentage.append("Sonntag")
print(wochentage)
wochentage[3] = "Doenerstag"
print(wochentage)
wochentage.remove("Doenerstag")
print(wochentage)

# Aufgabe 2
zahlen = [1, 5, 3, 9, 2]
m = max(zahlen)
k = min(zahlen)
d = sum(zahlen) / len(zahlen)
zahlen.append(4)
neuer_durchschnitt = sum(zahlen) / len(zahlen)
print(m, k, d, neuer_durchschnitt)

# Aufgabe 3
Namen = ["Anna", "Bernd", "Clara", "David"]
Namen.sort()
print(Namen)
Namen.append("Elena")
Namen.sort()
print(Namen)
Namen.remove("Bernd")
print(Namen)

# Aufgabe 4
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
element = matrix[1][2]
print(matrix[1][2])
matrix[2][2] = 99
print(matrix)
