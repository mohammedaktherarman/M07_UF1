numero = int(input("Un nùmero entre 10 i 100:"))

if numero>9 and numero<101 :
    tupla = tuple(range(1, numero + 1))
    print("La tupla dels números és:", tupla)
else :
    print("Numero entre 10 i 100!!!")





