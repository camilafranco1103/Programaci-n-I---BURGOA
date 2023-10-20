#Ejercicio Funciones
#Solicitar al usuario números hasta q ingrese 0. Por cada uno mostrar la suma de sus dígitos.
#Al finalizar mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos.
from prueba import * 
suma_num_ingresados = 0
suma_todos_los_digitos = 0

num = int(input("Ingrese un numeros para mostrar la suma de sus digitos, para salir presione 0: "))  
while num != 0:
    result = add_nums(num)
    print(f"La suma de los digitos del numero {num} es {result}")
    suma_num_ingresados += num
    suma_todos_los_digitos += result
    num = int(input("Ingrese otro numero --> ")) 
    
print(f"La suma de los numeros ingresados es: {suma_num_ingresados}")
print(f"La sumatoria total de los digitos ingresados es: {suma_todos_los_digitos}")
print("Adios!")
