'''1-	Crear un programa que reciba el número de años que tiene nuestra computadora y 
muestre en la consola que el computador es nuevo si es menor o igual a 2 años y que el 
computador es viejo si es mayor a 2 años.'''

# year_computer= int(input("Ingrese la cantidad de años de uso de su computadora: "))
# if year_computer <= 2: 
#     print("el computador es nuevo")
# else:
#     print("el computador es viejo")

'''2-	Hacer que el programa anterior muestre un mensaje de error si el usuario 
digita un número negativo.'''

# year_computer= int(input("Ingrese la cantidad de años de uso de su computadora: "))
# while year_computer < 0: 
#     year_computer = int(input("Ingrese un numero positivo: "))
# if year_computer <= 2:
#     print("el computador es nuevo")
# else:
#     print("el computador es viejo")

'''3-	Solicitar al usuario que ingrese los nombres de dos personas, los cuales se 
almacenarán en dos variables. A continuación. Imprimir ‘coincidencia’ si ambos nombres 
comienzan con la misma letra. Si no es así, imprimir ‘no hay coincidencia’.'''

# name_1= input("introduce el primer nombre: ").lower()
# name_2 = input("introduce el segundo nombre: ").lower()

# if name_1[0] == name_2[0]:
#     print("coincidencia")
# else:
#     print("no hay coincidencia")

'''4-	Crear un programa que permita al usuario elegir un candidato por el cual votar. 
Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verdad, 
candidato C por el partido azul.'''

# candidato = input("Ingrese el candidato a votar A,B o C: ").upper()
# while candidato != "A" and candidato != "B" and candidato != "C":
#     print("Ingrese un candidato valido")
#     candidato = input("Ingrese el candidato a votar A,B o C: ").upper()

# if candidato == "A":
#     print("Usted voto por el partido rojo")
# elif candidato == "B":
#     print("Usted voto por el partido verdad")
# elif candidato == "C":
#     print("Usted voto por el partido azul")

'''5-	Escribir un programa que solicite al usuario una letra, si es una vocal, 
mostrar el mensaje ‘Es vocal’.
Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de 
más de un carácter, informarle que no se puede procesar el dato.
'''

# vocal=input("introduce una vocal: ").lower()
# if len(vocal) > 1:
#     print("no se puede procesar el dato")
# elif vocal == 'a' or vocal == 'e' or vocal == 'i' or vocal == 'o' or vocal == 'u':
#     print("es vocal")
# else:
#     print("no es una vocal")

'''6-	Hacer un programa que permita saber si un año es bisiesto. Para que un año 
sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que 
también sea divisible por 400.'''

# bisiesto = int(input("introduce el año: "))
# if bisiesto % 4 == 0 and bisiesto % 100 != 0: 
#     print("el año es bisiesto")
# elif bisiesto % 100 == 0 and bisiesto % 400 == 0:
#     print("el año es bisiesto")
# else: 
#     print("el año no es bisiesto")

'''7-	Escribí un programa para solicitar al usuario tres números y mostrar en 
pantalla al menor de los tres.'''

# number_1 = int(input("introduce el numero 1: "))
# number_2 = int(input("introduce el numero 2: "))
# number_3 = int(input("introduce el numero 3: "))
# menor = 0
# if number_1 <= number_2 and number_1 <= number_3:
#     menor = number_1
# elif number_2 <= number_3:
#     menor = number_2
# elif number_3 <= number_1:
#     menor = number_3

# print("numero menor es: ", menor)

'''8-	Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. 
Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y 
contraseña correctos. Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, 
mostrar “Acceso denegado”.'''

# username= input("Introduce un nombre de usuario: ").lower()
# password = input("Introduce una contraseña: ").lower()

# if username == "gwenevere" and password == "excalibur":
#     print("Usuario y contraseña correctos.")
# else:
#     print("Acceso denegado")

'''9-	Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo 
y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los 
hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que 
pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.'''

# name = input("introduce un nombre: ").upper()
# sex = input("introduzca su sexo F o M: ").upper()

# if name[0] <= "M":
#     if sex[0] == "F":
#         print("forma parte del grupo A")
#     else:
#         print("forma parte del grupo B")
# elif name[0] >= "N":
#     if sex[0] == "M":
#         print("forma parte del grupo A")
#     else:
#         print("forma parte del grupo B")

'''10-	Escribir un programa para una empresa que tiene salas de juegos para todas las 
edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por 
entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la 
entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años 
debe pagar $500 y si es mayor de 18 años, $1000.'''

# edad = abs(int(input("cuantos años tienes: ")))

# if edad <= 4:
#     print("Ingresa gratis")
# elif edad > 4 and edad <= 18:
#     print("La entrada cuesta $500")
# else:
#     print("La entrada cuesta $1000")

'''11-	La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.
•	Ingredientes vegetarianos: Pimiento y tofu.
•	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas
    la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o 
    no y todos los ingredientes que lleva.
'''

# pepper = "pimiento"
# tofu = "tofu"
# pepperoni = "peperoni"
# ham= "jamon"
# salmon = "salmon"

# pizza = input("Pizza vegetariana S/N: ").upper()

# if pizza == "S" or pizza == "N":
#     if pizza == "S":
#         print("los ingredientes disponibles son: ", pepper, tofu)
#         pick= input("elige un ingrediente: ")
#         if pick == pepper:
#             pizza_v = "la pizza elegida es vegetariana y contiene: mozzarella, tomate y " + pepper
#             print(pizza_v)
#         elif pick == tofu:
#             pizza_v = "la pizza elegida es vegetariana y contiene: mozzarella, tomate y " + tofu
#             print(pizza_v)
#         else:
#             print("La opcion no es valida")
#     else:
#         print("los ingredientes disponibles son: ", pepperoni,ham,salmon)
#         pick = input("elige un ingrediente: ")
#         if pick == pepperoni:
#             pizza_c = "la pizza elegida no es vegetariana y contiene: mozzarella, tomate y " + pepperoni
#             print(pizza_c)
#         elif pick == ham:
#             pizza_c = "la pizza elegida no es vegetariana y contiene: mozzarella, tomate y " + ham
#             print(pizza_c)
#         elif pick == salmon:
#             pizza_c = "la pizza elegida no es vegetariana y contiene: mozzarella, tomate y " + salmon
#             print(pizza_c)
#         else:
#             print("La opcion no es valida")
# else:
#     print("la opcion no es valida")


'''12-	Escriba un programa que pida el año actual y un año cualquiera y que escriba 
cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.'''

# current_year = int(input("introduzca el año actual: "))
# random_year = int(input("introduzca un año cualquiera: "))

# if current_year <= random_year:
#     years_to_come= abs(current_year - random_year)
#     print("faltan para llegar ", years_to_come,"años")
# elif current_year > random_year:
#     years_passed =  abs(current_year - random_year)
#     print("han pasado, ", years_passed,"años")

'''13-	Escriba un programa que pida dos números enteros y que escriba si el mayor es 
múltiplo del menor. Haciendo que el programa avise cuando se escriben valores negativos o 
nulos.'''

# number_1 = int(input("ingrese primer numero: "))
# number_2 = int(input("ingrese segundo numero: "))

# major = 0

# if number_1 >= 0 and number_2 >= 0:
#     if number_1 > number_2:
#         major = number_1
#         if major % number_2 == 0:
#             print("el numero mayor es multiplo del menor")
#         else:
#             print("el numero mayor no es multiplo del menor")
#     else:
#         major = number_2
#         if major % number_1== 0:
#             print("el numero mayor es multiplo del menor")
#         else:
#             print("el numero mayor no es multiplo del menor")
# else:
#     print("el numero ingresado es negativo o nulo")

'''14-	Escriba un programa que pida los coeficientes de una ecuación de primer grado 
(a x + b = 0) y escriba la solución.
Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución 
única, o que todos los números sean solución. Se recuerda que la fórmula de las soluciones 
es 
x = -b / a
'''
# a = float(input("Ingrese el coeficiente 'a': "))
# b = float(input("Ingrese el coeficiente 'b': "))

# if a == 0:
#     if b == 0:
#         print("La ecuación tiene infinitas soluciones.")
#     else:
#         print("La ecuación no tiene solución.")
# else:
#     solucion = -b / a
#     print("La solución de la ecuación ", a, "x + ", b," = 0 es x =",solucion,".")

'''15-	Escriba un programa que pregunte primero si se quiere calcular el área de un 
triángulo o la de un círculo. Si se contesta que se quiere calcular el área de un triángulo 
(escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el 
área. Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el 
programa tiene que pedir entonces el radio y escribir el área.'''

# opcion = input("¿Quieres calcular el área de un triángulo (T) o un círculo (C)? ").upper()

# if opcion == "T":
#     base = float(input("Ingrese la base del triángulo: "))
#     altura = float(input("Ingrese la altura del triángulo: "))
#     area_triangulo = 0.5 * base * altura
#     print(f"El área del triángulo es: {area_triangulo}")
# elif opcion == "C":
#     radio = float(input("Ingrese el radio del círculo: "))
#     area_circulo = 3.14159 * radio ** 2
#     print(f"El área del círculo es: {area_circulo}")
# else:
#     print("Opción no válida. Por favor, ingresa 'T' para triángulo o 'C' para círculo.")

'''16-	Haz una calculadora básica pida al usuario dos valores, a y b.
Según la opción que desean, realizar la operación:
•	Si operación es 1 entonces debemos ver el resultado de a + b
•	Si operación es 2 entonces debemos ver el resultado de a * b
•	Si operación es 3 entonces debemos ver el resultado de a - b
•	Si operación es 4 entonces debemos ver el resultado de a / b
'''
# a = float(input("Ingrese el primer valor (a): "))
# b = float(input("Ingrese el segundo valor (b): "))

# print("Opciones de operación:")
# print("1. Suma")
# print("2. Multiplicación")
# print("3. Resta")
# print("4. División")
# operacion = int(input("Ingrese el número de la operación que desea realizar: "))

# if operacion == 1:
#     resultado = a + b
#     print(f"El resultado de {a} + {b} es: {resultado}")
# elif operacion == 2:
#     resultado = a * b
#     print(f"El resultado de {a} * {b} es: {resultado}")
# elif operacion == 3:
#     resultado = a - b
#     print(f"El resultado de {a} - {b} es: {resultado}")
# elif operacion == 4:
#     if b != 0:
#         resultado = a / b
#         print(f"El resultado de {a} / {b} es: {resultado}")
#     else:
#         print("Error: No se puede dividir por cero.")
# else:
#     print("Opción no válida. Por favor, ingrese un número del 1 al 4 para seleccionar una operación válida.")

'''17-	Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si 
es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o 
domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.'''

# dia_semana = input("Ingrese un día de la semana: ").lower()

# if dia_semana == "lunes":
#     print("¡Es el comienzo de la semana! Ánimo, ¡vamos a empezar!")
# elif dia_semana == "viernes":
#     print("¡Viernes al fin! El fin de semana está cerca. ¡Felicidades!")
# elif dia_semana == "sabado" or dia_semana == "domingo":
#     print("¡Es fin de semana! Disfruta y relájate.")
# else:
#     print("Este no es un día válido de la semana. Por favor, ingrese un día válido.")

'''18-	Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si 
trabajó horas extras y mostrar esta cantidad.
Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más 
que las horas laborales comunes.
'''
# horas_trabajadas = float(input("Ingrese el total de horas trabajadas en el mes: "))
# salario_por_hora = float(input("Ingrese el salario por hora: "))

# jornada_minima = 48

# if horas_trabajadas > jornada_minima:
#     horas_extras = horas_trabajadas - jornada_minima
#     salario_normal = jornada_minima * salario_por_hora
#     salario_horas_extras = horas_extras * (salario_por_hora * 1.1)
#     salario_total = salario_normal + salario_horas_extras
#     print("Ha trabajado ",horas_extras,"horas extras.")
#     print("Salario total: $",salario_total)
# else:
#     salario_total = horas_trabajadas * salario_por_hora
#     print("No ha trabajado horas extras.")
#     print("Salario total: $",salario_total)

'''19-	Determinar cuánto se debe pagar por una cantidad de lápices considerando que si 
son 1000 o más, existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es 
de $60; de lo contrario no hay descuento.'''

# costo_por_lapiz = 60

# cantidad_lapices = int(input("Ingrese la cantidad de lápices a comprar: "))

# if cantidad_lapices >= 1000:
#     descuento = 0.07
#     costo_total = cantidad_lapices * costo_por_lapiz * (1 - descuento)
# else:
#     costo_total = cantidad_lapices * costo_por_lapiz
# print("El costo total a pagar es: $" + str(round(costo_total)))

'''20-	Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si 
su promedio de cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.'''

# nota_1 = float(input("ingrese la primera nota: "))
# nota_2 = float(input("ingrese la segunda nota: "))
# nota_3 = float(input("ingrese la tercera nota: "))
# nota_4 = float(input("ingrese la cuarta nota: "))

# promedio = (nota_1+nota_2+nota_3+nota_4)/4

# if promedio >= 6:
#     print("Aprobado el promedio es: ", promedio)
# else:
#     print("Desaprobado el promedio es: ", promedio)



