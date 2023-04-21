numeros = [10, 2, 7, 3, 9, 4, 1, 5, 6, 8]
maior_numero = numeros[0]
menor_numero = numeros[0]

for num in numeros:
    if num > maior_numero:
        maior_numero = num
    if num < menor_numero:
        menor_numero = num

print("O maior número é:", maior_numero)
print("O menor número é:", menor_numero)
