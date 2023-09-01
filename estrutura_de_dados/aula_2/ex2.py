class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0.0

    def calcular_media(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Nota 1: {self.nota1}')
        print(f'Nota 2: {self.nota2}')
        print(f'Média: {self.media:.2f}')

    def resultado(self):
        if self.media >= 7:
            print('Aluno(a) aprovado(a)')
        else:
            print('Aluno(a) reprovado(a)')

aluno1 = Aluno('Carol', 9.0, 8.0)
aluno2 = Aluno('Chris', 8.4, 9.1)
aluno3 = Aluno('Dilba', 6.9, 9.8)

aluno1.calcular_media()
aluno1.mostrar_dados()
aluno1.resultado()

