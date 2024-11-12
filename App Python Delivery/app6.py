import os
x = int(input('Insira o valor de X:'))
y = int(input('INsira o valor de Y'))

if x > 0 and y > 0:
    os.system('cls')
    print('Você está no 1 quadrante')
elif x < 0 and y > 0:
    os.system('cls')
    print('Você está no 2 quadrante')
elif x < 0 and y < 0:
    os.system('cls')
    print('Você está no 3 quadrante')
elif x > 0 and y < 0:
    os.system('cls')
    print('Você está no 4 quadrante')
else:
    os.system('cls')
    print('O ponto está localizado n oeixo ou origem')