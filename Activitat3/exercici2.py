tupla = tupla = ("Enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

numero = int(input("Posa un número entre 0 i 12:"))

while (numero != 0):

    if numero>0 and numero<13:
        print(tupla[numero-1])
    else:
        print("Posa un número entre 0 i 12!!!")

    numero = int(input("Posa un número entre 0 i 12:"))

print("Acabat")