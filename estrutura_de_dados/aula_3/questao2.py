class Graus:
    def __init__(self, celsius, fahrenhit):
        self.celsius = celsius
        self.fahrenhit = fahrenhit

    def convert(self):
        self.fahrenhit = ((self.celsius * 1.8) + 32)
        print(f'Em graus Celsius: {self.celsius:.2f}ºC.\nEm Fahrenhit: {self.fahrenhit:.2f}ºF.')
        return self.fahrenhit

grau = Graus(36, 0)
grau = grau.convert()