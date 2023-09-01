numeros = int(input("Digite um número para saber se é ímpar ou par: "))


for n in range(numeros + 1):
    if (n % 2 == 0):
        print(f'O número {n} é par.')