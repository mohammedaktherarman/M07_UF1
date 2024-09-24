numero = int(input("introdueixi un número:"))
sumaTotal = 0

for i in range(1, numero+1):
    print(f"{sumaTotal} + {i} = {i+sumaTotal}")
    sumaTotal= sumaTotal + i