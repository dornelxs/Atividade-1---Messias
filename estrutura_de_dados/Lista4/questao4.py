def segundo_menor(vetor):
    vetor = list(set(vetor))
    if len(vetor) < 2:
        return None
    vetor.sort()
    return vetor[1]

vetor = [64, 25, 12, 22, 11, 12, 25]
segundo = segundo_menor(vetor)
print(f"O segundo menor número é: {segundo}")
