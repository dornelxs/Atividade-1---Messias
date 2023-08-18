mAltura = float('-inf')
meAltura = float('inf')
sHomem = 0
sMulher = 0


for pessoa in range(0, 2):
    genero = input("Digite seu gênero (M ou F): ")
    altura = float(input("Digite seu altura: "))

    mAlturah = sHomem / (2 - sMulher)
    
    if altura > mAltura:
        altura = meAltura

    if altura < meAltura:
        meAltura = altura

    if genero == 'M':
        sHomem += altura
    elif genero == 'F':
        sMulher += 1

sHomem = sHomem + 1
sMulher = sMulher +1


print('----------------------------------------------------------------------')
print('Maior altura:' , mAltura)
print('Menor altura' , meAltura)
print(f'Média da altura dos homens: {mAlturah: }')
print(f'Quantidade de mulheres: {sMulher:}')


