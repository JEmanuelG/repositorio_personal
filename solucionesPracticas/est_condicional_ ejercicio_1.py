'''
Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad.
Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un descuento
del 10%. Si compra más de 24 unidades, el descuento es del 15%. Además posee la promoción a
los jubilados. La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos,
se suma los descuentos). Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.

'''
# DEFINE PRECIO DEL LITRO DE LECHE
precio_litro = 1000

# DEFINE VARIABLE DEL TOTAL DE DESCUENTO Y MONTO TOTAL
descuento = 0
monto_total = 0

# DEFINE VARIABLES DETALLES DE VENTA
print("VENTA DE LECHE")
cant_litros = float(input("Ingresa la cantidad de litros:"))
es_jubilado = int(input("Es jubilado? (1 = Si / 2 = No)"))

# CALCULA DESCUENTOS SEGUN CANTIDAD DE LITROS
if cant_litros > 12 and cant_litros <= 24:
    descuento = 0.10
elif cant_litros > 24:
    descuento = 0.15

# SUMA DESCUENTO SI ES JUBILADO
if es_jubilado == 1:
    descuento += 0.10

# CALCULA MONTO TOTAL A COBRAR
monto_total = cant_litros * (precio_litro - (precio_litro * descuento))

# MUESTRA RESULTADO
print(f"El cliente debe pagar ${monto_total}")