pares = 0
spares = 0

lista = [20, 5, 9, 13, 12, 2, 8, 23]

for numero in lista:
    if numero % 2 == 0:
        print(f'Os números pares são: {numero}')
        spares += numero
        pares += 1

media = spares / pares

print(f'A média dos números pares é: {media}')