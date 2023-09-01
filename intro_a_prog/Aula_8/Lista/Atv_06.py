#Dado uma lista de dicionários, onde cada dicionário representa um produto com as chaves "nome",
#"preço" e "quantidade", crie um algoritmo que retorne o valor total do estoque.
#Exemplo de entrada: [{'nome': 'maçã', 'preço': 2.0, 'quantidade': 5}, {'nome': 'banana', 'preço': 1.5,
#'quantidade': 10}]. Saída esperada: 25.0

produtos = [{
    'nome' : 'laranja',
    'preço' : 0.99,
    'quantidade' : 20,
} ,
    { 'nome': 'limão',
    'preço' : 3,
    'quantidade' : 5
}]

total = 0

for produto in produtos:
    preco = produto['preço']
    quantidade = produto['quantidade']
    valor_produto = preco * quantidade
    total += valor_produto

print(total)

