
sucursales = [
            ["Sucursal 1", 750, 950, 860, 820],
              ["Sucursal 2",750, 750, 460, 520],
              ["Sucursal 3", 750, 510, 260, 320],
              ["Sucursal 4", 750, 450, 560, 720],
             ["Sucursal 5",750, 250, 860, 520],
              ]
productos = ["detergente", "desinfectante", "jabón líquido", "lavandina"]
precios = [1500, 2000, 3000, 1000]

#1

def cargar_stock(sucursales):
    for i in range(len(sucursales)):
        print(f"carga de stock para sucursal {sucursales[i][0]}")
        for j in range(1, len(sucursales)):
            stock_a_agregar = int(input(f"Ingrese la cantidad de stock para el producto: {productos[j-1]}"))
            #validar que no se supere las 5000 unidades
            
            if sucursales[i][j] + stock_a_agregar <= 5000:
        
                #procedo
                stock_actual = sumar_productos(sucursales[i])
                if stock_actual + stock_a_agregar <= 15000:
                    sucursales[i][j] += stock_a_agregar
                else:
                    print("no se puede superar el total de 15000 unidades por sucursal")
            else:
                print("No se puede superar las 5000 unidades de este producto")






# 2
def calcular_total_producto_por_sucrusal(sucursales):
    for i in range(len(sucursales)):
        total_productos = 0
        for j in range(1,len(sucursales[i])):
            total_productos += sucursales[i][j]
        print(f"la sucursal{sucursales[i][0]}tiene {total_productos}")
        
        
calcular_total_producto_por_sucrusal(sucursales)



#3

def producto_con_menor_Stock_por_sucursal(sucursales):
    for i in range(len(sucursales)):
        indice_menor_producto = -1
        for j in range(1,len(sucursales[i])):
            if j == 1 or sucursales[i][j] < sucursales[i][indice_menor_producto]:
                indice_menor_producto = j
        print(f" el producto con menos stock en la sucursal {sucursales[i][0]}es {sucursales}[i][indice_menor_producto]")
        
            
print(producto_con_menor_Stock_por_sucursal(sucursales))  

#4

def mostrar_productos_con_mayor_stock(sucursales, productos):
    for i in range(len(productos)):
        indice_maximo = -1
        for j in range(len(sucursales)):
            if j == 0 or sucursales[j][i+1] < sucursales[indice_maximo][i+1]:
                indice_maximo = j
        print(f"el maximo stock de {productos[i]} esta en la sucursal {sucursales[indice_maximo][0]}")
        
  
  
  
#5


def buscar_sucursal_con_mayor_valor_de_stock(sucursales, lista_precios): 
    indice_mayor_valor = -1
    mayor_valor = 0
    for i in range(len(sucursales)): 
        aux = 0   
        for j in range(1,len(sucursales[i])): 
            aux += sucursales [i][j] * lista_precios[j-1]
        if i == 0 or aux  > mayor_valor:
            indice_mayor_valor = i
            mayor_valor = aux
            
    print(f"la sucursal con mayor valor de stock es {sucursales[indice_mayor_valor][0]}")
            
#6

def mostrar_sucursales_con_mas_de_10000_unidades(sucursales):
    
    for i in range(len(sucursales)):
        total_productos = sumar_productos(sucursales[i])
        if total_productos >= 10000:
            print(f"la sucursal{sucursales[i][0]}tiene mas de 10000 productos{total_productos}")       
            

#7
def calcular_porcentaje_de_productos(sucursales, productos):
    #obtenemos total de productos
    total_productos = 0
    for i in range(len(sucursales)):
        total_productos += sumar_productos(sucursales[i])
    
    lista_total_productos = [0] * len (productos)
    for i in range(len(productos)):
        for j in range(len(sucursales)):
            lista_total_productos[i] += sucursales [j][i+1]
            
    for i in range(len(lista_total_productos)):
        print(f"{total_productos / total_productos *100} ")
        
        
def buscar_maximo(lista):
    indice_maximo = -1
    for i in range(len(lista)):
        if i == 0 or lista[i] > lista [indice_maximo]:
            indice_maximo = i
            
    return indice_maximo



#8

def informar_valor_total_por_sucursal(sucursales, precios): 
    lista_valores = [0] * len(sucursales)
    for i in range(len(sucursales)): 
        for j in range(1,len(sucursales[i])): 
            lista_valores[i] += sucursales [i][j] * precios[j-1]
    print(lista_valores)
    
    for i in range(len(lista_valores)-1):
        for j in range(i+1, len(lista_valores)):
            if lista_valores[i] < lista_valores[j]:
                aux = lista_valores[i]
                lista_valores[i] = lista_valores[j]
                lista_valores[j] = aux
    print(lista_valores)
    
informar_valor_total_por_sucursal(sucursales, precios)

        
         