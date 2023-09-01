#6. Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um
#método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.total = 0

    def calcular_total(self):
        total = (self.preco * self.quantidade)
        return total

    def informacoes(self):
        print(f'Produto: {self.nome}\n'
              f'Valor: R$ {self.preco:.2f}\n'
              f'Quantidade: {self.quantidade} unidades')


total1 = Produto('Maça', 3.50, 5)

total1.calcular_total()
total1.informacoes()
