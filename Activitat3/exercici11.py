divises = {
    "Euro": "€",
    "Dolar": "$",
    "Lliura": "£",
    "Ien": "¥",
}

input = input("Introdueix una divisa tenim Euro, Dolar, Lliura, Ien):")

if input in divises:
    print(f"El símbol de {input} és: {divises[input]}")
else:
    print("No tenim la divisa.")
