
# Função que gera um número aleatório de acordo 
# com o tamanho especificado

from random import randint

def gera_numero_conta(tamanho: int) -> int:
  return int(''.join([ str(randint(0, 9)) for _ in range(tamanho)]))


class ContaCorrente:

  def __init__(self, titular: str) -> None:
    self.numero: int = gera_numero_conta(7)
    self.titular: str = titular
    self._saldo: int = 0

  def consultar_saldo(self) -> str:
    return f'Saldo atual: R${self._saldo:_.2f}'

  def depositar(self, valor: float) -> None:
    self._saldo += valor

  def sacar(self, valor: float) -> str:
    if self._saldo - valor >= 0:
      self._saldo -= valor
      return f'Saque de R${valor:_.2f} realizado com sucesso'
    else:
      return f'Saldo insuficiente: R${self._saldo:_.2f}'

class ContaPoupanca(ContaCorrente):
  pass




