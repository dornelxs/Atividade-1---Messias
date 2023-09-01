maior_valor = float("-inf")
menor_valor = float("inf")

lista = [20, 5, 9, 13, 17, 2, 15, 23]

for numero in lista:
    if numero > maior_valor:
        maior_valor = numero

    elif numero < menor_valor:
        menor_valor = numero

print(f'O maior número é: {maior_valor}')
print(f'O menor número é: {menor_valor}')