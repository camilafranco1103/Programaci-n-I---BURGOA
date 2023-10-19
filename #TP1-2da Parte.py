#Trabajo Práctico1-2da Parte
#Calcular el perímetro y área de un rectángulo dada su base y su altura.

base_rectangulo=5
altura_rectangulo=3
perimetro=base_rectangulo+altura_rectangulo
area=altura_rectangulo*base_rectangulo
print("El perímetro del rectángulo es = ",perimetro," y el área es = ",area)
print("--------------------------------------------------------")

#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa



#Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
primer_num=float(input("Ingrese primer numero: "))
segundo_num=float(input("Ingrese un segundo numero: "))
suma=primer_num+segundo_num
resta=primer_num-segundo_num
division=primer_num/segundo_num
multip=primer_num*segundo_num
print("La suma de ambos numeros es = ",suma," la resta = ",resta," ,la división = ",division," y la mutiplcacion = ",multip)
print("--------------------------------------------------------")

# 4. Escribir un programa que convierta un valor dado en grados Fahrenheit a 
# grados Celsius.
#°C=9/5​×(°F−32)
grados=float(input("Ingrese los el valor en grados Fahrenheit: "))
grados_Celsius = (grados-32)*5/9
print("El valor en grados Fahrenheit:",grados," convertido a grados Celsius es: ",grados_Celsius)
print("--------------------------------------------------------")
# 5. ¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?

 #   a) A = input(nombre, “¿Cuál es tu canción favorita?”)
    #En esta instruccion lo que está mal, es que al querer imprimir una pregunta incluyendo
    #el nombre del usuario(la cual hay que definir previamente),lo quiera hacer 
    # en un input,yo lo solcionaria así:
    #print(nombre," cuál es tu cancion favorita?")
    #a=input()

    #b) precio = input(“Precio: “)
    #total = precio + (precio * 0.1)

    #c) edad = int(input(“Edad: “))
    #print(tu edad es, edad)
    #Esta instruccion tiene el error de que al print le faltan comillas, lo adecuado
    #sería print("Tu edad es: ",edad)

    #d) edad = int(input(“Edad: “))
    #print(“Veamos si tu edad es 18…”, edad=18)
    #El problema en esta instrucción es que así no se comparan valores, lo adecuado sería
    #utilizar un condicional como por ejemplo:
    # (edad = int(input(“Edad: “))
    # if edad == 18: 
    # print("Tu edad es igual a 18"))

#Calcular la media de tres números pedidos por teclado.
num_one=float(input("Ingrese un numero: "))
num_two=float(input("Ingrese otro numero: "))
num_three=float(input("Ingrese otro numero: "))
media=(num_one+num_two+num_three)/3
print("La media de los 3 numeros es: ",media)
print("--------------------------------------------------------")

#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla 
# a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas 
# y 40 minutos.
minutos=float(input("Ingrese la cantidad de minutos: "))
