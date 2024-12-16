# Crear una función que reciba una cadena y un caracter. 
# La función deberá devolver el índice en el que se encuentre 
# la primera ocurrencia de dicho caracter, 
# o -1 en caso de que no esté
def contar_vocal(cadena, caracter):
    
    indice = 0
    for i in range(len(cadena)):
        if i == caracter:
            indice += 1
        return indice
    else:
        return -1
    

cadena = "murcielaguito"
caracter = "o" 
print(contar_vocal(cadena, caracter))

   