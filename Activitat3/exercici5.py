frase = input("Frase:")
frase2 = frase.replace(" ", "")

tupla = (frase2)

fraseResposta = ""
for caracter in frase2:
    if caracter not in fraseResposta:
        fraseResposta = fraseResposta + caracter

print(tupla)
print(fraseResposta)
