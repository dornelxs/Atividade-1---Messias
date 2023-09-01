estoque = [{
    'nome': 'maçã',
    'preço': 2.0,
    'quantidade': 5
}, {
    'nome': 'banana',
    'preço': 1.5,
    'quantidade': 10
}]
total = 0

for produto in estoque:
    preco = produto['preço']
    quantidade = produto['quantidade']
    valor_produto = preco * quantidade
    total += valor_produto

print(total)
