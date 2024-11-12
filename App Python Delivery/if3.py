temperatura = float(input("Digite a temperatura atual: "))
# Está sendo utilizado o float pois o numero de entrada pode ser um numero com casas decimais, o int só iria reconhecer a parte inteira do número
if temperatura > 25:
    print("Alerta! Temperatura acima do limite permitido.")
else:
    print("Temperatura dentro do limite seguro.")