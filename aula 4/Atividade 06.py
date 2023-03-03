vendedores = []
vendas = []
relatorio = []

for _ in range(4):
    vendedor = input('\nInforme o seu nome: ')
    venda = float(input('Informe a sua venda: R$'))

    vendedores.append(vendedor)
    vendas.append(venda)

relatorio = list(zip(vendas,vendedores))
relatorio.sort(reverse=True)

print('-' * 40)
print(f'\nO {relatorio[0][1]} foi o que mais vendeu')
print(f'Vendas ->R${relatorio[0][0]}')
print('-' * 40)
print(f'\nO {relatorio[1][1]} foi o segundo que mais vendeu')
print(f'Vendas ->R${relatorio[1][0]}')
print('-' * 40)
