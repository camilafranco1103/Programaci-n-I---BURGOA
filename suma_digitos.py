import ejercicios_de_funciones

'''Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos.
Al finalizar mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos.'''

add = 0
summary_digit = 0   

while True:
    number = int(input("ingresa un digito: "))
    if number == 0:
        break
    elif number < 0:
        print("El numero ingresado debe ser mayor a 0. Vuelva a intentarlo.")
        continue
    print(f"La suma de los digitos es: {ejercicios_de_funciones.sum_digit(number)}")
    add += number
    summary_digit += ejercicios_de_funciones.sum_digit(number)

print(f"La suma de los numeros ingresados es: {add}")
print(f"La sumatoria total de los digitos ingresados es: {summary_digit}")
