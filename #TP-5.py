#1-Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es.
#  Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
"""
def validate_dni(num_dni):
    num_dni_str = str(num_dni)
#Convierto el documento en cadena para poder acceder a su longitud
    if len(num_dni_str) ==7 or len(num_dni_str)==8:
        return True
    else:
        return False


num_dni = input("Ingrese su número de DNI: ")
validate = validate_dni(num_dni)
if validate == True:
    print("EL DNI ingresado es váido")
else: 
    print("EL DNI ingresado no es válido!")
"""

#2-Escribir una función que, dado un string, retorne la longitud de la última palabra.
# Se considera que las palabras están separadas por uno o más espacios. 
# También podría haber espacios al principio o al final del string pasado por parámetro.
"""
def last_word(phrase):
    #Elimina los espacios en blanco al principio y al final de la cadena
    phrase = phrase.strip()
    #Divide la cadena en palabras usando los espacios en blanco como separadores
    words = phrase.split()
    
    
    if words:
        #La última palabra está en la posición [-1] de la lista de palabras
        ult_word = words[-1]
        
        longitud= len(ult_word)
        return longitud
    else:
        #Si no hay palabras en la cadena, retorna 0
        return 0


phrase = input("Ingrese una cadena: ")
result = last_word(phrase)
print(f"La longitud de la última palabra en la cadena es: {result}")

"""
#4-Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. 
# Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo.
"""
def is_multiple(num_one,num_two):
#Verifica si el 1er num es multiplo del 2do
    if num_one % num_two == 0:
        return True
    else:
        return False


number_one = int(input("Ingrese un número: "))
number_two = int(input("Ingrese otro número: "))
result = is_multiple(number_one,number_two)
if result == True:
    print(f"El primer número ({number_one}) es multiplo del segundo número ingresado ({number_two})")
else:
       print(f"El primer número ({number_one}) NO es multiplo del segundo número ingresado ({number_two})")
"""

#5-Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
# Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima 
# y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.
"""
def average_temperature(temp_max,temp_min,):
#Creo esta función que solo saca el promedio de la temp max y min
    average = (temp_max + temp_min) / 2
    return average
    

days = int(input("De cuántos días dese calcular la temperatura media: "))
for i in range(days):
    temp_maximum = float(input(f"Ingrese la temperatura máxima del día {i+1}° \n -->"))
    temp_minimum = float(input(f"Ingrese la temperatura mínima del del día {i+1}° \n -->"))
    medium = average_temperature(temp_maximum,temp_minimum,days)#Llamo la funcion para que me retorne la media
    print(f"La media del día {i+1}° es : {medium}")
"""

