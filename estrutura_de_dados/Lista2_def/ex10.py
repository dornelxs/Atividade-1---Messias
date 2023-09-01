#10. Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um
#método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário
#do funcionário.

class Funcionario:

    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self):
        aumento = (((self.salario * 20) / 100) + self.salario)
        return aumento

    def detalhes(self):
        print(f'Nome: {self.nome}\n'
              f'Cargo: {self.cargo}\n'
              f'Salário: R$ {self.salario:.2f}')


funcionario1 = Funcionario('Sofia Shararra Kettlhy', 600, 'Bolsista')

funcionario1.detalhes()
print(f'Aumento salarial de 20%\n'
      f'Salário atual: R${funcionario1.aumentar_salario():.2f}')