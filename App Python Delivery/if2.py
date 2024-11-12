
dia_a = int(input('Quantidade de dias para tarefa A: '))
dia_b = int(input('Quantidade de dias para tarefa B: '))
dia_c = int(input('Quantidade de dias para tarefa C: '))

if dia_a < 0 or dia_b < 0 or dia_c < 0:
    print('Valor inválido')
else:
    total = dia_a + dia_b + dia_c
    print(f'A quantidade total de dias é: {total}')