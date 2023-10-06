def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))
imc = calcular_imc(peso, altura)

print(f"Seu IMC é {imc:.2f}")
