myDict = {}
input1 = ""

while input1 != "para":
    input1 = input("Nom (o escriu 'para' per aturar): ")

    if input1 == "para":
        break

    if input1 in myDict:
        print(f"El nom {input1} ja existeix, no s'afegirà al diccionari.")
        continue

    input2 = input("Edat:")
    myDict[input1] = int(input2)

print(myDict)
