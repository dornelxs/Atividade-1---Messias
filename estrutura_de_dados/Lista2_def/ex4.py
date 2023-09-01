# 4. Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente
# métodos “depositar” e “sacar” para manipular o saldo.

class ContaBancaria:

    def __init__(self, titular, saldo,  deposito, saque):
        self.titular = titular
        self.saldo = saldo
        self.deposito = deposito
        self.saque = saque

    def depositar(self):
        self.saldo = self.saldo + self.deposito
        print(f'Titular da CC: {self.titular}. '
              f'\n-----------------------------------------------'
              f'\nSeu saldo atual na cc 147-8 é: R${self.saldo},00')
        return self.saldo

    def sacar(self):
        self.saque = self.saldo - self.saque
        print("-----------------------------------------------")
        print(f'Após realizar um saque de: R${self.saque},00. Seu saldo atual é de R${self.saldo - self.saque},00')
        return self.saque


saldo_e_titular = ContaBancaria('Christoff', 1000, 100, 600)

saldo_cc = saldo_e_titular.depositar()
saque_cc = saldo_e_titular.sacar()

