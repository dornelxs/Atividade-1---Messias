# Lista de frutas
frutas = ["pêra", "uva", "maçã", "kiwi"]
print(f'{frutas}')
# Alterando o elemento que está na posição 1
frutas[1] = "abacate"
print(f'{frutas}')

frutas.insert(2, 'morango')
print(f'{frutas}')

frutas.insert(5, 'chuchu')
print(f'{frutas}')
del frutas[5]
print(f'{frutas}')

frutas.insert(5, 'melancia')
print(f'{frutas}')
print(f'O que é o frutas.index {frutas.index("melancia")}')
del frutas[frutas.index('melancia')]
print(f'{frutas}')

frutas.remove('kiwi')
print(f'{frutas}')

frutas.insert(10, 'ameixa')
print(f'{frutas}')

indice_frutas = (frutas.index('abacaxi'))
pop_fruta = frutas.pop(indice_frutas)