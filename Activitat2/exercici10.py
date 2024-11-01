import random
numeroRandom = random.randint(1, 100)
jugades = 0
jugada = 0

while jugada != numeroRandom:
    jugada = int(input("Posa un numero entre 1 i 100:"))

    if jugada>numeroRandom:
        print("El numero es mes petit")
        jugades = jugades + 1
        print(f"Jugades fetes: {jugades}")

    if jugada<numeroRandom:
        print("El numero es mes gran")
        jugades = jugades + 1
        print(f"Jugades fetes: {jugades}")

print("Has encertat")

