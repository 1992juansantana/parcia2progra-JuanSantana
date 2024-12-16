# def calcular_factorial(numero):
#     factorial = 1
#     if numero > 0:
#         factorial = numero * calcular_factorial (numero-1)
#     return factorial

# def calcular_factorial(numero):
#     if numero > 0:
#         return  numero * calcular_factorial(numero-1)
#     else:
#         return 1


#SECUENCIA NO RECURSIVA:
# def calcular_factorial(numero):
#     resultado = 1
#     while numero > 0:
#         resultado = resultado * numero
#         numero = numero -1
#     return resultado
   
    
# print(calcular_factorial(-3))



#secuencia de fibonacci
#implementacion de recursividad

# def secuencia_de_fibonacci(elemento : int):
#     retorno = 0
#     if elemento == 1:
#         return 1
#     elif elemento > 1:
#         return secuencia_de_fibonacci(elemento-1) + secuencia_de_fibonacci(elemento-2)
#     return retorno


# def secuencia_de_fibonacci(numero):
#     contador = 2
#     resultado = 0
#     numero_uno = 1
#     numero_dos = 1
#     if numero == 1 or numero ==2:
#         return 1
#     while contador < numero:
#         contador +=1
#         resultado = (numero_uno + numero_dos)
#         numero_uno = numero_dos
#         numero_dos = resultado
        
#     return resultado

# print(secuencia_de_fibonacci(-5))
# print(secuencia_de_fibonacci(1))
# print(secuencia_de_fibonacci(2))
# print(secuencia_de_fibonacci(3))
# print(secuencia_de_fibonacci(4))
# print(secuencia_de_fibonacci(5))


def factorial(numero):
    fact = 1
    for i in range(1, numero + 1):
        fact = fact + i
    return fact



def factorial_recur(numero):
    
    if numero == 0:
           return 1
    else:
        return factorial_recur(numero -1) + numero

print(factorial(4))
print(factorial_recur(4))  


    
    
    




