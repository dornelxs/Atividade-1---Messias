def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

frase = input("Digite uma frase: ")
quantidade = contar_vogais(frase)
print(f"A frase possui {quantidade} vogais.")
