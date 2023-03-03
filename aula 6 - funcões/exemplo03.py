def produzir_roupa(peca: str = 'Camiseta', tamanho: str = 'M', 
                   cor: str = 'Branca') -> str:
  print(f'{peca} {cor} - Tamanho: {tamanho}')


# Se quisermos omitir um argumento, devemos passar os demais nomeados
# produzir_roupa(tamanho='P', cor='Preta')
# produzir_roupa('Saia', 'PP')
     