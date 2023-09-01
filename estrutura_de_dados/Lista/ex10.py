import random

import time

def ppt(n):
    if n == "Pedra":
        return 'Pedra'

    if n == "Papel":
        return 'Papel'

    if n == "Tesoura":
        return 'Tesoura'

    return None


escolha_user = input("Escolha Pedra, Papel ou Tesoura: ")
escolha_valida = ppt(escolha_user)

while ppt(escolha_user) is None:
    print("Escolha inválida. Tente novamente.")
    escolha_user = input("Escolha Pedra, Papel ou Tesoura: ")
    escolha_valida = ppt(escolha_user)

opcoes = ["Pedra", "Papel", "Tesoura" , "Pedra", "Papel", "Tesoura" , "Pedra", "Papel", "Tesoura"]
escolha_comp = random.choice(opcoes)

if escolha_valida == escolha_comp:
    resultado = "Empate"
elif (
        (escolha_valida == "Pedra" and escolha_comp == "Tesoura") or
        (escolha_valida == "Papel" and escolha_comp == "Pedra") or
        (escolha_valida == "Tesoura" and escolha_comp == "Papel")
):
    resultado = "Você venceu"
else:
    resultado = "O computador venceu!"

print(f'Você escolheu {escolha_valida}, o computador escolheu {escolha_comp}, {resultado}')

