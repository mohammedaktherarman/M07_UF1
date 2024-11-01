paraulesInput = input("Posa 2 paraules:")

paraules = paraulesInput.split()

paraula1 = paraules[0]
paraula2 = paraules[1]

if len(paraules) != 2:
    print("Error tens que posa 2 paraules:")
else:
    paraula1 = paraules[0]
    paraula2 = paraules[1]

    if len(paraula1) >= 2 and len(paraula2) >= 2:
        paraula3 = paraula2[:2] + paraula1[2:]
        paraula4 = paraula1[:2] + paraula2[2:]

        print(f"{paraula1} {paraula2} passaria a {paraula3} {paraula4}")