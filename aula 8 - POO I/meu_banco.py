
class ContaCorrente:
    def __init__(self,nome: str):
        self.titular = nome
        self.__saldo = 0
        self.extrato = []
    
    def __repr__(self):
        return self.titular

    def consultar_saldo(self):
        return f'seu saldo = R${self.__saldo}'
    
    def depositar(self,valor:float):
        self.__saldo += valor
        self.extrato.append(f'Deposito R${valor}')
        return f'R${valor} depositado com sucesso'

    def sacar(self,valor:float):
        if valor > self.__saldo:
            return f'Seu saldo é insuficiente'
        self.__saldo -= valor
        self.extrato.append(f'Saque R${valor}')
        return 'Saque realizado com sucesso' 

    def transferir(self,receptor:str, valor:float):
        self.sacar(valor)
        if self.sacar(valor) == 'Saque realizado com sucesso':
            receptor.depositar(valor)
            self.extrato.append(f'Transferência R${valor} para {receptor}')
            return f'R${valor} transferido com sucesso'
        return 'Saldo insuficiente para fazer a transferência'

    def imprimir_extrato(self):
        print(60*'=')
        print(23*' ','EXTRATO',23*' ')
        print(f'Titular -> {self.titular}')
        print(f'Saldo atual -> R${self.__saldo}\n')
        for i in self.extrato:
            print('-',35*' ','R$',i)
        print(60*'=')
