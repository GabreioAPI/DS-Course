
# Função que gera um número aleatório de acordo 
# com o tamanho especificado

from random import randint

def gera_numero_conta(tamanho: int) -> int:
  return int(''.join([ str(randint(0, 9)) for _ in range(tamanho)]))


class ContaCorrente:

  def __init__(self, titular: str) -> None:
    self.numero: int = gera_numero_conta(7)
    self.titular: str = titular
    self.saldo: int = 0

  def consultar_saldo(self) -> str:
    return f'Saldo atual: R${self.saldo:_.2f}'

  def depositar(self, valor: float) -> None:
    self.saldo += valor

  def sacar(self, valor: float) -> str:
    if self.saldo - valor >= 0:
      self.saldo -= valor
      return f'Saque de R${valor:_.2f} realizado com sucesso'
    else:
      return f'Saldo insuficiente: R${self.saldo:_.2f}'


#PS C:\Users\aluno\gabreio> & c:/Users/aluno/gabreio/environment/Scripts/Activate.ps1
#(environment) PS C:\Users\aluno\gabreio> cd 'aula 8 - POO I'
#(environment) PS C:\Users\aluno\gabreio\aula 8 - POO I> python -i .\main.py
#c1 = ContaCorrente('Gabriel')
#c1.titular
#'Gabriel'
#c1.depositar(1_000_000)
#c1.sacar(500)
#'Saque de R$500.00 realizado com sucesso'
#c1.__dict__
#{'numero': 3649905, 'titular': 'Gabriel', 'saldo': 999500}




