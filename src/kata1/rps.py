from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    comp = len(player) - len(ai)

    if comp == 0:
        respuesta = 'Empate!'
    elif comp == -1 or comp == 2:
        respuesta = 'Ganaste!'
    else:
        respuesta = 'Perdiste!'

    return respuesta

# Entry Point
def Game():
    player = options[randint(0, 2)]
    ai = options[randint(0, 2)]

    winner = quienGana(player, ai)
    print(winner)

Game()