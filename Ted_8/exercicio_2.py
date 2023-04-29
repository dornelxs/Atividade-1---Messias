#2. Faça um algoritmo para ler 10 números e armazenar em um vetor VET, verificar e escrever se existem
#números repetidos no vetor VET e em que posições se encontram.

numeros = []

for i in range(10):
    numero = int(input(f'Digite o {i + 1}º número: '))
    numeros.append(numero)

repetidos = []
for i in range(len(numeros)):
    if numeros.count(numeros[i]) > 1 and numeros[i] not in repetidos:
        repetidos.append(numeros[i])
        print(f'O número {numeros[i]} aparece nas posições: ', end='')
        for j in range(len(numeros)):
            if numeros[j] == numeros[i]:
                print(j+1, end=' ')
        print('')

if not repetidos:
    print('Não há números repetidos no vetor.')
print(numeros)

