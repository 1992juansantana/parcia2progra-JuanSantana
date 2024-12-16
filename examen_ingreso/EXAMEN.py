


TIPO_PRODUCTO = "PRODUCTO"
TIPO_SERVICIO = "SERVICIO"
TIPO_SUBASTA = "SUBASTA"

PUBLICACIONES_MIN = 1
PUBLICACIONES_MAX = 1000

CUENTA_ACTIVA = "SI"
CUENTA_INACTIVA = "NO"

contador_usuario = 0

usuario_mayor_edad = 0
nombre_usuario_mayor_edad=None
tipo_producto_usuario_mayor_edad = None

contador_usuarios_cuenta_activa = 0
contador_usuarios_cuenta_inactiva = 0

contador_publicaciones_subasta = 0
acumulador_edad_tipo_subasta = 0

contador_cuenta_activa_tipo_producto = 0
contador_cuenta_activa_tipo_servicio = 0
contador_cuenta_activa_tipo_subasta  = 0

while contador_usuario < 1:
    nombre = input("Ingrese su nombre de usuario: ")

    edad = int(input ("Ingrese su edad: "))
    while edad <= 0 :
        edad = int(input("ERROR! LA EDAD DEBE SER MAYOR A: 0 !!!"))

    cantidad_productos = int(input("Ingrese la cantidad de productos: "))  
    while cantidad_productos < 0:
        cantidad_productos = int(input("ERROR! LA CANTIDAD DE PRODUCTO DEBE SER UN NUMERO ENTERO POSITIVO !!!"))

    cantidad_publicaciones = int(input("Ingrese la cantidad de publicaciones: "))
    while cantidad_publicaciones < PUBLICACIONES_MIN or cantidad_publicaciones > PUBLICACIONES_MAX:
            cantidad_publicaciones = int(input("ERROR! LA CANTIDAD DE PUBLICACIONES DEBE SER ENTRE 0 Y 1000 !!!"))

    tipo = input(f"Elegir un tipo de producto: [{TIPO_PRODUCTO}]para producto [{TIPO_SERVICIO}] para servicio [{TIPO_SUBASTA}] para subasta: ").upper()
    while tipo != TIPO_PRODUCTO and tipo != TIPO_SERVICIO and tipo != TIPO_SUBASTA:
        tipo = input("ERROR! INGRESE UN TIPO VALIDO !!!")
        
    cuenta = input(f"Su cuenta esta activa? [{CUENTA_ACTIVA}] si esta activa [{CUENTA_INACTIVA}] no esta activa: ").upper()
    while cuenta != CUENTA_ACTIVA and cuenta != CUENTA_INACTIVA:
        cuenta = input("ERROR! INGRESE UNA OPCION VALIDA !!!")
    
    contador_usuario += 1
    
    #1
    if  cuenta == CUENTA_ACTIVA and tipo == TIPO_SUBASTA and edad < 60:
        contador_usuarios_cuenta_activa += 1
        
    #2
    if (usuario_mayor_edad==0 or edad > usuario_mayor_edad) and cantidad_publicaciones < 300:
        usuario_mayor_edad = edad
        nombre_usuario_mayor_edad=nombre
        tipo_producto_usuario_mayor_edad=tipo
    
    
    #3
    if cuenta == CUENTA_INACTIVA:
        contador_usuarios_cuenta_inactiva += 1
        # porcentaje_publicaciones_inactivas = (contador_usuarios_cuenta_inactiva * 100) / contador_usuario
        
    #4
    if tipo == TIPO_SUBASTA:
        contador_publicaciones_subasta += 1
        acumulador_edad_tipo_subasta = acumulador_edad_tipo_subasta + edad 
        
    #5
    if cuenta == CUENTA_INACTIVA and tipo == TIPO_PRODUCTO:
        contador_cuenta_activa_tipo_producto += 1
    if cuenta == CUENTA_INACTIVA and tipo == TIPO_SERVICIO:
        contador_cuenta_activa_tipo_servicio += 1
    if cuenta == CUENTA_INACTIVA and tipo == TIPO_SUBASTA:
        contador_cuenta_activa_tipo_subasta += 1
        


        
    
#1
print(f"la cantidad de usuarios con cuenta activa del tipo subasta mayores a 60 años son: ", {contador_usuarios_cuenta_activa})

#2
print(f"El usuario de mayor edad con menos de 300 publicaciones es:{nombre_usuario_mayor_edad} con el producto de tipo {tipo_producto_usuario_mayor_edad}, su edad es {usuario_mayor_edad} años")

#3
if  contador_usuarios_cuenta_inactiva !=0:
    porcentaje_publicaciones_inactivas = (contador_usuarios_cuenta_inactiva * 100) / contador_usuario
    print(f"porcentaje de cuentas inactivas es de : {round(porcentaje_publicaciones_inactivas,2)} %")

#4
if contador_publicaciones_subasta != 0:
    promedio_edad_usuarios_subasta = acumulador_edad_tipo_subasta/contador_publicaciones_subasta
    print(f"el promedio de edad de los usuarios que eligieron publicacion del tipo subasta es:{round(promedio_edad_usuarios_subasta,2)} años") 

#5
if contador_cuenta_activa_tipo_producto > contador_cuenta_activa_tipo_servicio and contador_cuenta_activa_tipo_producto > contador_cuenta_activa_tipo_subasta:
    print("el tipo con mas publicaciones y con la cuenta inactiva es: ", TIPO_PRODUCTO)
if contador_cuenta_activa_tipo_servicio > contador_cuenta_activa_tipo_producto and contador_cuenta_activa_tipo_servicio > contador_cuenta_activa_tipo_subasta:
    print("el tipo con mas publicaciones y con la cuenta inactiva es: ", TIPO_SERVICIO)
if contador_cuenta_activa_tipo_subasta > contador_cuenta_activa_tipo_producto and contador_cuenta_activa_tipo_subasta > contador_cuenta_activa_tipo_servicio:
    print("el tipo con mas publicaciones y con la cuenta inactiva es: ", TIPO_SUBASTA)
    

        
        
    

    
   
    

        

    

