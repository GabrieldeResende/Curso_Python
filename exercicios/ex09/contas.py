import abc

class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo= 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo



    @abc.abstractmethod
    def sacar(self,valor):
        ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f"(Deposito: {valor})")


    def detalhes(self, msg =''):
        print(f'O seu saldo é: {self.saldo:.2f} {msg}')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valorPosSaque = self.saldo - valor

        if valorPosSaque >= 0:
            self.saldo -= valor
            self.detalhes(f"(Saque: {valor})")

            return self.saldo
        
        print("Não foi possivel sacar o valor desejado")
        self.detalhes(f"(Saque negado)")

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo = 0, limite = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite


    def sacar(self, valor):
        valorPosSaque = self.saldo - valor
        limiteMaximo = -self.limite

        if valorPosSaque >= limiteMaximo:
            self.saldo -= valor
            self.detalhes(f"(Saque: {valor})")

            return self.saldo
        
        print("Não foi possivel sacar o valor desejado")
        self.detalhes(f"(Saque negado)")

if __name__ == '__main__':
    contaPoupanca1 = ContaPoupanca(111, 222, 0)
    contaPoupanca1.depositar(1)
    contaPoupanca1.sacar(1)
    print('##')
    contaCorrente1 = ContaCorrente(111, 222, 0, 100)
    contaCorrente1.depositar(1)
    contaCorrente1.sacar(1)
    contaCorrente1.sacar(100)
    contaCorrente1.sacar(1)
    print('##')
