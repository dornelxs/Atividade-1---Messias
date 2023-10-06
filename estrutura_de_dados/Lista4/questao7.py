def terceiro_maior(vetor):
    vetor = list(set(vetor))
    if len(vetor) < 3:
        return None
    vetor.sort()
    return vetor[-3]

vetor = [64, 25, 12, 22, 11, 25, 64, 33]
terceiro = terceiro_maior(vetor)
print(f"O terceiro maior número é: {terceiro}")
