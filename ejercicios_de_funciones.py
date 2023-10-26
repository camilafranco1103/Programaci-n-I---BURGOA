'''Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos.'''
#Sumar digitos de un numero ingresado.
def sum_digit(number):
    summary=0
    while number>10:
        summary += number%10
        number//=10
    summary += number
    return summary

'''El juego debe mostrar el estado actual de la palabra oculta con guiones bajos (_) que
representan las letras no adivinadas y las letras adivinadas deben mostrarse en su
lugar correspondiente.'''

# encuentra la palabra oculta
def choiced_word(word,phrase):
    characters = ""
    for i in word:
        if i in phrase:
            characters += i
        else:
            characters += "_"
    return characters