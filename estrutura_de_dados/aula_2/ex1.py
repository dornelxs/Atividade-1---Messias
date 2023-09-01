import time

def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma = soma + i
    return soma

def soma2(n):
    return (n * ( n + 1)) / 2

print(soma1(10))
print(soma2(10))

inicio = time.time()
resultado = soma1(100000)
termino = time.time()
execution_time = termino - inicio

print(f'O resultado foi de: {resultado}')
print(f'Tempo de iniciio: {inicio:.5f} segundos')
print((f'Tempo de termino: {termino:.5f} segundos'))
print(f'Tempo de execução: {execution_time:.10f} segundos')