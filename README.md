# Conecta4

Práctica de Fundamentos de los Sistemas Inteligentes: Búsqueda con Oponente

Esta consiste en crear un juego (Conecta4) el cual debe permitir poder jugar maquina contra humano y maquina contra maquina, pudiendo asi competir diferentes heuristicas, tambien debe permitir elegir una dificultad (facil(1),medio(2),dificil(3)) y por ultimo elegir quien juega primero si X o O.

Para ello se han modificado los siguientes ficheros:

## games.py

1. Se ha moficiado la forma en la que se muesta la partida, para facilitar la visualización, añadiendo colores (rojo para las X y amarillo para los O), tambien se ha cambiado la forma y se han añadido barras laterales.
	
## utils.py

1. Se ha modificado la funcion `argmin` para que muestre la puntuacion obtenida para cada movimiento
2. En la clase **Struct** se ha añadido una funcion hash para el correcto funcionamiento del decorador memoize

## run.py

1. Se ha creado la funcion `pedirNivel()` la cual se encarga de pedir el nivel ("facil (1), medio(2), dificil(3)") al comienzo de la partida
2. Se ha creado la funcion `pedirModo()` la cual se encarga de pedir el modo de juego ("Maquina VS Humano (1) | Maquina VS Maquina (2)") al comienzo de la partida
3. Se ha creado la funcion `pedirPlayer()` la cual se encarga de pedir que jugador empieza a jugar ("X o O") al comienzo de la partida
5. Una vez termina el juego indica quien ha ganado o si ha termiando en empate la partida.

## h.py

1. Se ha creado la funcion `memoize(f)`define el patrón memoize para reducir el tiempo de calculo de la heurística, reutilizando los estados que han sido previamente calculados.
2. `hX(state)` y `hO(state)` llaman a `h(state,player)` mandandole el jugador correspondiente.
3. Se ha creado la funcion `h(state,player)` la cual crea dos listas, en una se almacenan las posiciones de las fichas del jugador y en el otro las del rival, en caso de que el **state.utility** sea distinto de 0 se devuelve este multiplicado por un numero muy grande positivo en caso de ser el jugador **X** o negativo si es el jugador **O**, si no es asi a partir del tablero empieza a recorrerlos mirando si cada ficha es una X o un O, dependiendo de eso y del jugador que sea las metera en **listaJugador** o en **listaOponente**, luego llamara a `buscar(lista,ind)` mandando la lista correspondiente y la posicion de la ficha actual, esta funcion devolvera *True* o *False* si es true suma o resta dependiendo de si es el oponente o el jugador.
4. La función `buscar(lista,ind)` devulve *True* si encuentra otra ficha a su alrededor o *False* si no
