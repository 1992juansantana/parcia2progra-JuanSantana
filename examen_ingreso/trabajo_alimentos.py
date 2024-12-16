# '''3-
# Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
# para preparar comida al por mayor , hasta que el cliente quiera:
# peso (entre 10 y 1000)en kilo,
# precio por kilo (más de cero ),
# tipo validad("v";"a";"m")(vegetal,animal o mezcla )
# Si compro más de 100 kilos en total tenes 15% de descuento sobre el total a pagar.
# Si compro más de 300 kilos en total tenes 25% de descuento sobre el total a pagar.
# Se debe Informar al usuario lo siguiente:
# a)El importe total a pagar , bruto sin descuento y...
# b)el importe total a pagar con descuento(solo si corresponde)

# d)Informar el tipo de alimento más caro.
# f)El promedio de precio por kilo en total.'''


PESO_MINIMO = 10
PESO_MAXIMO = 1000

PRECIO = 0

V = "VEGETAL"
A = "ANIMAL"
M = "MEZCLA"

contador_precio = 0
acumulador_total_peso = 0
acumulador_total_kilo = 0
alimento_mas_caro = None
precio_mas_caro = None

while True:
    
    peso = float(input("ingrese la cantidad de peso: "))
    while not peso >= PESO_MINIMO and peso <= PESO_MAXIMO :
        peso = float("ERROR! DEBE ELEGIR UNA CANTIDAD ENTRE 10 Y 1000 KG !!!")
        
    precio = float(input("Ingrese el precio por kg: "))
    while not precio >= 0:
        precio = float(input("ERROR! EL NUMERO DEBE SER MAS DE 0 !!!"))
        
    print("ingrese el tipo de alimento")
    print("1 - VEGETAL")
    print("2 - ANIMAL")
    print("3 - MEZCLA")

    tipo_alimento = input("Ingrese el tipo de alimento que desea comprar: ").upper()
    while tipo_alimento != V and tipo_alimento != A and tipo_alimento != M:
        tipo_alimento = input("ERROR! INGRESE UN ALIMENTO VALIDO !!!")
    
    contador_precio +=1
    acumulador_total_kilo += precio
    acumulador_total_peso += peso
    
    
    if peso >= 100:
        descuento = 0.15
    if peso >= 300:
        descuento = 0.25
    
    precio_total = peso * precio
    precio_con_descuento = precio_total * descuento
    total_con_descuento = precio_total - peso
    
    if precio_mas_caro == None or precio > precio_mas_caro:
        precio_mas_Caro = precio
        alimento_mas_caro = tipo_alimento
        
    print("¿DESEA SEGUIR COMPRANDO?")
    opcion_continuar = input("si/no : ")
    if opcion_continuar == "no" :
        break
    elif opcion_continuar != "si":
        opcion_continuar = input("ERROR!!! debe responder con si/no : ")
            
        
        
    print(f"el precio total sin descuento es de: {precio_total}")
    print(f"el precio total con descuento es de: {total_con_descuento}")
    print(f"El alimento mas caro es: ", alimento_mas_caro)
    print(f"el promedio total de precio por kilo es de $ {precio_total / acumulador_total_kilo}")
    
        

    
    
