#TP-4
#Cree un bucle while con las siguientes características:

#• El valor inicial de la variable x será 0.
#• El valor del incremento será 1.
#• La condición de salida del bucle será mayor o igual a 30.
#• La ejecución debe interrumpirse cuando x es igual a 15.
#• Debes imprimir la siguiente frase cada vez que se ejecuta el bucle: 
#'El valor del bucle es: ' + x.
#• Debes saltarte las ejecuciones con el valor de x en 4, 6 y 10.
#• En cada salto de ejecución, debe mostrar los valores saltados con este mensaje:
# 'El valor ' + x ' de x fue omitido'.
#• Cuando se interrumpe la ejecución del bucle se debe mostrar un mensaje indicándolo: 
#'La ejecución del bucle se interrumpe cuando x era' + x.
"""
x= 0

while x <= 30 :
    x= x+1
    if x ==4 or x==6 or x== 10:
        print(f"El valor {x} de x fue omitido")
    else:
        print(f"El valor del bucle: {x}")
    if x ==15:
        print("La ejecución del bucle se interrumpió cuando x vale 15")
        break
        
        """
#1.Escriba un programa que acepte una secuencia de líneas e imprima todas las 
#lineas convertidas en mayúsculas. Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.
"""
lines = []
while True:
    # ingreso de linea
    line = input("Ingrese una linea: ")
    # condicion para guardar en la lista
    if line:
        lines.append(line.upper())
    else:
        # finaliza el bucle
        break

# imprime el resultado de las lineas
print("Estas son tus lineas: ")
for line in lines:
    print(line)
"""
#2. Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
#La bitácora de operaciones tiene la siguiente forma:
#D 100
#R 50

#D 100 significa que depositó 100 pesos
#R 50 significa que retiró 50 pesos
"""
bank_account=0

while True:
    print("Elija la opción que desee:")
    print("a-INGRESAR DINERO")
    print("b-RETIRAR DINERO")
    print("c-SALIR")
    opcion=input("-->").lower()
    if opcion == "a":
        money = float(input("Ingrese cantidad de dinero: $ "))
        if money <=0:
            print("Ingrese un numero positivo!!")
            
        else:
            bank_account += money

    elif opcion == "b":
        extraction=float(input("Cuanto dinero desea retirar?: $ "))
        if extraction <=0:
            print("Ingrese un numero positivo!!")
            
        elif bank_account < extraction:
            print(f"Fondo insuficiente \n Usted posee ${bank_account}")
        else:
            bank_account -= extraction

    elif opcion == "c":
        print(f"Cuenta bancaria = ${bank_account}")
        break

    else:
        print("Opcion invalida, ingrese una opcion correcta")
"""

#3.Escribir un programa que solicite el ingreso de una cantidad indeterminada de números 
# mayores que 1, finalizando cuando se reciba un cero.
#Imprimir la cantidad total de números primos ingresados.
"""
num = int(input("Ingrese los números que quiera, para salir presione 0: "))
es_primo = 0

while num != 0:
    if num < 0:
        print("Ingrese un número positivo")
    else:
        divisores = 0
        for i in range(2, num):
            if num % i == 0:
                divisores += 1
                
        if divisores == 0:
            es_primo += 1
    num = int(input("Ingrese otro número --> "))
    if num == 0:
        print(f"La cantidad de números primos que ingresó es: {es_primo}")
        print("Adiós!")
        break
"""
# 4. Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los 
# años en ese rango, que sean bisiestos y múltiplos de 10.
#Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
"""
year_one=int(input("Ingrese el primer año: "))
while year_one<=1000 :
    print("Ingrese el un año de 4 cifras: ")
    year_one=input("-->")

year_two=int(input("Ingrese el segundo año: "))
while year_two<=1000 :
    print("Ingrese el un año de 4 cifras: ")
    year_two=input("-->")

for i in range(year_one, year_two+1):     
    if i % 4 == 0 and i % 100 != 0: 
        if i % 10 == 0:
            print(f"El año {i} es bisiesto y multiplo de 10")
        else:
            print(f"El año {i} es bisiesto pero no multiplo de 10")
    elif i % 100 == 0 and i % 400 == 0:
        if i % 10 == 0:
            print(f"El año {i} es bisiesto y multiplo de 10")
        else:
            print(f"El año {i} es bisiesto pero no multiplo de 10")
    else: 
        print(f"El año {i} no es bisiesto")

"""
# 5.Escribe un programa que imprima todos los números 
# pares del 1 al 20 usando un bucle for. Utiliza la 
# declaración continue para omitir los números impares.
'''
for i in range(1,20):
    if i % 2 == 0:
        print(f"El numero {i}, es par")
    else:
        continue
'''
#6.Crea una lista de números y utiliza un bucle for para
#encontrar un número específico. Cuando encuentres el número, usa break para salir del bucle.
'''
import random


longitud_lista = 20

mi_lista = [random.randint(1, 100) for _ in range(longitud_lista)]
num = int(input("Ingrese el numero a encontrar: "))
for i in range (len(mi_lista)): 
    if num == mi_lista[i]:
        print("Has acertado al numero!!")
    elif num not in mi_lista:
        print("No se ha encontrado!!")
    else:
        continue

print(mi_lista)
'''

# 7.Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3).
# Utiliza un bucle while para permitir al usuario seleccionar una opción. Si el usuario 
# ingresa "0", utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).
'''
lista = {1,2,3}
opcion = int(input(f"Ingrese la opcion que desee {lista}: "))
opcion1 = 0
opcion2 = 0
opcion3 = 0
while opcion != 0:
    if opcion < 1 or opcion > 3:
        print("Ingrese opcion valida")
    if opcion == 1:
        print("Opcion 1")
        opcion1 += 1
    elif opcion == 2:
        print("Opcion 2")
        opcion2 += 1
    elif opcion == 3:    
        print("Opcion 3")
        opcion3 += 1
    if opcion == 0:
        print(f"Usted ingreso {opcion1} veces la opcion 1, {opcion2} la opcion 2 y {opcion3} la opcion 3")
        break
    opcion = input(f"Ahora ingrese otra opcion {lista}: ")
'''
