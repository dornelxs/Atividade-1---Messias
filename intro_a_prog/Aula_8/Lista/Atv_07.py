#Dado duas listas, crie um algoritmo que retorne a interseção dos elementos das duas listas (ou seja, os
#elementos que aparecem nas duas listas).
#Exemplo de entrada: [1, 2, 3, 4], [3, 4, 5, 6]
#Saída esperada: [3, 4

paises = {
        'Brasil': ['São Paulo', 'Rio de Janeiro', 'Paraíba'],
        'EUA': ['Los Angelos', 'Nova Iorque', 'São Francisco'],
        'Espanha': ['Milão', 'Madri', 'Barcelona']
}

cidade_m_p = {}

for p in paises:
        cidade = paises[p][0]
        cidade_m_p[p] = cidade
print(cidade_m_p)