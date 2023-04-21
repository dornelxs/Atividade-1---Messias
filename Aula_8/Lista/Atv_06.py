produtos = [{
    'nome' : 'laranja',
    'preço' : 0.99,
    'quantidade' : 20,
} ,
    { 'nome': 'limão',
    'preço' : 3,
    'quantidade' : 5
}]

for produto in produtos:
    preco = produto['preço']
    quantidade = produto['quantidade']
    valor_produto = preco * quantidade
    valor_total = valor_produto

print(valor_total)