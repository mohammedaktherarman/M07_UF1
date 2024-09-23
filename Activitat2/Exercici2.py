valor = int(input("introdueixi un valor en €:"))
iva = int(input(" introdueixi el IVA a aplicar-hi (4%, 10% o 21%):"))

while iva != 4 and iva != 10 and iva != 21:
    print("El iva no es correcte")
    iva = int(input(" introdueixi el IVA a aplicar-hi (4%, 10% o 21%):"))

if iva == 4 or iva == 10 or iva == 21 :
    calcul = valor * iva
    calcul2 = calcul/100
    total = valor + calcul2

print(f"valor intruduit {valor}€")
print(f"iva intruduit {iva}%")
print(f"calcul intruduit {total}€");