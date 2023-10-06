def ordenar_vetor(vetor, crescente=True):
    vetor.sort(reverse=not crescente)

vetor = [64, 25, 12, 22, 11]
ordenar_vetor(vetor, crescente=False)
print(vetor)
