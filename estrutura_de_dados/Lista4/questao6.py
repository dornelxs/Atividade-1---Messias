def contar_pares_impares(vetor):
    vetor.sort(reverse=True)
    pares = sum(1 for num in vetor if num % 2 == 0)
    impares = sum(1 for num in vetor if num % 2 != 0)
    return pares, impares

vetor = [64, 25, 12, 22, 11]
pares, impares = contar_pares_impares(vetor)
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
