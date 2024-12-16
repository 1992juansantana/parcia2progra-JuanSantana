

TARIFA_MIN = 10000
TARIFA_MAX = 20000

ALTURA_MIN = 100
ALTURA_MAX = 250

PESO_MIN = 30
PESO_MAX = 200

RUTINA_CARDIO = "CARDIO"
RUTINA_MUSCULACION = "MUSCULACION"
RUTINA_FUNCIONAL = "FUNCIONAL"

contador_socio = 0
contador_rutina_funcional = 0
contador_rutina_musculacion = 0
acumulador_socio_musculacion = 0
contador_rutina_altura_cardio = 0
contador_rutina_altura_musculacion = 0
contador_rutina_altura_funcional = 0
contador_porcentaje_rutina_funcional = 0

socio_mayor_peso = 0
peso_socio_funcional = None
nombre_socio_funcional = None
altura_socio_funcional = None

while contador_socio < 20:
    nombre = input("Ingrese su nombre completo: ")

    tarifa = int(input ("Ingrese la tarifa: "))
    while tarifa < TARIFA_MIN or tarifa > TARIFA_MAX :
        tarifa = int(input("ERROR! LA TARIFA ES ENTRE 10000 Y 20000 !!!"))

    altura = float(input("Ingrese su altura en cm: "))  
    while altura < ALTURA_MIN or altura > ALTURA_MAX:
        altura = float(input("ERROR! LA ALTURA DEBE SER ENTRE 100 Y 250 CM !!!"))

    peso = float(input("Ingrese su peso en kg: "))
    while peso < PESO_MIN or peso > PESO_MAX:
            peso = float(input("ERROR! EL PESO DEBE SER ENTRE 30 Y 200 KG !!!"))

    rutina = input(f"Elegir la rutina: [{RUTINA_CARDIO}]PARA CARDIO [{RUTINA_MUSCULACION}] PARA SERVICIO [{RUTINA_FUNCIONAL}] PARA FUNCIONAL: ").upper()
    while rutina != RUTINA_CARDIO and rutina != RUTINA_MUSCULACION and rutina != RUTINA_FUNCIONAL:
        rutina = input("ERROR! INGRESE UNA RUTINA VALIDA !!!")
        
    
    contador_socio += 1
    
    
    if rutina == RUTINA_FUNCIONAL and peso < 85:
        contador_rutina_funcional += 1
        
    if rutina == RUTINA_MUSCULACION and peso > 90:
        contador_rutina_musculacion +=1
        acumulador_socio_musculacion = acumulador_socio_musculacion + tarifa
    
    
    if rutina == RUTINA_FUNCIONAL and (socio_mayor_peso == 0 or peso > socio_mayor_peso):
        peso_socio_funcional = peso
        nombre_socio_funcional = nombre
        altura_socio_funcional = altura
    
    if rutina == RUTINA_CARDIO and altura > 170:
        contador_rutina_altura_cardio += 1
    if rutina == RUTINA_MUSCULACION and altura > 170:
        contador_rutina_altura_musculacion += 1
    if rutina == RUTINA_FUNCIONAL and altura > 170:
        contador_rutina_altura_funcional += 1
        
    if rutina == RUTINA_FUNCIONAL:
        contador_porcentaje_rutina_funcional +=1
        
        
        
        
        
        
        
#1
print ("1) cantidad de socios que realizan funcional y pesan menos de 85 son: ", contador_rutina_funcional)

#2
if contador_rutina_musculacion > 0:
    promedio_socio_musculacion = acumulador_socio_musculacion/contador_rutina_musculacion
    print(f"2) el promedio de la recaudacion de musculacion es :{round(promedio_socio_musculacion,2)} $") 
#3
print(f"3) el socio de funcional de mayor peso, su nombre es: {nombre_socio_funcional} y su altura es {altura_socio_funcional} y su peso es {peso_socio_funcional}")

#4
if contador_rutina_altura_cardio > contador_rutina_altura_funcional and contador_rutina_altura_cardio > contador_rutina_altura_musculacion:
    print("4) la rutina mas elegida con una altura mayor a 170cm es: ", RUTINA_CARDIO)
if contador_rutina_altura_musculacion > contador_rutina_altura_cardio and contador_rutina_altura_musculacion > contador_rutina_altura_funcional:
    print("4) la rutina mas elegida con una altura mayor a 170cm es: ", RUTINA_MUSCULACION)
if contador_rutina_altura_funcional > contador_rutina_altura_cardio and contador_rutina_altura_funcional > contador_rutina_altura_musculacion:
    print("4) la rutina mas elegida con una altura mayor a 170cm es: ", RUTINA_FUNCIONAL)
    
#5
if  contador_porcentaje_rutina_funcional !=0:
    porcentaje_publicaciones_inactivas = (contador_porcentaje_rutina_funcional * 100) / contador_socio
print(f"5) el porcentaje de rutina funcional es: {round(porcentaje_publicaciones_inactivas,2)} %")
