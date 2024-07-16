# Aufgabe 1
kontakte = {"Max": "123456", "Anna": "654321", "Bernd": "987654"}
print(kontakte.get("Max"))
print(kontakte.get("Clara", "Nicht gefunden"))

# Aufgabe 2
nummern = list(kontakte.values())
nummern.sort()
print(nummern)

# Aufgabe 3
kontakte["Clara"] = "111111"
print(kontakte)
del kontakte["Max"]
print(kontakte)
kontakte["Anna"] = "000000"
print(kontakte)
