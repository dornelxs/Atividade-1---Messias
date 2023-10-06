def encontrar_max_min(vetor):
    if len(vetor) == 0:
        return None, None

    max_elemento = vetor[0]
    min_elemento = vetor[0]

    for elemento in vetor:
        if elemento > max_elemento:
            max_elemento = elemento
        elif elemento < min_elemento:
            min_elemento = elemento

    return max_elemento, min_elemento

vetor = [64, 25, 12, 22, 11]
maximo, minimo = encontrar_max_min(vetor)
print(f"Elemento máximo: {maximo}")
print(f"Elemento mínimo: {minimo}")
