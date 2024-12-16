

#1
def registrar_stock(inventario):
      
    nueva_cantidad = int(input("Ingrese la nueva cantidad para el primer producto de la sucursal 1: "))
    if nueva_cantidad < 5000 or nueva_cantidad < 15000:
        inventario[0][0] = nueva_cantidad
    else: 
        print("LA CANTIDAD DEBE SER ENTRE 5000 A 15000 !!!: ") 
    return nueva_cantidad

  


#2
def calcular_productos(inventario):
    
    for i in range(len(inventario)):
        total = 0
        for cantidad in inventario[i]:
            total += cantidad
        print(f"El total de productos es la sucursal {i+1} es {total}")
        

    
#3    

def producto_menor_stock_por_sucursal(inventario):
    resultado = {}

    for sucursal in inventario:
        productos = list(inventario[sucursal])  # Convertimos a lista de tuplas
        menor_stock = None
        producto_menor = None

        for i in range(len(productos)):
            producto, cantidad = productos[i]
            if menor_stock is None or cantidad < menor_stock:
                menor_stock = cantidad
                producto_menor = producto

        resultado[sucursal] = (producto_menor, menor_stock)
    return resultado
    
    
    
    
#4    





#5
def sucursal_mayor_unidades(inventario):
    contador_sucursales = 0
    for sucursal in inventario:
        total_sucursal = 0
        for unidad in sucursal:
            total_sucursal += unidad
        if total_sucursal > inventario:
            contador_sucursales += 1
    return contador_sucursales
   
