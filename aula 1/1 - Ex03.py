#Exemplo 3
cont = 1
media = 0

while(cont<=4):
    nota = float(input(f'Informe a {cont}º nota:'))
    media = media + nota
    cont = cont + 1

media = media / 4
print(f'Media = {media:.2f}')
