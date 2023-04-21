nomes = ["duda", "chris", "duda", "chris", "carvalho", "dilba"]

nomes_n_duplicados = []

for nome in nomes:
    if nome not in nomes_n_duplicados:
        nomes_n_duplicados.append(nome)

print(nomes_n_duplicados)