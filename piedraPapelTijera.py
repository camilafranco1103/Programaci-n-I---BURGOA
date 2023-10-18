import random


elements = ["piedra","papel","tijera"]
#Presentación
name=input("Hola, mi nombre es Wall-e (Una super IA jeje d(*-*)b), y tu como te llamas?: ")
decision=input(f"Encantado de conocerte {name.capitalize()}. Te gustaría jugar conmigo? Ingresa S para jugar o N para salir: ").upper()

#validacion de entrada al juego
while decision != "N" and decision != "S":
    print("Opcion no válida, vuelve a intentarlo así nos divertimos d(~.~)b")
    decision=input(f"Quiéres jugar {name.capitalize()}? Ingresa S para jugar o N para salir: ").upper()

print(f"Buenísimo, {name.capitalize()}. Jugaremos a Piedra, Papel o Tijera!!")

while decision:
    if decision == "S":
        # Utilizo la clase random para la elección de Wall-e
        random_element = random.choice(elements) 
        player = input("Elige Piedra, Papel o Tijera: ").lower()
        if player != "piedra" and player != "papel" and player != "tijera":
            print("Opcion no válida, vuelve a intentarlo así nos divertimos d(~.~)b")
            continue
        # Se muestra que ingresó cada jugador 
        print(f"{name.capitalize()} ingreso: {player.capitalize()}")
        print(f"Wall-e ingreso: {random_element.capitalize()}")
        # Validacion del ganador
        if (player == "piedra" and random_element == "tijera") or (player == "papel" and random_element == "piedra") or (player == "tijera" and random_element == "papel"):
            print(f"EL ganador es {name.capitalize()}")
        elif (player == "piedra" and random_element == "papel") or (player == "tijera" and random_element == "piedra") or (player == "papel" and random_element == "tijera"):
            print("El ganador es Wall-e.. Osea yo!!, buen intento!! d(^-^)b")
        elif (player == "piedra" and random_element == "piedra") or (player == "papel" and random_element == "papel") or (player == "tijera" and random_element == "tijera"):
            print("Tenemos un empate d(¬-¬')b buuuu")
        decision = input("Quieres volver a jugar? Ingresa S para 'Si' y N para 'No': ").upper()
        while decision != "N" and decision != "S":
            print("Opcion no válida, vuelve a intentarlo así nos divertimos d(~.~)b")
            decision = input("Quieres volver a jugar? Ingresa S para 'Si' y N para 'No': ").upper()
        if decision == "S":
            continue
        elif decision == "N":
            print("Que pena! d(>_<)b Nos vemos la próxima")
            break
    elif decision == "N":
        print("Que pena! d(>_<)b Nos vemos la próxima")
        break