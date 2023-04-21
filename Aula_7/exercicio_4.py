#Fácil: Faça um programa que calcule a média aritmética de 4 notas e informe se o aluno foi aprovado (média maior ou igual a 7) ou reprovado.
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
nota4 = float(input("Digite sua quarta nota: "))

media =  ((nota1 + nota2 + nota3 + nota4) / 4 )

if media >= 7.0 and media <= 10.0:
    print("Aluno aprovado!")
    print(f'Sua média foi: {media}')
elif media < 7.0 and media >= 0.0:
    print("Aluno reprovado!")
    print(f'Sua média foi: {media}')
else:
    print("Valor incorreto!")