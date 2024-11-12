import os
print('Bem vindo!')
usuario_correto = 'Miguel'
senha_correta = 'Miguel123'
usuario = input('Insira o seu usuario:')
senha = input('Insura sua senha:')

if senha == senha_correta and usuario == usuario_correto:
    print('Log in concluido')
else:
    print('Log in falhou')