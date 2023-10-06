def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

opcao = input("Escolha a conversão (C para Celsius para Fahrenheit, F para Fahrenheit para Celsius): ")
temperatura = float(input("Digite a temperatura: "))

if opcao.upper() == "C":
    resultado = celsius_para_fahrenheit(temperatura)
    print(f"{temperatura}°C é igual a {resultado:.2f}°F")
elif opcao.upper() == "F":
    resultado = fahrenheit_para_celsius(temperatura)
    print(f"{temperatura}°F é igual a {resultado:.2f}°C")
else:
    print("Opção inválida.")