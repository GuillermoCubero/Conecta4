from h import buscar

infinity = 1.0e400


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@memoize
def hX(state):
    return h(state, "X")


@memoize
def hO(state):
    return h(state, "O")


def h(state, player):
    listaJugador = []
    listaOponente = []
    valor = 0
    if state.utility != 0:
        if player == "X":
            return infinity * state.utility
        else:
            return -infinity * state.utility
    else:
        for pos in state.board:
            if state.board[pos] == player:
                listaJugador.append(pos)
                valor += buscar(listaJugador, pos)
            else:
                listaOponente.append(pos)
                valor -= buscar(listaOponente, pos)
    return valor


def buscar(lista, ind):
    return buscarAux(lista, ind, -1, 0) + buscarAux(lista, ind, -1, -1) + buscarAux(lista, ind, 0, -1) + buscarAux(
        lista, ind, 1, -1)


def buscarAux(lista, ind, dir1, dir2):
    valor = 1
    while (ind[0] + dir1, ind[1] + dir2) in lista:
        ind = (ind[0] + dir1, ind[1] + dir2)
        valor *= 2
    return valor
