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

def h(state,player):
    h = 0
    lista1 = []
    lista2 = []
    if state.utility != 0:
        if player == "X":
            return infinity*state.utility
        else:
            return -infinity*state.utility
    else:
        for pos in state.board:
            valor = 1
            if state.board[pos] == player:
                lista1.append(pos)
                if buscar(lista1, pos):
                    h += valor
            else:
                lista2.append(pos)
                if buscar(lista2, pos):
                    h -= valor
        return h


def buscar(list, ind):
    indInf = (ind[0] - 1, ind[1])
    indInfIzq = (ind[0] - 1, ind[1] - 1)
    indIzq = (ind[0], ind[1] - 1)
    indSupIzq = (ind[0] + 1, ind[1] - 1)
    if indInf in list:
        list.remove(indInf)
        return True
    elif indInfIzq in list:
        list.remove(indInfIzq)
        return True
    elif indIzq in list:
        list.remove(indIzq)
        return True
    elif indSupIzq in list:
        list.remove(indSupIzq)
        return True
    else:
        return False
