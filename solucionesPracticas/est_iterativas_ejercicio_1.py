'''
1 - Mostrar los números desde el 0 al número solicitado al usuario (input)
'''

print("Ingresa un número para mostrar todos los números desde el 0 hasta tu número")
num = int(input("Número: "))

for n in range(0, num+1):
    print(n)