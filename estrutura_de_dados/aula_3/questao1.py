class IMC:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura


    def calculo(self):
        imc = ((self.peso / (self.altura**2)))
        print(f'Seu IMC é: {imc:.2f}')
        return imc


im1 = IMC(76.600, 1.82)
im2 = im1.calculo()