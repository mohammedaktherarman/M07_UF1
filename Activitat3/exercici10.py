abecedari = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

llistaNoMultipleDe3 = []

for i in range(len(abecedari)):
    posicio = i + 1
    if posicio % 3 != 0:
        llistaNoMultipleDe3.append(abecedari[i])

tupla = tuple(llistaNoMultipleDe3)

print("llista:", llistaNoMultipleDe3)
print("tupla", tupla)
