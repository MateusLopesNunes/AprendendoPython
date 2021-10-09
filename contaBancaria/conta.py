class Conta:
    def __init__(self, numero, titular, limite):
        self.numero = numero
        self.titular = titular
        self.__saldo = 3000
        self.limite = limite

    @property
    def saldo(self):
        self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        print("O saldo não pode ser alterado diretamente")

    def deposito(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        if self.__saldo > valor:
            self.__saldo -= valor
        else:
            print('Errro. O valor de saque é maior que o valor do saldo')

    def transferencia(self, destino, valor):
        self.__saldo -= valor
        destino.__saldo += valor

    def extrato(self):
        print(f"numero: {self.numero}, titular: {self.titular}, saldo: {self.__saldo}, limite: {self.limite}")