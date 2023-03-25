nota1 = float(input("Digite sua primeira nota:"))
nota2 = float(input("Digite sua segunda nota:"))
media =  ((nota1 + nota2) / 2 )

if media >= 6.0 and media <= 10.0:
    print("Auno aprovado!")
    print(f'Sua média foi: {media}')
elif media < 6.0 and media >= 0.0:
    print("Aluno reprovado!")
    print(f'Sua média foi: {media}')
else:
    print("Valor incorreto!")


