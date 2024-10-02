numero = input("Introdueixi 10 números separats per un espai: ")

numerosSeparats = numero.split()

numeros = []

for i in numerosSeparats:
    numeroInt = int(i)
    numeros.append(numeroInt)

if len(numeros) == 10:
    print(tuple(sorted(numeros)))
else:
    print("10 números!!!")
