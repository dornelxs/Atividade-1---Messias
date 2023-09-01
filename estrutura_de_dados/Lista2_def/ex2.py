#2. Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método
#chamado “detalhes” que retorna uma string com as informações do livro.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        print(f'Título do livro: {self.titulo}')
        print(f'Autor(a) do livro: {self.autor}')


livro1 = Livro('Percy Jackson', 'Rick Riordan')

livro1.detalhes()

