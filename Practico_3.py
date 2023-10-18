'''1- Escribir un programa que pida al usuario una palabra y 
la muestre por pantalla 10 veces.'''

# word = input("Ingrese una palabra: ")
# counter = 0 # La variable counter me ayuda a establecer un inicio en mi bucle while
# while counter < 10:
#     counter += 1
#     print(word)

'''2- Escribir un programa que pregunte al usuario su edad y 
muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)'''

# age = int(input("Ingrese su edad: "))
# if age > 0:
#     while True:
#         print(f"Felicidades por tu cumpleaños numero {(age-1)} ") # Incluyo el age-1 para que no se muestre la edad actual ingresada
#         age = age - 1
#         if age < 2:
#             break


'''3- Escribir un programa que pida al usuario un número entero positivo
y muestre por pantalla todos los números 
impares desde 1 hasta ese número separados por comas'''

# number = None # Defino a numero como None por si no ingresa nada

# while number is None or number <= 0:
#     number1 = input("Ingrese un numero entero positivo: ")
#     if number1.isdigit(): # Valido que el numero ingresado sea un digito numerico
#         number = int(number1)
#     else:
#         print("Ingrese un numero entero válido.")

# # Creo una lista donde se recorra el numero ingresado buscando los impares
# odds = [str(i) for i in range(1, number + 1) if i % 2 != 0]
# # Los concateno con una ',' utilizando la funcion .join
# odds_counts = ', '.join(odds)
# print(f"Números impares dentro de '{number}' :", odds_counts)

'''4- Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas'''

# number_positive = int(input("Ingrese un numero entero positivo: "))

# while number_positive < 0:
#     print("El numero ingresado debe ser entero positivo. Intente nuevamente")
#     number_positive = int(input("---> "))

# if number_positive >= 0:
#     while number_positive >= 0:
#         print(number_positive, end='')
#         if number_positive > 0:
#             print(',', end=' ')
#         number_positive -= 1


'''5- Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años, y muestre por pantalla el 
capital obtenido en la inversión cada año que dura la inversión.'''

# quantity = float(input("Ingrese la cantidad de dinero que desea invertir: "))
# interest = float(input("Ingrese la tasa de interes anual: "))
# years = int(input("Ingrese la cantidad de años que durara su inversion: "))

# duration = 0

# while duration < years:
#     capital = quantity + (quantity * (interest / 100))  # Operacion para conocer el valor de capital
#     duration += 1
#     quantity = capital
#     print(f"El capital obtenido por año es: {capital}")
#     continue


'''6- Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
como el de más abajo, de altura el número introducido.'''

# hight = int(input("Ingrese la altura del triángulo rectángulo: "))

# for i in range(1, hight + 1): # Mediante un for recorro cada elemento del numero ingresado y formo la piramide
#     print('*' * i) # El '*' cuenta como '1' entonces cada vez que i se aumente en 1, se agregara un '*'

'''7-  Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.'''

# for i in range(1, 11):
#     print(f'Tabla de multiplicar del {i}:') # Iterando los multiplicando obtengo las tablas
#     for j in range(1, 11):
#         resultado = i * j
#         print(f'{i} x {j} = {resultado}')
#     print("--------------------------------")

'''8- Escribir un programa que pida al usuario un número entero
y muestre por pantalla un triángulo rectángulo como el de más abajo.'''

# number = int(input("Ingrese un numero entero: "))

# for i in range(1, number+1, 2):
#     for k in range(0,i,2):
#         print(i-k, end= " ") #Restar el iterador i con el iterador k hace que solo se muestre 1 vez cada numero
#     print()

'''9- Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.'''

# password_original = input("Ingrese su contraseña: ") #Declaro la contraseña original

# while True: #El bucle se repite hasta que la confirmacion sea igual a la contraseña original
#     password_confirmation = input("Por favor, confirme su contraseña: ")
#     if password_original != password_confirmation:
#         print("Las contraseñas no coinciden. Intente nuevamente.")
#         continue
#     else:
#         print("Contraseña correcta. ¡Bienvenido!")
#         break

'''10- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no'''

# number = abs(int(input("Ingrese un numero entero: "))) #Utilizo la funcion abs para 'forzar' a que el numero sea positivo
# if number % 2 != 0:
#     print(f"El numero {number} es primo")
# else:
#     print(f"El numero {number} no es primo")


'''11- Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
una a una las letras de la palabra introducida empezando por la última'''

# word = input("Ingrese una palabra a su eleccion: ")

# for i in reversed(word): #La funcion reversed me devuelve un string de atras hacia adelante
#     print(i, end= "")

'''12- Escribir un programa en el que se pregunte al usuario por una
frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase'''

# phrase = input("Ingrese una frase: ").capitalize()
# letter = input("Ingrese una letra: ").capitalize()
# counter = 0
# for i in phrase:
#     if letter == i:
#         counter += 1

# if counter > 0:
#     print(f"La letra {letter.capitalize()} se encuentra {counter} veces en la frase introducida.")
# else:
#     print(f"La letra {letter.capitalize()} no se encuentra en la frase introducida.")

'''13- Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba
“salir” que terminará.'''

# entry = input("Ingrese una frase o palabra a su eleccion:\n")
# salir = "esto es un ecoo"
# print(entry)
# while salir == "esto es un ecoo":
#     eco = input("Si desea dejar de escuchar su eco, escriba la palabra 'salir'\n").lower()
#     if eco == "salir":
#         break
#     else:
#         new_eco = eco
#         print(new_eco)
#     continue

'''14- Escriba un programa que pida dos números enteros y escriba 
qué números son pares y cuáles impares desde el primero hasta el segundo.'''

# num1 = int(input("Ingrese un numero: "))
# num2 = int(input("Ingrese otro numero: "))
# if num1 < num2:
#     for i in range(num1, num2+1):
#         if i % 2 == 0:
#             print(f"El numero {i} es par")
#         else:
#             print(f"El numero {i} es impar")
# elif num2 < num1: 
#     for i in range(num2, num1+1):
#         if i % 2 == 0:
#             print(f"El numero {i} es par")
#         else:
#             print(f"El numero {i} es impar")
# elif num1 == num2:
#     num3 = num1
#     if num3 % 2 == 0:
#         print(f"El numero {num3} es par")
#     else:
#         print(f"El numero {num3} es impar") 

'''15- Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores'''

# numero = 0
# while numero <= 0:
#     numero = int(input("Ingrese un numero: "))

# for i in range(1, numero+1):
#     if numero % i == 0:
#         print(f"El numero {numero}, es divisible por {i}")


'''16- Escriba un programa que pregunte cuántos números se van a introducir, pida 
esos números y escriba cuántos negativos ha introducido'''

# cant_numeros = int(input("Cuantos numeros va a introducir? "))
# cont_neg = 0

# for i in range(1, cant_numeros+1):
#     i = int(input(f"Ingrese el {i} numero: "))
#     if i < 0:
#         cont_neg += 1

# print("La cantidad de numeros negativos ingresados son: ",cont_neg)

'''17- Solicitar al usuario que
ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas)'''

# # Solicitar al usuario que ingrese una frase
# phrase = input("Ingrese una frase: ")
# vocals = []

# for caracter in phrase:
#     # Verificar si el carácter es una vocal y no está en la lista de vocales
#     if caracter.lower() in "aeiou" and caracter.lower() not in vocals:
#         # Agregar la vocal a la lista
#         vocals.append(caracter.lower())

# print("Vocales en la frase:", vocals)


'''18- Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. 
#La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos 
#números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…'''

# fibonacci = [0, 1]

# for _ in range(8):
#     # Calcular el siguiente número como la suma de los dos anteriores
#     siguiente_numero = fibonacci[-1] + fibonacci[-2]
    
#     fibonacci.append(siguiente_numero)

# print("Los primeros 10 números de la sucesión de Fibonacci son:", fibonacci)

'''19- Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad,
que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y 
otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. 
El programa deberá comprobar que las cantidades ingresadas sean positivas'''


# current_savings = 0
# saving_goal = float(input("Ingrese la cantidad que desea ahorrar: $"))
# money = 0  

# while current_savings < saving_goal:
#     try:
#         money = float(input("Cuánto dinero desea ingresar?: $"))
#         if money < 0:
#             print("Error. Por favor, ingrese una cantidad positiva.")
#         else:
#             current_savings += money
#     except ValueError:
#         print("Error: Por favor, ingrese un número válido.")

# print(f"¡Felicidades! Has alcanzado tu objetivo de ahorro de ${saving_goal}.")
# print(f"Total ahorrado: ${current_savings}")

'''20-	Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, 
mostrar la sumatoria de todos los números ingresados.'''
# number = int(input("Ingresa un numero entero, presione 0 para salir: "))
# count = number
# while number:
#     number = int(input("Ingresa otro numero entero, presione 0 para salir: "))
#     count += number
# print(f"La suma de los numeros enteros ingresados es {count}")

'''21-	Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. 
Informar cuál fue el mayor número ingresado.'''

# major = 0

# while True:
#     number = int(input("Ingresa un numero entero positivo, presione 0 para salir: "))

#     if number == 0:
#         break
#     elif number < 0:
#         print("El numero ingresado debe ser positivo!!")
#     elif number > major:
#         major = number

# print(f"El numero mayor es: {major}")


'''22-	Solicitar al usuario que ingrese números enteros positivos y, por cada uno, 
imprimir la suma de los dígitos que lo componen. 
La condición de corte es que se ingrese el número -1. 
Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.'''

# # Ingresa el primer numero
# number = int(input("Ingresa un numero entero positivo, presione -1 para salir: "))
# # Contador de pares
# count_pair = 0
# while number != -1:
#     # Valida que los numeros no sean negativos
#     if number < 0:
#         print("El numero ingresado no es valido, por favor intente nuevamente: ")
#     number_str = str(number)
#     # Hace la suma de los digitos
#     sum_number = 0
#     for i in number_str:
#         number_int = int(i)
#         sum_number += number_int
#     # Encuentra numeros pares
#     if number % 2 == 0:
#         count_pair += 1
#     print(f"la suma de los digitos del numero introducido es: {sum_number}")
#     number = int(input("Ingresa otro numero entero positivo, presione -1 para salir: "))
# print(f"la cantidad de pares son {count_pair}")


'''23-	Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
(se desconoce la cantidad de datos que cargará, 
la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.'''

# amount_buys = []
# amount = float(input("introduce el monto de la compra realizada, ingrese 0 para salir: "))

# while amount:
#     amount_buys.append(amount)
#     amount = float(input("introduce el monto de otra compra realizada, ingrese 0 para salir: "))
# print(f"los montos de las compras son: {amount_buys}")

'''24-	Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
Al finalizar, informar el total a pagar teniendo que cuenta que, 
si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.'''

# amount_pay = float(input("Ingrese el monto a pagar: "))

# while amount_pay < 0:
#     amount_pay = float(input("Ingrese un nuevo monto a pagar: "))

# if amount_pay > 1000:
#     price_off = amount_pay - (amount_pay*0.10)
#     print(f"El monto a pagar seria: ${price_off}")
# else:
#     print(f"El monto a pagar seria: ${amount_pay}")

'''25-	Dado un número entero positivo, mostrar su factorial. 
El factorial de un número se obtiene multiplicando todos los números enteros positivos 
que hay entre el 1 y ese número. 
El factorial de 0 es 1.'''

# number = int(input("Ingrese un número entero positivo: "))

# factorial = 1

# if number < 0:
#     print("El factorial no está definido para números negativos.")
# elif number == 0:
#     print("El factorial de 0 es 1.")
# else:
#     for i in range(1, number + 1): # Mediante un bucle recorro los numeros y los multiplico por el iterador
#         factorial *= i

#     print(f"El factorial de {number} es: {factorial}")
