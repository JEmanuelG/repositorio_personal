'''
EJERCICIO 2: Un pintor de casas debe hacer un presupuesto para un cliente. Lo
que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El
cliente le indica que necesita conocer el costo de mano de obra para pintar una
pared rectangular de un galpón. El pintor cobra un monto fijo por cada metro
cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para
pintar la pared.
'''

# DEFINE VARIABLES MEDIDAS DE PARED
print("Ingresa las medidas en metros de la pared")
ancho_pared = float(input("Ancho pared:"))
alto_pared = float(input("Alto pared:"))

# DEFINE VARIABLE PRECIO X M2
precio = float(input("Ingresa el precio por m2: $"))

# CALCULA SUPERFICIE
superficie_pared = ancho_pared * alto_pared

# CALCULA EL COSTO PARA PINTAR LA PARED
costo_pared = round(superficie_pared * precio, 2)

# MUESTRA RESULTADO DEL COSTO
print(f"El costo para pintar la pared es: ${costo_pared}")