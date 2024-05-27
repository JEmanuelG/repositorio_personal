'''
EJERCICIO 1: Un estudiante está cursando 5 materias, tiene la nota de cada
materia y quiere saber cuál es su promedio.
'''


# DEFINE VARIABLES NOTAS
print("Ingresa las notas del alumno/a (1<=nota<=10)")
nota1 = int(input("Ingresa nota 1:"))
nota2 = int(input("Ingresa nota 2:"))
nota3 = int(input("Ingresa nota 3:"))
nota4 = int(input("Ingresa nota 4:"))
nota5 = int(input("Ingresa nota 5:"))

# CALCULA PROMEDIO

suma_notas = nota1 + nota2 + nota3 + nota4 + nota5
promedio = suma_notas / 5

# MUESTRA RESULTADOS
print(f"El promedio del alumno es: {promedio}")