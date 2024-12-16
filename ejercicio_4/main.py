import funciones

# Debemos alquilar el servicio de transporte para llegar a Mar del Plata con un
# grupo de personas, de cada persona debemos obtener los siguientes datos:

# - número de cliente
# - estado civil ("soltero", "casado"  o "viudo")
# - edad (solo mayores de edad, más de 17)
# - dni (validar que el numero sea de 8 digitos)

# NOTA: el precio por pasajero es de $60000.

# Se debe informar (solo si corresponde):

# a)  La cantidad de personas con estado "casado" de más de 40 años y
#     menos de 60 años.
# b)  el número de cliente y edad de la mujer soltera más joven.
# c)  cuánto sale el viaje total sin descuento.
# d)  si hay más del 50% de los pasajeros que tiene más de 60 años , el precio
#     final tiene un descuento del 25%, que solo mostramos si corresponde.

# Crear funciones para realizar la validación e ingreso de datos, incorporandolas a nuestros módulos
CIVIL_SOLTERO = "SOLTERO"
CIVIL_CASADO = "CASADO"
CIVIL_VIUDO = "VIUDO"

EDAD_MINIMA = 17
EDAD_MAXIMA = 100
PRECIO_PASAJE = 60000

cantidad_pasajeros = 0
cantidad_personas_casadas = 0
edad_menor= 0
numero_cliente_menor_soltera = None
precio_final = None

pasajeros_mayores_60 = 0


numero = funciones.obtener_cliente()

civil = funciones.pedir_civil()

edad = funciones.pedir_edad()

dni = funciones.pedir_dni()

genero = funciones.pedir_genero()

cantidad_pasajeros +=1


if  edad >= 40 or edad <= 60 and civil == CIVIL_CASADO:
    cantidad_personas_casadas += 1
    
if (edad_menor==0 or edad > edad_menor) and civil == CIVIL_SOLTERO and genero == "HOMBRE":
    edad_menor = edad
    numero_cliente_menor_soltera = numero
    
if cantidad_pasajeros > 0 and (pasajeros_mayores_60 / cantidad_pasajeros) > 0.5:
    precio_total = cantidad_pasajeros * PRECIO_PASAJE
    precio_final = PRECIO_PASAJE * 0.75



print("la cantidad de personas casadas son : ", cantidad_personas_casadas)

print(f"Número de cliente y edad de la mujer soltera más joven: {numero_cliente_menor_soltera} y {edad_menor}")

print(f"precio total del viaje sin descuento: ", PRECIO_PASAJE)
print(f"precio con descuento es: ", precio_final)







