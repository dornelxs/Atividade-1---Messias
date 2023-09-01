#Fácil: Crie um programa que solicite o nome e a idade do usuário e informe se ele pode dirigir um veículo
print("Digite seu nome e depois sua idade para comprovarmos que você está apto a dirigir")
nome = input("Digite seu nome: ")
idade = int(input("Agora digite sua idade: "))
if idade >= 18:
    print("Você está apto para dirigir!")
else:
    print("Você não está apto para dirigir!")