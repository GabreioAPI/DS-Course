requesitos = ['Nome','Sobrenome','Idade','Email']
dicionario = dict.fromkeys(requesitos)

dicionario['Nome'] = input('Informe seu nome: ').title().strip()
dicionario['Sobrenome'] = input('Informe seu sobrenome: ').title().strip()
dicionario['Idade'] = int(input('Informe sua idade: '))
dicionario['Email']  = input('Informe seu email: ').lower().strip()

for pos, dados in enumerate(dicionario.items(),start = 1):
    chave, valor = dados
    print(f'\n{pos}: {chave} -> {valor}')
print()