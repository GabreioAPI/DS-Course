dados = {}
notas = []

print()
dados['Nome'] = input(f'Informe o nome: ').strip().title()

for aux in range(1,5,1):
    nota = float(input(f'\nInforme a {aux}º nota: '))
    notas.append(nota)
 
media = sum(notas)/len(notas)

dados['Notas'] = notas
dados['Media'] = round(media,2)
dados['Maior_Nota'] = max(notas)
dados['Menor_Nota'] = min(notas) 

if media >=7 :
    dados['Situação'] = 'Aprovado'
elif media >=5 and media <7:
    dados['Situação'] = 'Recuperação'
else:
    dados['Situação'] = 'Reprovado'

print('------------------------------------------------------------')    
for dicionario in dados.items():
    chave, valor = dicionario
    print(f'{chave} : {valor}')
print('------------------------------------------------------------') 
