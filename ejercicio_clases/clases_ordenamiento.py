# Se nos pide que diseñemos un programa  que nos permita, 
# mediante un menu de opciones, realizar consultas sobre la informacion de estudiantes 
# de la universidad. Cada estudiante tiene:

# - Nombre 
# - Apellido
# - Legajo
# - Division
# - Notas (primer parcial y segundo parcial)

# Asi mismo, contamos con una lista de divisiones a las que puede pertenecer un alumno: 1A, 2B, 1C, 1D, 2A, 2B , 2C, 3A, 3B, 4A
# Las consultas que se requieren realizar son:

# - Nombre, division y nota del estudiante con mayor promedio.

# - De cada division, mostrar los alumnos en condicion de aprobacion directa (se requiere nota 6 o mas en ambos parciales para esta condicion). 

# - Ordenar los alumnos por legajo, nombre o apellido

# - De cada division, el alumno con la menor nota

# - Seleccionar un alumno y modificar sus notas o su division.




alumnos = [
    ["Juan", "Martin", "Claudia", "Francisco", "Romina"], #nombres
    ["Martinez","Fernandez","Ferreira", "Casals", "Scarsi"], #apellidos
    [123456,234567,345567,456789,567890],#legajos
    ["2A", "2A", "1C", "1B" ,"1D"],#divisiones
    [5,8,2,9,10],#nota 1
    [9,8,5,7,10]#nota 2
    ]

lista_divisiones = ["1A", "1B", "1C", "1D", "2A",
                    "2B" , "2C", "3A", "3B", "4A"]

def buscar_mayor_promedio(alumnos):
    mayor_promedio = 0
    nombre_mayor_promedio = None
    for i in range(len(alumnos[0])):
        promedio = (alumnos[4][i] + alumnos[5][i]) / 2
        if i == 0 or mayor_promedio < promedio:
            mayor_promedio = promedio
            nombre_mayor_promedio = i
    return nombre_mayor_promedio

def buscar_aprobacion_directa(alumnos, divisiones):

    for division in divisiones:
        bandera = False
        print(f"Alumnos en condicion de aprobacion directa en la división: {division}")
        for i in range(len(alumnos[0])):
            if alumnos[3][i] == division and alumnos[4][i] >= 6 and alumnos[5][i] >= 6:
                alumno_en_AD = i
                print(f"Nombre completo: {alumnos[1][i]} {alumnos[0][i]}")
                bandera = True
        if bandera == False:
            print("No hay alumnos en condicion de aprobación directa")

def mostrar_alumno_con_menor_promedio(alumnos, divisiones):

    for division in divisiones:
        menor_promedio = None
        alumno_con_menor_promedio = None
        for i in range (len(alumnos[0])):
            if alumnos[3][i] == division:
                promedio = (alumnos[4][i] + alumnos[5][i]) / 2
                if alumno_con_menor_promedio == None or promedio < menor_promedio:
                    menor_promedio = promedio
                    alumno_con_menor_promedio = i
        if alumno_con_menor_promedio != None:
            print(f"El alumno con menor promedio de la división {division} es {alumnos[1][alumno_con_menor_promedio]}, {alumnos[0][alumno_con_menor_promedio]}")
        else:
            print(f"No hay alumnos el la división {division}")


def modificar_alumno(alumnos):
    def mostrar_alumno(alumnos):
        for i in range(len(alumnos[0])):
            print(f"{i+1} - Nombre completo: {alumnos[1][i]}, {alumnos[0][i]}, Legajo: {alumnos[2][i]}, División: {alumnos[3][i]}, Notas: {alumnos[4][i]}, {alumnos[5][i]}")
    mostrar_alumno(alumnos)
    opcion = int(input("Ingrese el numero del alumno a modificar: "))
    opcion = opcion -1
    if opcion > len(alumnos[0]):
        print("No existe ese numero en el registro de alumnos otorgado")
    else:
        print(f"Se va a modificar a {alumnos[1][opcion]} {alumnos[0][opcion]}")
        def tomar_decision():
            bandera = True
            while bandera == True:
                decision = int(input("Ingrese 1 para modificar notas, 2 para modificar división: "))
                if decision == 1:
                    nueva_nota = int(input("Primera nueva nota modificada: "))
                    nueva_nota_2 = int(input("Segunda nueva nota modificada: "))
                    alumnos[4][opcion] = nueva_nota
                    alumnos[5][opcion] = nueva_nota_2
                    print(f"Alumno: {alumnos[0][opcion]} {alumnos[1][opcion]}, Nuevas Notas: {alumnos[4][opcion]}, {alumnos[5][opcion]}")
                    break
                elif decision == 2:
                    numero_nueva_division = input("Ingrese el numero de su nueva division: ")
                    letra_nueva_division = input("Ingrese la letra de su nueva división: ")
                    nueva_division = numero_nueva_division + letra_nueva_division
                    alumnos[3][opcion] = nueva_division
                    print(f"La nueva division del alumno {alumnos[0][opcion]} {alumnos[1][opcion]} es {alumnos[3][opcion]}")
                    bandera = False
                    break
                else:
                    print("Opcion incorrecta, vuelva a intentar")
        tomar_decision()


def menu(alumnos):
    print("1- Nombre, division y nota del estudiante con mayor promedio.")
    print("2- De cada division, mostrar los alumnos en condicion de aprobacion directa (se requiere nota 6 o mas en ambos parciales para esta condicion). ")
    print("3- Ordenar los alumnos por legajo, nombre o apellido")
    print("4- De cada division, el alumno con el menor promedio")
    print("5- Seleccionar un alumno y modificar sus notas o su division.")
    opcion_menu = int(input("Ingrese su opción: "))
    if opcion_menu == 1:
        mayor_promedio = buscar_mayor_promedio(alumnos)
        print(f"El alumno con mayor promedio es: {alumnos[0][mayor_promedio]} de la división {alumnos[3][mayor_promedio]} con un promedio de {(alumnos[4][mayor_promedio] + alumnos[5][mayor_promedio]) / 2}")

    elif opcion_menu == 2:
        buscar_aprobacion_directa(alumnos, lista_divisiones)

    elif opcion_menu == 3:
        print("Opcion no disponible")

    elif opcion_menu == 4:
        mostrar_alumno_con_menor_promedio(alumnos, lista_divisiones)

    elif opcion_menu == 5:
        modificar_alumno(alumnos)

    else:
        print("Opcion incorrecta.")

menu(alumnos)