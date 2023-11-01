#TP-7
#1-Escribe un programa que tome una lista de números como entrada y la ordene en orden ascendente 
# utilizando el método de ordenamiento de burbuja.
"""
def bubble_sort(arr):
    leng = len(arr) - 1

    for i in range (0, leng): #bucle para recorrer la lista
        for j in range(0, leng):#bucle para comparar 
            if arr[j] > arr[j+1]:
                temp = arr[j] #uso esta variable temporal para guardar si es mayor 
                arr[j] = arr[j+1] # reemplazo
                arr[j+1] = temp #y reemplazo para que quede la menor a la izquierda

    return arr


list = []
cont = 0
print ("Ingresaremos 6 números para ordenarlos en orden ascendente...")
while cont != 6:
    element = int(input(f"Ingrese {cont+1}° número: "))
    list.append(element)
    cont= cont +1
print(f"La lista antes de ordenar: \n {list}")
bubble_sort(list)
print(f"La lista ordenada: \n {bubble_sort(list)}")
"""
#2-Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en 
# orden ascendente utilizando el método de ordenamiento de selección.
"""
def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

def main():
    palabras = input("Ingresa una lista de palabras separadas por espacios: ")
    lista_palabras = palabras.split()
    ordenamiento_seleccion(lista_palabras)
    print("Palabras ordenadas alfabéticamente:")
    for palabra in lista_palabras:
        print(palabra)

if __name__ == "__main__":
    main()
"""
#Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden ascendente
#  según su longitud. Puedes utilizar el método de ordenamiento de inserción.
"""
def insertion_sort_strings_by_length(strings):
    for i in range(1, len(strings)):
        current_string = strings[i]
        j = i - 1
        while j >= 0 and len(current_string) < len(strings[j]):
            strings[j + 1] = strings[j]
            j -= 1
        strings[j + 1] = current_string

if __name__ == "__main__":
    strings = ["manzana", "pera", "banana", "uva", "kiwi"]
    
    print("Lista original de cadenas:")
    print(strings)
    
    insertion_sort_strings_by_length(strings)
    
    print("\nLista de cadenas ordenada por longitud ascendente:")
    print(strings)
"""
#6-Escribe un programa que tome una lista de números enteros y ordene la lista utilizando el algoritmo 
# de ordenamiento por conteo.
"""
def counting_sort(arr):
    if not arr:
        return []

    # valor máximo y mínimo en la lista
    max_value = max(arr)
    min_value = min(arr)

    # lista auxiliar para contar las ocurrencias de cada número
    count = [0] * (max_value - min_value + 1)

    # Contar las ocurrencias de cada número en la lista
    for num in arr:
        count[num - min_value] += 1

    # reconstruyo la lista ordenada
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i + min_value] * count[i])

    return sorted_arr

if __name__ == "__main__":
    
    unsorted_list = [4, 2, 2, 8, 3, 3, 1]

    print("Lista desordenada:")
    print(unsorted_list)

    sorted_list = counting_sort(unsorted_list)

    print("\nLista ordenada:")
    print(sorted_list)
"""
