numeros = input("Posi 10 números separats per espais: ")

numerosSeparats = numeros.split()

numerosfinal = []

if len(numerosSeparats) == 10:
    for i in numerosSeparats:
        numero = int(i)
        numerosfinal.append(numero)

    suma_total = sum(numerosfinal)
    mitjana = suma_total / len(numerosfinal)

    print("Números de l'usuari:", numerosfinal)
    print("suma total:", suma_total)
    print("mitjana:", mitjana)
else:
    print("posa 10 numeros!!!")
