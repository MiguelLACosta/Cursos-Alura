lista_numeros = [1,2,3,4,5,6,7,8,9,10]

print(f'Lista {lista_numeros}')

for numero in lista_numeros:
    print(f'Numero {numero}')
    #A variavel numero é reconhecida mesmo sem ter sido nomeada

soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)

for i in range(10, 0 , -1):
    print(i)
