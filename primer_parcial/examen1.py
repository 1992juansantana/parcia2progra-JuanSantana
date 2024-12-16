import examen_funciones

sucursales = ["Sucursal 1", "Sucursal 2", "Sucursal 3", "Sucursal 4", "Sucursal 5"]
productos = ["detergente", "desinfectante", "jabón líquido", "lavandina"]
precios = [1500, 2000, 3000, 1000]



def menu(inventario):
    

    print(" --- MENU DE OPCIONES ---")
    print("1- Registrar stock.")
    print("2- Calcular el total de productos por sucursal). ")
    print("3- Producto con menor stock por sucursal")
    print("4- Máxima cantidad de unidades por producto")
    print("5- Sucursal con mayor valor de stock.")
    print("6- Sucursales con más de 10,000 unidades.")
    print("7- Porcentaje de cada producto sobre el total.")
    print("8- Generar informe de valor total por sucursal.")
        
    opcion_menu = int(input("Ingrese su opción: "))
        
    if opcion_menu == 1: 
        examen_funciones.registrar_stock(inventario)
            
    elif opcion_menu == 2:
        examen_funciones.calcular_productos(inventario)

    elif opcion_menu == 3:
        examen_funciones.producto_menor_stock_por_sucursal(inventario)

    elif opcion_menu == 4:
        examen_funciones.mostrar_productos_con_mayor_stock(inventario)

    elif opcion_menu == 5:
        examen_funciones.sucursal_mayor_unidades
            
    elif opcion_menu == 6:
        print("OPCION NO DISPONIBLE")
            
    elif opcion_menu == 7:
        print("OPCION NO DISPONIBLE")
            
    elif opcion_menu == 8:
        print("OPCION NO DISPONIBLE")

    else:
        print("Opcion incorrecta.")

menu(inventario)