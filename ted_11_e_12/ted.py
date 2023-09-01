import csv

def maiorPublicoDosFilmes(filmes):
    cabecalho = next(filmes)
    totalPublico = 0
    nomeDoFilme = ''
    anoDeExibicao = ''

    for filme in filmes:
        coluna = float(filme[9])

        if coluna > totalPublico:
            totalPublico = coluna
            nomeDoFilme = filme[2]
            anoDeExibicao = filme[1]
        else:
            continue

    print('O filme com maior público foi: ', nomeDoFilme)
    print('O total do público: ', totalPublico)
    print('Ano da exibição: ', anoDeExibicao)

with open('filmes.csv', newline='', encoding='utf-8') as filmes:

    lerfilmes = csv.reader(filmes)

    maiorPublicoDosFilmes(lerfilmes)