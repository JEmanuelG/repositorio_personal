'''
2 - Mostrar sólo los números pares desde 0 hasta el número ingresado (input). Nota: para saber si un número es par hacer i % 2 == 0)
'''

print("Ingresa un número para mostrar todos los números PARES desde el 0 hasta tu número")
num = int(input("Número: "))

for n in range(0, num+1):
    if n % 2 == 0:
        print(n)