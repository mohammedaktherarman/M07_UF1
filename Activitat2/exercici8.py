paraulesInput = input("Posa entre 1 i 3 paraules:")

paraules = paraulesInput.split()

if len(paraules) < 1 or len(paraules) > 3:
    print("Error tens que posa entre 1 i 3 paraules")
else:
    for paraula in paraules:
        print("\n")
        print(f"Paraula: {paraula}")
        print(f"quants caràcters té {len(paraula)}")
        print(f"primer caracter {paraula[0]}")
        print(f"ultim caracter {paraula[-1]}")
