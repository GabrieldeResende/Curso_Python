import contas
import pessoas

class Banco:
    def __init__(
            self, agencias: list[int] | None = None, 
            clientes: list[pessoas.Pessoas] | None = None, 
            contas: list[contas.Conta] | None = None
            ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checaAgencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _checaCliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False

    def _checaConta(self, conta):
        if conta in self.contas:
            return True
        return False

    def autenticar(self, cliente: pessoas.Pessoas, conta: contas.Conta):
        return self._checaAgencia(conta) and self._checaCliente(cliente) and self._checaConta(conta)
    

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    cliente1 = pessoas.Cliente("Gabriel", 25)
    contaCorrente1 = contas.ContaCorrente(111, 222, 0, 100)
    cliente1.conta = contaCorrente1

    cliente2 = pessoas.Cliente("Maria", 60)
    contaPoupanca2 = contas.ContaPoupanca(111, 222, 100)
    cliente2.conta = contaPoupanca2

    banco = Banco()
    banco.clientes.extend([cliente1, cliente2])
    banco.contas.extend([contaCorrente1, contaPoupanca2])
    banco.agencias.extend([111, 222])
    print(banco.autenticar(cliente1, contaPoupanca2))
    print(banco)
