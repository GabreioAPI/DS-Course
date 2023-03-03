from random import randint

class Conta:
    def __init__(self,titular: str,senha: int):
        self.titular = titular
        self._senha = senha
        self._saldo = 0
        self.extrato = []
    
    def __repr__(self):
        return self.titular

    def consultar_saldo(self,password:int):
        if password == self._senha:
            return f'seu saldo = R${self._saldo}'
        return'Senha Incorreta. Tente novamente'
    
    def sacar(self,valor:float,password:int):
        if password == self._senha:
            if valor > self._saldo:
                return f'Seu saldo é insuficiente'
            self._saldo -= valor
            self.extrato.append(f'Saque R${valor}')
            return 'Saque realizado com sucesso' 
        return'Senha Incorreta. Tente novamente'
    
    def imprimir_extrato(self,password:int):
        if password == self._senha:
            print(60*'=')
            print(23*' ','EXTRATO',23*' ')
            print(f'Titular -> {self.titular}')
            print(f'_saldo atual -> R${self._saldo}\n')
            for i in self.extrato:
                print('-',15*' ','R$',i)
            print(60*'=')
        return'Senha Incorreta. Tente novamente'


class ContaCorrente(Conta):
    '''
    tem:
    - Consultar
    - Sacar
    - Imprimir extrato
    - transferir
    - depositar
    '''
    def depositar(self,valor:float,password:int):
        if password == self._senha:
            self._saldo += valor
            self.extrato.append(f'Deposito R${valor}')
            return f'R${valor} depositado com sucesso'
        return'Senha Incorreta. Tente novamente'

    def transferir(self,receptor:str, valor:float,password:int):
        if password == self._senha:
            if self.sacar(valor) == 'Saque realizado com sucesso':
                self.extrato.pop()
                receptor.depositar(valor)
                self.extrato.append(f'Transferência R${valor} para {receptor}')
                return f'R${valor} transferido com sucesso'
            return 'saldo insuficiente para fazer a transferência'
        return'Senha Incorreta. Tente novamente'

class ContaSalario(Conta):
    '''
    tem:
    - Consultar
    - Sacar
    - Imprimir extrato
    - transferir
    - pagamento
    '''
    def __init__(self, titular: str,conta_empregador: str,):
        super().__init__(titular)
        self.conta_empregador = conta_empregador

    def transferir(self,receptor:str, valor:float):
        nome = receptor.__repr__()
        if self.titular == nome:
            if self.sacar(valor) == 'Saque realizado com sucesso':
                self.extrato.pop()
                receptor.depositar(valor)
                self.extrato.append(f'Transferência R${valor} para {receptor}')
                return f'R${valor} transferido com sucesso'
            return '_saldo insuficiente para fazer a transferência'
        return 'Obrigatoriamente, você precisa ser o titular das duas contas para fazer a transferência '
    
    def pagamento(self,valor:float,emissor: str):
        if emissor == self.conta_empregador:
            self._saldo += valor
            self.extrato.append(f'Deposito R${valor}')
            return f'R${valor} depositado com sucesso'
        else:
            return f'Essa conta só pode receber valores da empresa {self.conta_empregador}'
        
        

    