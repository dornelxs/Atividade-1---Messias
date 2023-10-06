def mediana(vetor):
    vetor.sort()
    meio = len(vetor) // 2
    if len(vetor) % 2 == 0:
        return (vetor[meio - 1] + vetor[meio]) / 2
    else:
        return vetor[meio]

vetor = [64, 25, 12, 22, 11]
mediana_valor = mediana(vetor)
print(f"A mediana é: {mediana_valor}")
