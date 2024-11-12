import os
print('Olá, por favor me diga o seu nome e sua idade e como você prefere ser chamado')
nome = input('Qual o seu nome?')
idade = int(input('Qual a sua idade?'))
nome2 = input('Você prefere ser chamado de:')

if 0 < idade < 12:
    print('Você é uma criança')
elif idade < 18:
    print('Você é adolecente')
elif idade < 60:
    print('Você é adulto')
elif idade >= 60:
    print('Você é idoso')
else:
    print('Número inválido')

print('Seu nome é',nome,',você tem',idade,'anos e prefere ser chamado de',nome2)