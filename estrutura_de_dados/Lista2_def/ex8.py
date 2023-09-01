#8. Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado
#“calcular_media” que retorna a média das notas do aluno.

class Aluno:
    def __init__(self, nome, nota1, nota2, nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = 0.0

    def calcular_media(self):
        self.media = (self.nota1 + self.nota2 + self.nota3) / 3
        return self.media

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'\nNota 1: {self.nota1}')
        print(f'Nota 2: {self.nota2}')
        print(f'Nota 3: {self.nota3}')
        print(f'Média: {self.media:.2f}')

    def resultado(self):
        if self.media >= 7:
            print('\nAluno(a) aprovado(a)!')
        else:
            print('Aluno(a) reprovado(a)!')


aluno1 = Aluno('Carol', 9.0, 8.0, 6.5)

aluno1.calcular_media()
aluno1.mostrar_dados()
aluno1.resultado()