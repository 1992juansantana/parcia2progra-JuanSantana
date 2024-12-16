# nombreUsuario= input("Ingrese su nombre")
# print("Hola", nombreUsuario)

# numberOne = int(input("Ingrese el primer numero"))
# numberTwo = int(input("Ingrese el segundo numero"))
# print (numberOne+numberTwo)

# nombreUsuario= input("Ingrese su nombre")
# apellidoUsuario= input("Ingrese su apellido")
# edad = int(input("Ingrese su edad"))
# print(nombreUsuario, apellidoUsuario, edad)

# nombre= input("Ingrese su nombre")
# comision= input("Ingrese su numero de comision")
# asignatura= input("Ingrese su asignatura")
# docente= input("Ingrese nombre del docente")
# presentismo = (input("El usuario estuvo presente?"))
# print("nombre:", nombre,"comision:", comision,"asignatura:", asignatura,"docente:", docente,"asistio el usuario?:", presentismo)

# ladoCuadrado = int(input("Ingrese el lado de un cuadrado"))
# print ("la superfice es:", ladoCuadrado*4)

# lado1 = int(input("Ingrese el primer lado del rectangulo"))
# lado2 = int(input("Ingrese el segundo lado del rectangulo"))
# print ("la superfice es:", lado1*lado2)

# base = int(input("Ingrese la base de un triangulo"))
# altura = int(input("Ingrese la altura de un triangulo"))
# print ("la superfice es:", (base*altura)/2)

# nombreProducto = input("Ingrese el nombre del producto")
# precioProducto = int(input("Ingrese el precio de un producto"))
# productoIVA = (precioProducto)*1.21
# print("Nombre del producto:", nombreProducto,"precio sin IVA:", precioProducto,"precio con IVA:", productoIVA)

# nombre = input("Ingrese su nombre")
# apellido = input("Ingrese su apellido")
# nota1 = int(input("Ingrese la primer nota"))
# nota2 = int(input("Ingrese la segunda nota"))
# nota3 = int(input("Ingrese la tercer nota"))
# print("nombre alumno:",nombre,'',apellido)
# print("el promedio total es:", (nota1+nota2+nota3)/100)

# nombre = input("Ingrese su nombre")
# edad = int(input("Ingrese su edad"))
# print("su edad dentro de 10 años sera:", edad +10)

# precio1 = int(input("Ingrese el primer precio del producto"))
# precio2 = int(input("Ingrese el segundo precio del producto"))
# precio3 = int(input("Ingrese el tercer precio del producto"))
# print ("la suma es:", precio1+precio2+precio3)
# print ("el promedio total es:", (precio1+precio2+precio3)/100)
# print ("el precio final mas IVA es:", (precio1+precio2+precio3)*1.21)

# print("para ventas ingrese 1")
# print("para administracion ingrese 2")
# print("para administracion ingrese 3")

# opcion = int(input("ingrese una opcion:  "))

# match opcion:
#     case 1:
#         print ("VENTAS")
#     case 2:
#         print ("ADMINISTRATIVO")
#     case 3:
#         print ("SOPORTE TECNICO")
#     case _:
#         print("porfavor eliga una opcion valida")
# EDAD_MNINIMA = 21

# edad = int(input("Ingrese su edad: "))
# categoria = (input("Ingrese su categoria(A, B, C, D, E, F, G) "))

# if edad >= EDAD_MNINIMA and (categoria == "D" or categoria == "d"):
#     print("Puede conducir ambulancia")
# else:
#     print("no puede conducir ambulancia")

# edad = int(input("Ingrese su edad"))

# if edad == 18:
#     print("Usted tiene 18 años")


# edad = int(input("Ingrese su edad"))

# if edad >= 18:
#     print("MAYOR")
# elif edad <=17:
#     print("MENOR")


# altura = float(input("Ingrese su altura"))

# if altura >= 1.80:
#     print("Usted es pivot")
# elif altura <=1.79:
#      print("Usted no es pivot")


# edad = int(input("Ingrese su edad"))

# if edad >= 13 and edad <= 17:
#     print("Usted es adolecente")
# else:
#      print("no eres adolecente")

# edad = int(input("Ingrese su edad"))
# if edad <= 9 :
#     print("eres muy chico")
# elif edad >= 10 and edad <= 12:
#     print("eres pre adolecente")
# elif edad >= 13 and edad <= 17:
#      print("eres un adolecente")

# contador = 1

# while contador <= 10:
#     print(contador)
#     contador = contador +1

# contador = 0

# while contador <= 10:
#     print(contador)
#     contador = contador +2




# password = input("ingrese su clave: ")

# while password != "utn750":
#     password = int(input("clave incorrecta, intente nuevamente"))
#     print("Bienvenido al sistema")

# number = int(input("Ingrese un numero entre el 0 y 9: "))
# while number < 0 or number > 10:
#     number = int(input ("numero incorrecto, ingreselo nuevamente pofavor: "))



# letra = str(input("Ingrese una letra porfavor que sea la U, T o N: "))
# while letra != "U" and letra != "T" and letra != "N":
#     letra = str(input("Ingrese una letra correcta porfavor: "))

# numero1 = int(input("ingrese el numero 1: "))
# numero2 = int(input("ingrese el numero 2: "))
# numero3 = int(input("ingrese el numero 3: "))
# numero4 = int(input("ingrese el numero 4: "))
# numero5 = int(input("ingrese el numero 5: "))

# suma = (numero1 + numero2 +numero3 +numero4 + numero5)/100
# print (suma)



# #SOLICITAR NOMBRE DE LOS JUGADORES:

# jugador1 = input("Ingrese nombre de jugador uno: ")
# jugador2 = input("ingrese nombre del jugador dos: ")
# jugador3 = input("ingrese nombre del jugador tres: ")

# #SOLICITAR EDADES DE LOS JUGADORES:
# edad1 =int(input("ingrese la edad del jugador 1,debe ser mayor de 25: "))
# while edad1 < 25:
#     edad1=int(input("ingrese una edad valida, debe ser mayor a 25: "))
    
# edad2 = int(input("ingrese la edad del jugador 2,debe ser mayor de 25: "))
# while edad2 < 25:
#     edad2=int(input("ingrese una edad valida, debe ser mayor a 25: "))
    
# edad3 = int(input("ingrese la edad del jugador 3,debe ser mayor de 25: "))
# while edad3 < 25:
#     edad3=int(input("ingrese una edad valida, debe ser mayor a 25: "))
    
# # SOLICITAR VOTOS DE LOS JUGADORES:

# votos1 =int(input("ingrese la cantidad de votos del jugador numero 1: "))
# while votos1 <= 0:
#     votos1=int(input("no puede ser menor a 0: "))
    
# votos2 = int(input("ingrese la cantidad de votos del jugador numero 2: "))
# while votos2 <= 0:
#     votos2=int(input("no puede ser menor a 0: "))
    
# votos3 = int(input("ingrese la cantidad de votos del jugador numero 3: "))
# while votos3 <= 0:
#     votos3=int(input("no puede ser menor a 0: "))

# #NOMBRE DEL CANDIDATO CON MAS VOTOS:

# if votos1 > (votos2 and votos3):
#     print("el jugador " + jugador1," es el que mayor votos tiene")
# elif votos2 > (votos1 and votos3):
#     print("el jugador " + jugador2," es el que mayor votos tiene")
# else:
#     print("el jugador " + jugador3," es el que mayor votos tiene")
    
# #NOMBRE Y EDAD DEL CANDIDATO CON MENOS VOTOS:

# if votos1 < (votos2 and votos3):
#     print("el jugador " + jugador1, "de", + edad1, "años de edad es el que menor votos tiene")
# elif votos2 < (votos1 and votos3):
#     print("el jugador " + jugador2, "de", + edad2, "años de edad es el que menor votos tiene")
# else:
#     print("el jugador " + jugador3, "de", + edad3, "años de edad es el que menor votos tiene")
    
# # PROMEDIO DE EDAD DE LOS CANDIDATOS:

# edad = (edad1 + edad2 + edad3)/100
# print ("el promedio de edad es: ", edad)

# # TOTAL DE VOTOS EN TOTAL:

# votos = (votos1 + votos2 +votos3)
# print("la cantidad de votos total fue de: ", votos)
# -------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# En una ferretería se quiere implementar un sistema que permita a los usuarios saber cuánto deberán 
# pagar por la compra de lámparas de bajo consumo. Se tiene en cuenta que todas las lámparas cuestan $800.

# A partir de la cantidad y marca de las lámparas compradas (solo se puede comprar una marca por vez) se aplicará el siguiente descuento:

# Si compra 6 o más  lámparas bajo consumo tiene un descuento del 50%. 

# Si compra 5  lámparas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.

# Si compra 4  lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.

# Si compra 3  lámparas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.

# Por otro lado, si el importe final con descuento suma más de $4000  se obtiene un descuento adicional de 5%.

# Mostrar por pantalla: 

# Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, el descuento adicional (si corresponde) y el total a pagar con descuento.

# LAMPARAS = 800

# # SISTEMA DE BIENVENIDA Y OPCIONES DE STOCK:
# print("Bienvenido al sistema de compra de lamparas. ")
# print ("Estas son nuestras marcas disponibles en stock: ")
# print("OPCION 1: ArgentinaLuz")
# print("OPCION 2: FelizpeLamparas")
# print("OPCION 3: PepitoLuz")

# marca = (input("Ingrese con un numero la marca que desea comprar: "))
# match marca:
#     case 1:
#         print ("ArgentinaLuz")
#     case 2:
#         print ("FelizpeLamparas")
#     case 3:
#         print ("PepitoLuz")
        
# # CANTIDAD QUE DESEA COMPRAR:
# cantidad = int(input("porfavor Ingrese la cantidad de lamparas que desea comprar?: "))
# #PROMO 1
# if  cantidad >= 6 :
#     TotalPromo1 = (cantidad*LAMPARAS) / 2
    
# if  TotalPromo1 >= 4000:
#     DesAdiccional = (TotalPromo1)*0.05
#     Total = (TotalPromo1) - (DesAdiccional)
 
#     print ("TICKET TOTAL: ")
#     print (" de la marca: ", marca)
#     print ("Usted compro la cantidad de lamparas numero: " , cantidad)
#     print ("el total sin descuento es: ", cantidad*LAMPARAS )
#     print ("tuvistes un descuento adicional por superar los $4000 de: ", DesAdiccional)
#     print ("el total con descuento es ; $", Total)
    
    

    
    
# #PROMO 2
# if (cantidad == 5) and (marca == 1):
#     calculo1 = (cantidad*LAMPARAS)
#     calculo2 = calculo1*0.40
#     TotalPromo2 = calculo1 - calculo2
#     print ("el total es; $", TotalPromo2)
# elif (cantidad == 5) and (marca == 2 or marca == 3):
#     calculo1 = (cantidad*LAMPARAS)
#     calculo2 = calculo1*0.30
#     TotalPromo2 = calculo1 - calculo2
#     print ("TICKET TOTAL: ")
#     print ("Usted compro la cantidad de lamparas numero: " , cantidad)
#     print (" de la marca: ", marca)
#     print ("el total es; $", TotalPromo2)
    
    
# #PROMO 3
# if (cantidad == 4) and (marca == 1 or marca == 2):
#     calculo1 = (cantidad*LAMPARAS)
#     calculo2 = calculo1*0.25
#     TotalPromo3 = calculo1 - calculo2
#     print ("TICKET TOTAL: ")
#     print ("Usted compro la cantidad de lamparas numero: " , cantidad)
#     print (" de la marca: ", marca)
#     print ("el total es; $", TotalPromo3)
# elif(cantidad == 4) and (marca == 3):
#     calculo1 = (cantidad*LAMPARAS)
#     calculo2 = calculo1*0.20
#     TotalPromo3 = calculo1 - calculo2
#     print ("TICKET TOTAL: ")
#     print ("Usted compro la cantidad de lamparas numero: " , cantidad)
#     print (" de la marca: ", marca)
#     print ("el total es; $", TotalPromo3)

# #PROMO 4

# if (cantidad == 3) and (marca == 1 ):
#     calculo1 = (cantidad*LAMPARAS)
#     calculo2 = calculo1*0.15
#     TotalPromo4 = calculo1 - calculo2
#     print ("TICKET TOTAL: ")
#     print ("Usted compro la cantidad de lamparas numero: " , cantidad)
#     print (" de la marca: ", marca)
#     print ("el total es; $", TotalPromo4)
# elif (cantidad == 3) and (marca == 2 ):
#     calculo1 = (cantidad*LAMPARAS)
#     calculo2 = calculo1*0.10
#     TotalPromo4 = calculo1 - calculo2
#     print ("TICKET TOTAL: ")
#     print ("Usted compro la cantidad de lamparas numero: " , cantidad)
#     print (" de la marca: ", marca)
#     print ("el total es; $", TotalPromo4)
# elif (cantidad == 3) and (marca == 3 ):
#     calculo1 = (cantidad*LAMPARAS)
#     calculo2 = calculo1*0.5
#     TotalPromo4 = calculo1 - calculo2 
#     print ("TICKET TOTAL: ")
#     print ("Usted compro la cantidad de lamparas numero: " , cantidad)
#     print (" de la marca: ", marca)
#     print ("el total es; $", TotalPromo4)




# 1-
# Debemos realizar la carga de 5(cinco) productos de prevención de contagio,
# de cada una debo obtener los siguientes datos:
# el tipo (validar "barbijo" , "jabón" o "alcohol", “guardapolvo”, “guantes”) ,
# el precio (validar entre 100 y 300),
# la cantidad de unidades 
# (no puede ser 0 o negativo y no debe superar las 1000 unidades),
# la Marca y el fabricante.
# Se debe Informar al usuario lo siguiente:
# a) Del más caro de los Barbijos, la cantidad de unidades y el fabricante
# b) Del ítem con más
# más unidades, el fabricante
# c) Cuántas unidades de jabones hay en total


# TIPO_BARBIJO = "barbijo"
# TIPO_JABON ="jabon"
# TIPO_ALCHOL = "alchol"
# TIPO_GUARDAPOLVO = "guardapolvo"
# TIPO_GUANTES = "guantes"

# PRECIO_MIN = 100
# PRECIO_MAX = 300

# CANTIDAD_MAXIMA = 1000
# CANTIDAD_MINIMA = 1

# contador_productos = 0

# precio_barbijo_mas_caro = 0
# cantidad_barbijo_mas_caro = 0
# fabricante_Barbijo_mas_caro = None

# while contador_productos < 5:
#     tipo_producto = input(f" ingrese el producto {TIPO_BARBIJO},{TIPO_JABON},{TIPO_ALCHOL},{TIPO_GUARDAPOLVO},{TIPO_GUANTES}: ")
# while tipo_producto != TIPO_BARBIJO and tipo_producto != TIPO_JABON and tipo_producto != TIPO_BARBIJO and tipo_producto != TIPO_ALCHOL and tipo_producto != TIPO_GUARDAPOLVO and tipo_producto != TIPO_GUANTES:
#      tipo_producto = input (f"ERROR ELIJA NUEVAMENTE EL TIPO DEL PRODUCTO{TIPO_BARBIJO},{TIPO_JABON},{TIPO_ALCHOL},{TIPO_GUARDAPOLVO},{TIPO_GUANTES}: ")
    
# precio = int(input("ingrese el precio"))
# while not (precio > PRECIO_MIN and precio < PRECIO_MAX):
#     precio = int(input("ERROR, ingrese el nuevo el precio"))
    
# cantidad = int(input("ingrese la cantidad entre 1 y 1000: "))
# while not (cantidad > CANTIDAD_MINIMA and precio < CANTIDAD_MAXIMA):
#    cantidad = int (input("ERROR, Ingrese una nueva cantidad: "))

# marca = input("ingrese la marca")
# fabricante = input("ingrese el nombre del fabricante")


        
# if tipo_producto == TIPO_BARBIJO and (precio_barbijo_mas_caro == 0 or precio > precio_barbijo_mas_caro):
#     precio_barbijo_mas_caro = precio
#     cantidad_barbijo_mas_caro = cantidad
#     fabricante_Barbijo_mas_caro = fabricante
    
# contador_productos +=1

# print(f"el fabricante{fabricante_Barbijo_mas_caro} fue el que vendio el/los barbijos mas caros $
#       ${precio_barbijo_mas_caro} la cantidad fue de {cantidad_barbijo_mas_caro} unidad/unidades")


# NUMERO PRIMO :

# numero = -50

# divisor = 2
# es_primo = True
# if(numero <= 1):
#     es_primo = False
# while es_primo and divisor < numero:
#     if (numero % divisor == 0):
#         es_primo = False
#         divisor+=1
# if es_primo:
#     print("es primo")
# else:
#     print("no es primo")
# -----------------------------------------------------------
# -----------------------------------------------------------
# 5. Terminados en 8 o 9:
# ● Informar la cantidad total de socios que realizan “Funcional” y su altura es
# inferior a “165”.
# ● El promedio total recaudado de los socios que realizan “Musculación” y su peso
# es superior a “120”.
# ● El nombre y la altura del socio que realiza “Musculación” de mayor peso.

# B. Informar cuál fue el tipo de rutina de entrenamiento más elegida.
# C. Los porcentajes de cada tipo de rutina de entrenamiento. Ejemplo: [30% Cardio, 40%
# Funcional, 30% Musculación]

#SIMULACRO


NOMBRE = "NOMBRE"
APELLIDO = "APELLIDO"

TARIFA_BASE = 10000

ALTURA_MINIMA = 100
ALTURA_MAXIMA = 250

PESO_MINIMO = 30
PESO_MAXIMO = 200

RUTINA_CARDIO = "CARDIO"
RUTINA_MUSCULACION = "MUSCULACION"
RUTINA_FUNCIONAL = "FUNCIONAL"

contador_socio = 0
acumulador_socio = 0
cantidad_socio_cardio= 0
cantidad_socio_musculacion = 0
cantidad_socio_funcional = 0
cantidad_socio_funcional_altura_inferior_165=0
cantidad_socio_musculacion_peso_mayor_120 = 0
cantidad_socio_musculacion_peso_mayor_200 = 0

#INGRESO DE DATOS:
while contador_socio < 1:
    nombre_completo = input(f" ingrese su {NOMBRE} y {APELLIDO}: ")

    tarifa = int(input("ingrese la tarifa: "))
    while tarifa != 10000:
        tarifa = int(input("ERROR, la tarifa debe ser 10000!!!: "))
        
    altura = float(input("ingrese su altura: "))
    while not (altura > ALTURA_MINIMA and altura < ALTURA_MAXIMA):
        altura = float(input("ERROR, ingrese una altura entre 100 y 250"))
        
    peso = float(input("ingrese su peso: "))
    while not (peso > PESO_MINIMO and peso < PESO_MAXIMO):
        peso = float(input("ERROR, ingrese un peso entre 30 y 200"))

    rutina = input(f"ingrese la rutina que desea realizar {RUTINA_CARDIO}, {RUTINA_FUNCIONAL}, {RUTINA_MUSCULACION}: ").upper()
    while rutina != RUTINA_CARDIO and rutina != RUTINA_MUSCULACION and rutina != RUTINA_FUNCIONAL:
        rutina = float(input(f"ERROR, Eliga una opcion valida{RUTINA_CARDIO}, ´{RUTINA_MUSCULACION}, {RUTINA_FUNCIONAL}"))
        
# CALCULO DE PORCENTAJE SEGUN RUTINA ELEGIDA
    if rutina == RUTINA_CARDIO and RUTINA_MUSCULACION:
        calculo = TARIFA_BASE/100*0.10
        total_tarifa = TARIFA_BASE + calculo
        print(f"el abono de la cuota sera de: {total_tarifa}")
        
        
    if rutina == RUTINA_FUNCIONAL:
        calculo = TARIFA_BASE/100*0.10
        total_tarifa = TARIFA_BASE - calculo
        print(f"el abono de la cuota sera de: {total_tarifa}")
        
#A
    if rutina == RUTINA_FUNCIONAL and altura < 165:
        cantidad_socio_funcional_altura_inferior_165 =+1
        
        
        
    if rutina == RUTINA_MUSCULACION and peso > 120:
        total_promedio = rutina*20
        cantidad_socio_musculacion_peso_mayor_120 =+1
        
        
        
    if rutina == RUTINA_MUSCULACION and peso > 200:
        cantidad_socio_musculacion_peso_mayor_200 =+1
        
    contador_socio +=1
    
    
 #B
    if cantidad_socio_cardio > cantidad_socio_funcional and cantidad_socio_musculacion:
        rutina_mas_elegida = RUTINA_CARDIO
    if cantidad_socio_funcional > cantidad_socio_cardio and cantidad_socio_musculacion:
        rutina_mas_elegida = RUTINA_FUNCIONAL
    if cantidad_socio_musculacion > cantidad_socio_funcional and cantidad_socio_cardio:
            rutina_mas_elegida = RUTINA_MUSCULACION
            print("la rutina mas elegida es: ", rutina_mas_elegida)
    print(cantidad_socio_funcional_altura_inferior_165)
    print(cantidad_socio_musculacion_peso_mayor_120)
    print(cantidad_socio_musculacion_peso_mayor_200)
            
    
    
    
    




