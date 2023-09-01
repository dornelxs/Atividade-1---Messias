def calculadora(num1, num2, op):
    if op == 1:
        # soma
        return num1 + num2
    elif op == 2:
        # subtração
        return num1 - num2
    elif op == 3:
        # multiplicação
        return num1 * num2
    elif op == 4:
        # divisão
        return  num1 // num2
    else:
        return 'Valor inválido!'

print(f'Somando dois números: {calculadora(10, 15, 1)}')
print(f'Subtraindo dois números: {calculadora(100, 15, 2)}')
print(f'Multiplicando dois números: {calculadora(8, 8, 3)}')
print(f'Dividindo dois números: {calculadora(500, 15, 4)}')
print(f'Errado: {calculadora(10, 15, 5)}')
