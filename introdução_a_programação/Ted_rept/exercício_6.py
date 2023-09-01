convidados = ['Neymar', 'Blue Pen', 'Augustinho Carrára', 'Ednaldo Pereira', 'Jailson Mendes',]

for convidado in convidados:
    print(f'Olá {convidado}, venho através desse convite lhe chamar para comparecer a PH para celebrarmos o aniversário do nosso ilustre Vetin777!')

convidados_impossibilitados = ['Neymar']
for convidado_impossibilitado in convidados_impossibilitados:
    convidados.remove(convidado_impossibilitado)
    print()
    print(f'A notícia é triste mas devo informar que o {convidado_impossibilitado} não poderá comparecer pois estará viajando.')
    print()

novos_convidados = ['Salsicha', 'Scooby-Doo']
for novo_convidado in novos_convidados:
    convidados.append(novo_convidado)

for convidado in convidados:
    print(f'Olá {convidado}, você está sendo convidado para o festejar o aniversário do Vetin777 na PH!')


