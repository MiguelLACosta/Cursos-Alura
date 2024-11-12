lista_numeros = [10, 5, 8, 3, 7, 8, 25, 46, 25, 9861]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")