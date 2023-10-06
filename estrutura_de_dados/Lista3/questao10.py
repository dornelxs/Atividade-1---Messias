def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    return fib_sequence

num_termos = int(input("Digite o número de termos desejado: "))
if num_termos <= 0:
    print("Digite um número inteiro positivo.")
else:
    resultado = fibonacci(num_termos)
    print(f"A sequência de Fibonacci com {num_termos} termos é: {resultado}")