import random
import ejercicios_de_funciones
'''Ejercicio en clase – Funciones
Crea un juego interactivo del ahorcado en Python. El juego debe seleccionar una palabra al
azar de una lista de palabras predefinidas y permitir que el jugador adivine la palabra letra por
letra. El jugador tiene un número limitado de intentos antes de perder el juego.
Requisitos:
 Define una lista de palabras que el programa pueda elegir al azar para que el jugador
adivine. Puedes usar palabras relacionadas con la programación, tecnología o
cualquier tema que te guste.
 El programa debe seleccionar una palabra al azar de la lista para cada partida.
 El juego debe mostrar el estado actual de la palabra oculta con guiones bajos (_) que
representan las letras no adivinadas y las letras adivinadas deben mostrarse en su
lugar correspondiente.
 El jugador debe poder ingresar una letra adivinada en cada turno.
 El programa debe verificar si la letra adivinada está en la palabra secreta y actualizar el
tablero en consecuencia.
 El jugador tiene un número limitado de intentos (por ejemplo, 6) antes de perder el
juego.
 Muestra mensajes informativos al jugador, como "Adivinaste una letra correctamente"
o "Letra incorrecta, te quedan X intentos".
 El juego debe terminar cuando el jugador adivina todas las letras o se quedan sin
intentos.
 Proporciona un mensaje de victoria si el jugador adivina la palabra y un mensaje de
derrota si se quedan sin intentos.
Consideraciones adicionales:
 Puedes utilizar funciones para organizar tu código de manera efectiva.
 Agrega comentarios para explicar el funcionamiento de tu código.'''

list_word = ["ARBOL", "CASAMIENTO", "PYTHON", "RUEDA", "MESA", "CAZAR", "CASAR", "HELADERIA", "HELADERO", "HELADERA", "CARACAS", "VENEZUELA"]
attempts = 10
random_word = random.choice(list_word)
phrase = ""
message = ""

while True:
    characters = ejercicios_de_funciones.choiced_word(random_word,phrase)
    print(f"la palabra es: {characters}")
    if characters != random_word and attempts == 0:
        message = "No te quedan mas intento, Perdiste JAJAJAJA"
        break
    elif characters == random_word and attempts > 0:
        message = "Felicidades has adivinado la palabra!!"
        break
    letter = input('Ingrese una "letra" para adivinar la palabra: ').upper()
    if letter not in random_word and attempts > 0:
        attempts -= 1
    if len(letter) > 1:
        print("Opcion no valida.")
        continue
    print(f"Te quedan {attempts} intentos")
    phrase += letter

print(message)


