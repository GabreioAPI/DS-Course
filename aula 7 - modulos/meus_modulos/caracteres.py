'''
Este é um modulo que contém funções para trabalhar com strings
* conta_consoantes
* conta_vogais
* eh_palindromo
* tem_maiusculas
* tem_minusculas
'''

def conta_consoante(var):
    var = var.replace(' ','')
    cont = 0
    vogais = ('aeiou')
    for x in var:
        if x not in vogais:
            cont = cont + 1
    return cont

def conta_vogais(var):
    var = var.replace(' ','')
    cont = 0
    vogais = ('aeiou')
    for x in var:
        if x in vogais:
            cont = cont + 1
    return cont

def eh_palindromo(var):
    if (var == var[:: -1]):
        return 'É palindromo'
    else:
        return 'Não é palindromo'

def tem_maiusculas(var):
    var = var.replace(' ','')
    cont = 0
    for x in var:
        if x.isupper():
            cont = cont + 1
    return cont

def tem_minusculas(var):
    var = var.replace(' ','')
    cont = 0
    for x in var:
        if x.islower():
            cont = cont + 1
    return cont