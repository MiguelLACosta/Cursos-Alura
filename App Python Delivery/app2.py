print('Python na Escola de Programação Alura')
#Print padrão
minha_idade = input('Digite a sua idade:')
meu_nome = input('Digite o seu nome:')
# Definição de variáveis para chamarmos no print abaixo
print(f'Meu nome é {meu_nome} e tenho {minha_idade} anos')
print('A','L','U','R','A',sep='\n')
# Podemos colocar o \n depois de cara letra, ou utilizar o sep=\n para colocar o \n entre cara item
pi = 3.14159
# Para a função rodar, temos que antes definir o valor de Pi (definir o valor da variável)
print(f'O valor arredondado de pi é: {pi:.2f}')
# Abordagem utilizando o f-string
print('O valor arredondado de pi é:', round(pi, 2))
# Abordagem utilizando a função round()