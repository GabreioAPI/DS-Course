def situacao_do_aluno(nota1: float, nota2: float) -> tuple:
  media = (nota1 + nota2) / 2
  situacao = 'Aprovado' if media > 6.99 else 'Reprovado'
  
  return media, situacao