
CIVIL_SOLTERO = "SOLTERO"
CIVIL_CASADO = "CASADO"
CIVIL_VIUDO = "VIUDO"

GENERO_MUJER = "MUJER"
GENERO_HOMBRE = "HOMBRE"

EDAD_MINIMA = 17
EDAD_MAXIMA = 100

PRECIO_PASAJE = 60000

# FUNCION PARA PEDIR NUMERO DE CLIENTE:
def obtener_cliente():
    numero = input("Por favor, ingrese se número de cliente: ")
    for caracter in numero:
        if caracter < "0" or caracter > "9":
            return ("Numero de cliente incorrecto")
    numero = int(numero)
    return numero
    
print(obtener_cliente()) 

#FUNCION PARA PEDIR ESTADO CIVIL:

def pedir_civil():
    estado_civil = input(f"Ingrese su estado civil porfavor: [{CIVIL_SOLTERO}] para soltero. [{CIVIL_CASADO}] para casado. [{CIVIL_VIUDO}] para viudo: ").upper()
    while estado_civil != CIVIL_SOLTERO and estado_civil != CIVIL_CASADO and estado_civil != CIVIL_VIUDO:
        estado_civil = input ("ERROR !!! PORFAVOR INGRESE UN ESTADO CIVIL VALIDO : ").upper()
    return estado_civil    

print(pedir_civil())


#FUNCION PARA PEDIR EDAD:


def pedir_edad():
    
    edad = int(input("Porfavor ingrese su edad: "))
    while  edad < EDAD_MINIMA:
        edad = int(input("ERROR!! LA EDAD DEBE SER MAYOR A 17!!!, Ingrese su edad nuevamente: "))
    return edad
        
print(pedir_edad())

#FUNCION PARA PEDIR DNI:

def pedir_dni():

    dni = int(input("Ingrese su dni porfavor: "))
    while dni > 99999999:
        dni = int(input("ERROR!!! PORFAVOR INGRESE UN NUMERO DE DNI VALIDO!!! Ingrese nuevamente el numero de dni: "))
    return dni

print(pedir_dni())


def pedir_genero():

    genero = input(f"Ingrese su genero porfavor: [{GENERO_MUJER}] para MUJER [{GENERO_HOMBRE}] para MASCULINO: ").upper()
    while genero != GENERO_MUJER and genero != GENERO_HOMBRE:
        genero = input ("ERROR !!! PORFAVOR INGRESE UN GENERO VALIDO : ").upper()
      
    return genero

print(pedir_genero())

