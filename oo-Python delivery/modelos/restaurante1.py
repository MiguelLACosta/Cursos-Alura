class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'italiana'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True


nome_do_restaurante = restaurante_praca.nome
categoria = Restaurante.categoria
restaurante_praca.nome = 'Bistro'


restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca,restaurante_pizza]

print(vars(restaurante_praca))

if restaurante_praca.ativo:
    print('O restaurante está ativo.\n')
else:
    print('O restaurante está inativo.\n')

print(vars(restaurante_pizza))

if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.\n')
else:
    print('A categoria não é Fast Food.\n')

print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')