areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

print("Imprimir el segon elemente:\n", areas_pis[1])

print("Imprimir l’últim element:\n", areas_pis[-1])

print("Imprimir l’àrea de la terrassa:\n", areas_pis[areas_pis.index("Terrassa") + 1])

print("Imprimir del primer element al tercer element:\n", areas_pis[0:6])

print("Imprimir del tercer element a l’últim:\n", areas_pis[2:])

indexHab1 = areas_pis.index("Habitació1") + 1
indexHab2 = areas_pis.index("Habitació2") + 1
total = float(areas_pis[indexHab1]) + float(areas_pis[indexHab2])
print("Imprimir el total de l'àrea de les dues habitacions:\n", total)

valorLavabo= areas_pis.index("Lavabo") + 1
valorLavaboNou = 10
areas_pis[valorLavabo] = valorLavaboNou
print("Modificar l’àrea del lavabo i imprimir la nova list area:\n", areas_pis)

areas_pis.append("Pati interior")
areas_pis.append(2.78)
print(f"Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area:\n", areas_pis)

index1 = float(areas_pis.index("Habitació1") + 1)
index2 = float(areas_pis.index("Habitació2") + 1)
index3 = float(areas_pis.index("Menjador") + 1)
index4 = float(areas_pis.index("Rebedor") + 1)
index5 = float(areas_pis.index("Terrassa") + 1)
index6 = float(areas_pis.index("Lavabo") + 1)
index7 = float(areas_pis.index("Cuina") + 1)
index8 = float(areas_pis.index("Pati interior") + 1)
total = index1 + index2 + index3 + index4 + index5 + index6 + index7 + index8
print("Imprimir el total de l’àrea del pis:\n", total)