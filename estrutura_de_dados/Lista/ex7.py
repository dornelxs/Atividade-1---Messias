a, b = 0, 1

numero = int(input("Digite o número máximo da sequência de Fibonacci: "))

while a <= numero:
    print(a)
    a, b = b, a + b