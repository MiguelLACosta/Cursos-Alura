import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},{'nome':'Pizza Suprema', 'categoria':'Pizzaria','ativo':True},{'nome':'Cantina', 'categoria':'italiana','ativo':False}]

def exibir_nome_do_programa():
    '''Função para apresentar o nome do app'''
    print('''

┏━━━┓╋╋┏┓╋╋╋╋╋╋╋┏━━━┓
┃┏━┓┃╋╋┃┃╋╋╋╋╋╋╋┃┏━━┛
┃┗━━┳━━┫┗━┳━━┳━┓┃┗━━┳┓┏┳━━┳━┳━━┳━━┳━━┓
┗━━┓┃┏┓┃┏┓┃┏┓┃┏┛┃┏━━┻╋╋┫┏┓┃┏┫┃━┫━━┫━━┫
┃┗━┛┃┏┓┃┗┛┃┗┛┃┃╋┃┗━━┳╋╋┫┗┛┃┃┃┃━╋━━┣━━┃
┗━━━┻┛┗┻━━┻━━┻┛╋┗━━━┻┛┗┫┏━┻┛┗━━┻━━┻━━┛
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┃┃
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗┛''')
# Para escolhermos alguma letra diferenciada para colocar no programa, podemos acessar a pagina "FSymbols" no Google e pegar o modelo desejado
# O simbolo # é utilizado para fazermos comentários em Python
# A função '\n' é utilizada para pularmos uma linha, também podemos utilizar ' ou " triplas.
def voltar_ao_menu_principal():
    '''Função para ativar a tecla de retorno ao menu incial do app'''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def exibir_opcoes():
    '''Exibe as opções disponiveis'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alternar estado do Restaurante')
    print('4. Sair\n')
def finalizar_app():
    '''Mensagem de finalização do App'''
    exibir_subtitulo('Finalizando App')

def opcao_invalida():
    '''Essa função cria a saida caso o usuario escolha uma opção inválida'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função facilita a apresentação dos subtitulos e faz uma função estetica com *'''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()
    # os.system('clear) como utilizar esse comando no Mac
    
def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante
    Input: Nome do restaurante e categoria
    Output: Adiciona o novo restaurante com sua categoria a lista de restaurantes    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que quer cadastrar:\n')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:\n ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def lista_restaurantes():
    '''Essa função é responsável por listrar os restaurantes'''
    exibir_subtitulo('Lista dos restaurantes cadastrados')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status do Restaurante'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    '''Essa função é responsável por alternar o estado de ativado ou desativado do restaurante
    Outputs: mensagem de falha ou de conclusão do processo
    '''
    exibir_subtitulo('Alterar estado do resurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado  = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função nos apresenta as opções para escolhermos e também vincula a opção aos comandos
    
    Outputs: Executa a opção escolhida pelo usuário a depender no numero inserido
    '''
    try:
    # o Try está sendo utilizado caso o usuario insira algum valor não numerio o sistema reconheça como inválido e execute o 'except'
        opcao_escolhida = int(input('Escolha uma opção: '))
        # A função "int" transforma a varíavel em número inteiro
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            print('Cadastrar Restaurante')
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print('Listar Restaurante')
            lista_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            print('Finalizar app')
        else:
            opcao_invalida()
    except:
        # O except está sendo utilizado para dar ao programa o que fazer caso o que foi tentado fazer dentro do 'try' não dê certo
        opcao_invalida()
# Podemos utilizar o match para substituir o if elif else, e assim o codigo ficaria dessa forma abaixo:
#opcao_escolhida = int(input('Escolha uma opção: '))
#match opcao_escolhida:
#    case 1:
#        print('Adicionar restaurante')
#    case 2:
#        print('Listar restaurantes')
#    case 3:
#        print('Ativar restaurante')
#    case 4:
#        print('Finalizar app')
#    case _:
#        print('Opção inválida!')

def main():
    '''Essa função define como o programa prinncipal irá rodar, aqui que nós puxamos os programas principais definidos anteriormente'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

# Colocamos o 'f' dentro do print para o print identificar a string que está dentro dos {}