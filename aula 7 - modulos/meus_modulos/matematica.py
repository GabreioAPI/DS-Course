'''
Este é um modulo que contém funções para trabalhar com numeros
* calcula_percentual
* divide_dois
* fatorial
* media
* multiplica_dois
* par_ou_impar
* potencia
* quantos_porcento
* soma_dois
* subtrai_dois
'''
def calcula_percentual(num):
    pass

def divide_dois(num1,num2):
    return num1/num2

def fatorial(num):
    resultado = 1
    contador = 1

    while contador <= num:
        resultado *= contador
        contador += 1

    return resultado

def media():
    pass

def multiplica_dois(num1,num2):
    return num1*num2

def par_ou_impar(num):
    if num % 2 == 0:
        return 'Par'
    else:
        return 'Impar'

def potencia(num1,num2):
    return pow(num1,num2)

def quantos_porcento(num1,num2):
    resultado22 = ((num2*100)/num1)
    return resultado22

def soma_dois(num1,num2):
    return num1+num2

def subtrai_dois(num1,num2):
    return num1-num2