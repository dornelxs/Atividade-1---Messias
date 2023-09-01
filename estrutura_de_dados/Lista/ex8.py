def e_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    raiz = int(n ** 0.5) + 1
    for divisor in range(3, raiz, 2):
        if n % divisor == 0:
            return False
    return True


numero = int(input("Digite o número que você deseja saber se é primo: "))

if e_primo(numero):
    print(f'O número {numero} é primo.')
else:
    print(f'O número {numero} não é primo.')
