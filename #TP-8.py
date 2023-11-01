#TP-8
# 1. Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.
'''

def cant_digito(num):
    if num < 10:
        return 1
    else:
        return 1 + cant_digito(num//10)

while True:
    numero = int(input("Ingrese un numero positivo: "))
    if numero > 0:
        break
    else:
        print("Ingrese un numero valido")
        continue
    
resultado = cant_digito(numero)
print("La cantidad de digitos que tiene el numero ingresado es: ", resultado)
'''
"""
3.	Escribir una funcion recursiva que reciba como parámetros dos strings a y b, y devuelva una lista con las posiciones en donde se encuentra b dentro de a. '''

# el tercer parametro es por defecto y es la posicion
def is_inside(a,b,pos = 0):
    # condicion de salida si la longitud del primer parametro es menor al del segundo
    if len(a) < len(b):
        return []
    # condicion para encontrar el segundo parametro en el primero
    if a[:len(b)] == b:
        return [pos] + is_inside(a[1:],b,pos + 1)
    else:
        return is_inside(a[1:], b, pos + 1)

# imprime la lista con las posiciones
print(is_inside("hola, tienes tiempo de tirar titeres a la tina?", "ti"))
"""
# 7. Implemente un algoritmo, usando una función recursiva, que resuelva la siguiente sumatoria:
# K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p
# El programa debe pedir al usuario que ingrese un número n, y un número p,
# Luego debe calcular el valor de K(n, p) usando una función recursiva,
# Debe imprimir el resultado de K(n, p)

'''
def suma(n, p):
    if n == 1:
        return p
    else:
        return p * n + suma(n-1,p)
    
n = int(input("Ingrese un numero: "))
p = int(input("Ahora ingrese un numero para la suma: "))

resultado = suma(n, p)
print(f"El resultado de la suma es {resultado}")

'''
