#3. Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método
#chamado “calcular_area” que retorna a área do retângulo.

class Retangulo:
     def __init__(self, base, altura):
        self.base = base
        self.altura = altura

     def calcular_area(self):
        area = (self.base * self.altura)
        return area


diametro = Retangulo(5, 8)

area_do_retangulo = diametro.calcular_area()

print(f'A base do retângulo é: {diametro.base}cm, e a altura é: {diametro.altura}cm. '
      f'\nA área total do retângulo é {area_do_retangulo:.2f}cm')
