'''
Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
'''

idades = []
alturas = []
aluno = {}
media = 0
cont = 0


for aux in range(5):
    idade = int(input(f'Informe a {aux+1} idade: '))
    altura = float(input(f'Informe a {aux+1} sua altura em cm: '))

    idades.append(idade)
    alturas.append(altura)

    media = media + altura

media = media / len(alturas)

for aux in range(len(idades)):
    aluno[aux] = idades[aux],alturas[aux]

for aux in range(len(idades)):
    if aluno[aux][0] > 13:
        if aluno[aux][1] < media:
            cont = cont + 1

print(f'Temos {cont} alunos com altura inferior a media de {media}')
