numero = int(input("Posa un número entre 1 i 10:"))

if numero>0 and numero<11:
    resultats = []

    for i in range(1, 11):
        resultats.append(numero * i)

    print(resultats)
else:
    print("Posa un número entre 1 i 10!!!")
