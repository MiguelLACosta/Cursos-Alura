class Carro:
    carros =[]
    def __init__(self,modelo,cor,ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = int(ano)

carro_chevrolet = Carro('Cruze', 'Prata', '2024')

class Restaurante:
    restaurantes = []
    def __init__(self,nome,categoria,ativo,delivery,chefe):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.delivery = delivery
        self.chefe = chefe
        self.funcinando = False
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante_cookmaster = Restaurante('cookmaster','japonesa','ativado','com delivery','okarun')
print(restaurante_cookmaster)

class Cliente:
    def __init__(self,nome = '',idade = 0,telefone = 0,profissao = ''):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.profissao = profissao
    
    def __str__(self):
        return f'{self.nome}, {self.idade} anos, sou {self.profissao} e meu contato {self.telefone}'
    
    @property
    def saudacao(self):
        if self.profissao:
            return f' Ola, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Ola, sou {self.nome}! E tenho {self.idade} anos.'
    
    def aniversario(self):
        self.idade += 1

cliente1 = Cliente('Miguel', idade =28,telefone = 987263054,profissao='Engenheiro')
cliente2 = Cliente('Mario',idade = 62,telefone = 987635421,profissao='Medico')
cliente3 = Cliente('Galgani',idade = 55,telefone = 989458677)

print('Informações Iniciais:')
print(cliente1)
print(cliente2)
print(cliente3)

cliente1.aniversario()
cliente2.aniversario()
cliente3.aniversario()

print("Informações após aniversário:")
print(cliente1)
print(cliente3)


print(cliente1.saudacao)
print(cliente2.saudacao)
print(cliente3.saudacao)