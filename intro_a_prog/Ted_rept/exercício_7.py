usuarios = []

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
email = input('Digite seu e-mail: ')

usuario = {'nome': nome, 'idade': idade, 'email': email}
usuarios.append(usuario)

print('Usuários cadastrados:')
for usuario in usuarios:
    print(f'Nome: {usuario["nome"]}, Idade: {usuario["idade"]}, E-mail: {usuario["email"]}')


