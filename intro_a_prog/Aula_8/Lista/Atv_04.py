#Dado uma lista de strings, crie um algoritmo que retorne a lista de strings ordenada por ordem
#decrescente de tamanho.
#Exemplo de entrada: ['casa', 'carro', 'abacate', 'pipoca']
#Saída esperada: ['abacate', 'carro', 'casa', 'pipoca']

strings = ["Casa", "Amanda", "Alavanca", "Bola", "Bala", "Dado"]

for i in range(len(strings)):
    for j in range(i + 1, len(strings)):
        if len(strings[i]) < len(strings[j]):
            strings[i], strings[j] = strings[j], strings[i]

print(strings)

