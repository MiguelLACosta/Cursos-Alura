import os

maca = int(input('Insira a quantidade de maçãs vendidas: '))
banana = int(input('Insira a quantidade de Bananas vendidas: '))
if maca > banana:
    os.system('cls')
    print('Foram vendidas mais maçãs do que bananas')

elif banana > maca:
    os.system('cls')
    print('Foram vendidas mais bananas do que maçãs')

else:
    os.system('cls')
    print(f'A quantidade de maçãs e bananas vendidas foram iguais, sendo vendidas {maca} de cada')

