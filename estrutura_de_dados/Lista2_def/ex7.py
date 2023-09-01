#7. Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. Implemente um método
#chamado “detalhes” que retorna uma string com as informações do carro

class Carro:
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano

    def detalhes(self):
        print(f'Modelo do carro: {self.modelo}\n'
              f'Marca: {self.marca}\n'
              f'Ano de fabricação: {self.ano}')


carro1 = Carro('Urus', 'Larborghini', '2022-2023')

carro1.detalhes()