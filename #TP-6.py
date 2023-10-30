#1-Solicitar al usuario que ingrese números, estos deben guardarse en una lista. 
# Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.

list = []
while True:
    element = int(input("Ingrese numeros a guardar en una lista: "))
    if element == 0:
        break
    list.append(element)

print(f"La lista contiene los numeros: {list}")

#2-A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, 
# eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
number = int(input("Ingrese un número a encontrar en la lista: \n -->"))

if number in list:
    list.remove(number)
    print (list)
else:
    print(f"El numero {number} no se encuentra en la lista!")

#3-Imprimir la sumatoria de todos los números de la lista.
sum = 0
for i in list:
    sum += i
print(f"La suma de los elementos de la lista es: {sum}")

#4-Solicitar al usuario otro número y crear una lista con los elementos de la lista original,
# que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
new_list = []
new_number = int(input("Ingrese un número:"))
for i in list:
    if i < new_number:
        new_list.append(i)
print(new_list)

        