nome = input('Digite seu nome: ')

pessoa = {
    'primeiro_nome': nome,
    'segundo_nome': 'Dornelas',
    'idade': 18,
    'cidade': 'Jõao Pessoa'
}


print(f'Primeiro Nome: {pessoa["primeiro_nome"]}')
print(f'Segundo Nome: {pessoa["segundo_nome"]}')
print(pessoa)