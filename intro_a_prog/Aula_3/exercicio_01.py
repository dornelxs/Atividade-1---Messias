idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Essa pessoa pode entrar na festa!")
elif idade > 16 and idade <= 18:
    print("Mostre sua carteira de identidade!")
else:
    print("Essa pessoa não pode entrar na festa!")