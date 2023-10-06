def remover_duplicatas(vetor):
    return list(set(vetor))

vetor = [1, 2, 2, 3, 4, 4, 5]
vetor_sem_duplicatas = remover_duplicatas(vetor)
print(vetor_sem_duplicatas)
