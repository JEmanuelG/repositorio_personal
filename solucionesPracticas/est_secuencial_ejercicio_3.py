'''
EJERCICIO 3: Un hincha de fútbol desea conocer la cantidad de puntos que su
equipo lleva acumulados en el campeonato, para ello recibe cada semana la
información de la cantidad total de partidos, desde el inicio del campeonato, que
el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado
recibe un punto, por cada partido ganado tres puntos y por los perdidos cero
puntos.
'''

# DEFINE VARIABLES DE RESULTADOS DE PARTIDOS
print("Ingresa la cant. de partidos por cada tipo de resultado")

perdidos = int(input("Cant. partidos perdidos:"))
empatados = int(input("Cant. partidos empatados:"))
ganados = int(input("Cant. partidos ganados:"))

# DEFINE ACUMULADOR DE PUNTOS
puntos = 0

# SUMA PUNTOS SEGUN CORRESPONDA CONTROLANDO CON IF
if empatados > 0:
    puntos += empatados

if ganados > 0:
    puntos += ganados * 3

# MUESTRA RESULTADO
print(f"Tu equipo sumó {puntos} puntos durante el campeonato.")