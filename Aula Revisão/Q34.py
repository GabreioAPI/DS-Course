'''
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.

'''

notas = []
cont = 0

for aux in range(5):
    nota1 = float(input('\nInforme a 1° nota: '))
    nota2 = float(input('Informe a 2° nota: '))
    nota3 = float(input('Informe a 3° nota: '))
    nota4 = float(input('Informe a 4° nota: '))

    media = (nota1 + nota2 + nota3 + nota4)/4
    
    if media >= 7:
        cont = cont + 1

    notas.append(media)

print(f'\n{cont} alunos foram aprovados')
print(f'{len(notas)- cont} alunos foram aprovados')

