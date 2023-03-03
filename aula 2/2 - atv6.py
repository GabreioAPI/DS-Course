print('\n=============================================================')
print('                       Calculadora                           \n')
print(' + -> Soma   - -> Subtração   *-> Multiplicação    /-> Divisão')
print('=============================================================\n')
    
n1 = float(input('Informe o primeiro numero: '))
n2 = float(input('Informe o segundo numero: '))

operacao = input('\nQual operação deseja realizar: ')


if operacao =='+':
    resultado = n1 + n2

elif operacao == '-':
    resultado = n1 - n2

elif operacao == '*':
    resultado = n1 * n2

elif operacao == '/':
    resultado = n1 / n2

else:
    print('Operação inválida')


print(f'\nResultado = {resultado}',end=' ->')

if resultado >= 0:   
    print(' positivo',end=',')
else:
    print(' negativo',end=',')

if resultado % 2 == 0:
    print(' par',end=',')
else:
    print(' impar',end=',')

tipo = resultado.is_integer()

if tipo == True:
    print('inteiro.')
else:
    print('float.')

print('=============================================================\n')