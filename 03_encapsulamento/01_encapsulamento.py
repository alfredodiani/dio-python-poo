class Conta:
    def __init__(self, numero_agencia, saldo):
        self._saldo = saldo
        self.numero_agencia = numero_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def get_saldo(self):
        return self._saldo

conta = Conta(4001, 100)
conta.depositar(50)
print(conta.get_saldo())