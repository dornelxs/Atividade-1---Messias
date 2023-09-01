#9. Crie uma classe chamada “Triangulo” com atributos “lado1”, “lado2” e “lado3”. Implemente um
#método chamado “calcular_perimetro” que retorna o perímetro do triângulo

class Triangulo:

    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3


    def calcular_perimetro(self):
        print(f'1º lado = {self.lado1}\n'
              f'2º lado = {self.lado2}\n'
              f'3º lado = {self.lado3}\n')
        perimetro = (self.lado1 + self.lado2 + self.lado3)
        print(f'Perimetro: {perimetro}')
        return perimetro


area = Triangulo(8, 7, 15)
area.calcular_perimetro()