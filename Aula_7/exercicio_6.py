#Intermediário: Faça um programa que leia o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1500,00, o aumento é de 10%. Para salários inferiores ou iguais a R$1500,00, o aumento
# é de 15%.
S = float(input("Digite o valor do seu salário atual: "))

if S > 1500:
    aumento = S * 0.1
else:
    aumento = S * 0.15

ns = S + aumento

print(f'Seu novo salário é de: {ns}: ')