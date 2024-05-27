'''
3 - Pedir que el usuario ingrese (input) nombre de personas y mostrarlos hasta que el valor de lo que ingresa sea “fin”
'''

nombres = []
valor = ""

print("ingresa nombres (para finalizar ingresa 'fin')")

while valor != "fin":
    valor = str(input("Nombre: "))
    if valor != "fin":
        nombres.append(valor)


print("Los nombres cargados son:")
for nombre in nombres:
    print(nombre)