import games
import h
import os
import hadri


# Funcion encargada de pedir y configurar la dificultad del juego
def pedirNivel():
    level = -1
    while level < 1 or level > 3:
        level = int(raw_input("Elige dificutad: facil (1), medio(2), dificil(3): "))

    if level == 1:
        return None, 3
    elif level == 2:
        return h.hX, 4
    else:
        return hadri.heuristicaBuena, 4
# Fin funcion ---------------------------------------------------
# Funcion encargada de pedir y configurar el modo del juego
def pedirModo():
    mod = -1
    while mod < 1 or mod > 3:
        mod = int(raw_input("Elige modo: Maquina VS Humano (1) | Maquina VS Maquina (2):"))

    if mod == 1:
        return humano
    elif mod == 2:
        return maquina
# Fin funcion ---------------------------------------------------
# Jugador humano
def humano():
    col_str = raw_input("Movimiento: ")
    coor = int(str(col_str).strip())
    x = coor
    y = -1
    legal_moves = game.legal_moves(state)
    for lm in legal_moves:
        if lm[0] == x:
            y = lm[1]
    return x, y
# Fin funcion ---------------------------------------------------
# Jugador maquina
def maquina():
    print "Thinking..."
    return games.alphabeta_search(state, game, eval_fn=h.hO, d=5)
# Fin funcion ---------------------------------------------------
# Pedir primer Jugador
def pedirPlayer():
    return raw_input("Elige primer jugador X o O: ")

ejecutar = pedirModo()
nivel = pedirNivel()
player = pedirPlayer()

game = games.ConnectFour()
state = game.initial
game.initial.to_move = player

while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        move = ejecutar()
    else:
        print "Thinking..."
        move = games.alphabeta_search(state, game, eval_fn=nivel[0], d=nivel[1])

    state = game.make_move(move, state)
    player = state.to_move
    os.system('cls')
    # print "------------------------------------------"
    if game.terminal_test(state):
        print "----------------------------------------"
        if player == 'O':
            print "Jugador Ganador: X"
        else:
            print "Jugador Ganador: O"
        game.display(state)
        print "Final de la partida"
        break
