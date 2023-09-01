#1. Crie uma classe chamada “Circulo” que tenha um atributo “raio”. Implemente um método chamado
#“calcular_area” que retorna a área do círculo

import math


class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        area = math.pi * self.raio ** 2
        return area


raio_do_circulo = 5
circulo1 = Circulo(raio_do_circulo)

area_do_circulo = circulo1.calcular_area()

print(f'O raio do círculo é {circulo1.raio} e a aréa do círculo é {area_do_circulo:.2f}')

