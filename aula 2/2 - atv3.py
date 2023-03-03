print('\n==========================================')
print(' M -> Masculino       F -> Feminimo        ')
print('==========================================')

sexo = input('\nInforme seu sexo: ')
sexo = sexo.upper()

if sexo =='F':
    print('Seu sexo é Feminino\n')
elif sexo =='M':
    print('Seu sexo é Masculino\n')
else:
    print('Sexo inválido\n')