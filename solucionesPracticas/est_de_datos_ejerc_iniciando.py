print('''
ELIJA UNA OPCIÓN PARA EJECUTAR EJERCICIOS

1) Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una
lista y mostrarlos. 

2) Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo

3) Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento.

4) En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con los mismos 5 datos (nombre,
apellido, dni, email, fecha de nacimiento)

5) Guardar en una tupla los primeros n números pares. El valor de n que lo ingrese el usuario (input). Luego
mostrar los datos de la tupla.

6) Salir.
''')

flag_op1 = False
opcion = 0



while opcion != 6:

    print("\n"+"*"*50+"\n")
    opcion = int(input("Opción:"))

    while opcion not in (1,2,3,4,5,6):
        opcion = int(input("OPCIÓN INCORRECTA, INGRASA DE NUEVO:"))

    if opcion == 2 and not flag_op1:
        print("No podés ejecutar la opción 2 sin haber ejecutado la opción 1 primer")
        opcion = 1

    if opcion == 1:
        nombres = []
        flag_op1 = True

        print("ingresa 10 nombres de personas sin repetir")
        for n in range(10):
            nombre = str(input("Nombre:"))

            while nombre in nombres:
                nombre = str(input("Ese nombre ya está cargado, ingresa otro:"))
    
            nombres.append(nombre)

        print("-" * 50 + "\n" + "Los nombres cargados:")
        for n in nombres:
            print(n)

    elif opcion == 2:
        nombres.pop(2)
        nombres.pop(-1)
        nombres.sort()

        print("Así quedó la lista de nombres cargados:")
        for n in nombres:
            print(n)

    elif opcion == 3:
        nombre = str(input("Nombre:"))
        apellido = str(input("Apellido:"))
        dni = str(input("DNI:"))
        email = str(input("Email:"))
        fecha_nacimiento = str(input("Fecha de nacimiento:"))

        dic_persona = {"nombre":nombre, "apellido":apellido, "dni":dni, "email":email, "fecha_nacimiento":fecha_nacimiento}

    elif opcion == 4:
        dic_familia = {}
        
        for integrante in range(4):
            print(f"Ingresa los datos del integrante {integrante} de la flia.")
            nombre = str(input("Nombre:"))
            apellido = str(input("Apellido:"))
            dni = str(input("DNI:"))
            email = str(input("Email:"))
            fecha_nacimiento = str(input("Fecha de nacimiento:"))

            dic_persona = {"nombre":nombre, "apellido":apellido, "dni":dni, "email":email, "fecha_nacimiento":fecha_nacimiento}

            dic_familia["integrante_"+str(integrante)] = dic_persona

    elif opcion == 5:
        lista_num = []
        
        print("Ingresa un número para guardar todos los números PARES desde el 0 hasta tu número")
        num = int(input("Número: "))

        for n in range(0, num+1):
            if n % 2 == 0:
                lista_num.append(n)

        tupla_num = tuple(lista_num)

        print(tupla_num)

