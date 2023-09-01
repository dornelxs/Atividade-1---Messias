nomes_a = []

qtd_nomes = int(input("Digite a quantidade de nomes que você deseja fornecer: "))

for n in range(qtd_nomes):
    nome = input("Digite um nome: ")
    if nome[0].lower() == 'a':
        nomes_a.append(nome)
print("Os nomes inseridos que começam com a letra 'A' foram: ", nomes_a)