cidadao = {'Nome: ': 'Miguel', 'idade: ': '28 anos', 'cidade: ': 'Fortaleza'}

cidadao['idade'] = 30
cidadao['Profissao'] = 'Engenheiro Civil'
del cidadao['cidade: ']
cidadao['endereco'] = 'Rua 01'

print(cidadao)
if 'Nome: ' in cidadao:
    print('A chave está presente no dicionario')
else:
    print('A chave não está presente no dicionario')

numeros_quadrados = {x: x**2 for x in range(1, 11)}
print(numeros_quadrados)


frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos e vem crescendo cada vez mais com o desenvolvimento da IA Python tornou linguagens."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)