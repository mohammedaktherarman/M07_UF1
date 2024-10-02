assignatures  = ["Mates", "Catalan", "Castellano", "Ingles", "Tecno", "Bio"]
print(assignatures)
notas = input("indiqui les notes de cada assignatura separats amb espais en ordre: ")

notasSeparats = notas.split()

numerosfinal = []

for i in notasSeparats:
    notaInt = int(i)
    numerosfinal.append(notaInt)

for i in range(len(assignatures)):
    print(f"A {assignatures[i]} ha tret {numerosfinal[i]}")

