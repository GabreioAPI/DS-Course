letra = input('Informe uma letra: ').strip()
letra = letra.lower()

vogais = ('a','e','i','o','u')

if letra.isalpha():
    if letra in vogais:
        print(f'{letra} é uma vogal')
    else:
        print(f'{letra} é uma  consoante')
else:
    print('Inválido')

     

