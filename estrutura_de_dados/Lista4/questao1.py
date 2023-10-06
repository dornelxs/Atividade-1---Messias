def ordenar_selecao(vetor):
    for i in range(len(vetor)):
        min_index = i
        for j in range(i+1, len(vetor)):
            if vetor[j] < vetor[min_index]:
                min_index = j
        vetor[i], vetor[min_index] = vetor[min_index], vetor[i]

vetor = [64, 25, 12, 22, 11]
ordenar_selecao(vetor)
print(vetor)
