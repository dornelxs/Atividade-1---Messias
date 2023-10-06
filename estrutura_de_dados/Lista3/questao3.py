def eh_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    return texto == texto[::-1]

frase = input("Digite uma palavra ou frase: ")
if eh_palindromo(frase):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
