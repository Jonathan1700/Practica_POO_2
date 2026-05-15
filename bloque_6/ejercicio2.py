contador = 1
while contador <= 10:
    print(contador)
    contador += 1


frutas = ["Pera", "Mandarina", "UVA"]
for indice, fruta in enumerate(frutas):
    print(indice, fruta)


pc = ["Procesador", "ram", "disco"]
for indice, Pc in enumerate(pc):
    print(indice, Pc)

cuadrados = [x**2 for x in range(1, 11) if x % 2 == 0 ]
print(cuadrados)


