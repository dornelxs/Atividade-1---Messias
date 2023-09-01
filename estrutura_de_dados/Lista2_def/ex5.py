#5. Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”. Implemente um método
#chamado “falar” que imprime uma mensagem com o nome da pessoa

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'Olá {self.nome}, como vai você? fiquei sabendo que você completou {self.idade} anos recentemente,'
              f'\nmeus parabéns!!')


fala = Pessoa('Carvalho', 19)

fala1 = fala.falar()