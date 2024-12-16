

PUBLICACIONES_MIN = 1
PUBLICACIONES_MAX = 1000
TIPO_PRODUCTO = "PRODUCTO"
TIPO_SERVICIO = "SERVICIO"
TIPO_SUBASTA = "SUBASTA"


CUENTA_ACTIVA = "SI"
CUENTA_INACTIVA = "NO"

contador_usuarios = 0
contador_usuario_inactivos_55 = 0
contador_cuenta_activa = 0
publicacion_tipo_servicio = 0
acumulador_edad_tipo_servicio = 0
contador_cuenta_activa_tipo_producto = 0
contador_cuenta_activa_tipo_servicio = 0
contador_cuenta_activa_tipo_subasta = 0


while contador_usuarios <= 1:
    
    nombre = input("Ingrese su nombre de usuario: ")

    edad = int(input("Ingrese su edad: "))
    while edad < 1:
        edad = int(input("ERROR, Ingrese una edad valida: "))
        
    productos = int(input("Ingrese la cantidad de productos: "))
    while productos < 0 :
        productos = int(input("ERROR, Ingrese una cantidad de productos valida: "))
        
    publicaciones = int(input("Ingrese la cantidad de publicaciones: "))
    while publicaciones < PUBLICACIONES_MIN or publicaciones > PUBLICACIONES_MAX:
        publicaciones = int(input("ERROR, la cantidad debe ser entre 0 y 1000 !!!: "))
        
    tipo = input (f"Ingrese su tipo de publicacion : [{TIPO_PRODUCTO} para producto][{TIPO_SERVICIO} para servicio][{TIPO_SUBASTA} para subasta]: ").upper()
    while tipo != TIPO_PRODUCTO and tipo != TIPO_SERVICIO and tipo != TIPO_SUBASTA:
        tipo=input("ERROR, Ingrese una opcion valida: ")
        
    cuenta = input(f"Ingrese cual es el estado de su cuenta?:  [{CUENTA_ACTIVA}, si esta activa][{CUENTA_INACTIVA}, no esta inactiva]: ").upper()
    while cuenta != CUENTA_ACTIVA and cuenta != CUENTA_INACTIVA:
        cuenta = input("ERROR, Ingrese una opcion valida: ")
    
    contador_usuarios += 1
    
    #1
    if cuenta == CUENTA_INACTIVA and tipo == TIPO_SERVICIO and edad < 55:
        contador_usuario_inactivos_55 += 1
    
    #3   
    if cuenta == CUENTA_ACTIVA:
        contador_cuenta_activa += 1
    if contador_cuenta_activa != 0:
        porcentaje_cuentas_activas = (contador_cuenta_activa* 100)/contador_usuarios
        
    #4
    if tipo == TIPO_SERVICIO:
        publicacion_tipo_servicio += 1
        acumulador_edad_tipo_servicio = acumulador_edad_tipo_servicio + edad
    if publicacion_tipo_servicio != 0:
        promedio_edad_tipo_servicio = acumulador_edad_tipo_servicio/publicacion_tipo_servicio
        
    #5
    if cuenta == CUENTA_ACTIVA and tipo == TIPO_PRODUCTO:
        contador_cuenta_activa_tipo_producto +=1
    elif cuenta == CUENTA_ACTIVA and tipo == TIPO_SERVICIO:
        contador_cuenta_activa_tipo_servicio +=1
    elif cuenta == CUENTA_ACTIVA and tipo == TIPO_SUBASTA:
        contador_cuenta_activa_tipo_subasta +=1
    
if contador_cuenta_activa_tipo_producto > contador_cuenta_activa_tipo_servicio and contador_cuenta_activa_tipo_producto > contador_cuenta_activa_tipo_subasta:
    print (f"el mayor tipo con cuenta activa es : {contador_cuenta_activa_tipo_producto}")
    if contador_cuenta_activa_tipo_servicio > contador_cuenta_activa_tipo_producto and contador_cuenta_activa_tipo_servicio > contador_cuenta_activa_tipo_subasta:
        print (f"el mayor tipo con cuenta activa es : {contador_cuenta_activa_tipo_servicio}")
        if contador_cuenta_activa_tipo_subasta > contador_cuenta_activa_tipo_servicio and contador_cuenta_activa_tipo_subasta > contador_cuenta_activa_tipo_producto:
            print (f"el mayor tipo con cuenta activa es : {contador_cuenta_activa_tipo_subasta}")
        

    
        
    
    
    print (f"el promedio de edad, de los usuarios tipo servicio es: {round(promedio_edad_tipo_servicio,2)} años")
    print(f"porcentaje de publicaciones activas: {round(porcentaje_cuentas_activas,2)} %")
    print ("cantidad de usuarios: ", contador_usuarios)    
    print ("cantidad de usuarios inactivos: ", contador_usuario_inactivos_55)
    


 