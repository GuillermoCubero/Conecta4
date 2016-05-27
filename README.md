# Conecta4

Práctica de Fundamentos de los Sistemas Inteligentes: Búsqueda con Oponente.
Esta consiste en crear un juego (Conecta4) el cual debe permitir poder jugar maquina contra humano y maquina contra máquina, pudiendo así competir diferentes heurísticas, también debe permitir elegir una dificultad (fácil(1),medio(2),difícil(3)) y por ultimo elegir quien juega primero si X o O.
Para ello se han modificado los siguientes ficheros:

## games.py

1. Se ha modificado la forma en la que se muestra la partida, para facilitar la visualización, añadiendo colores (rojo para las X y amarillo para los O), también se ha cambiado la forma y se han añadido barras laterales.
	
## utils.py

1. Se ha modificado la función `argmin` para que muestre la puntuación obtenida para cada movimiento.
2. En la clase **Struct** se ha añadido una función hash para el correcto funcionamiento del decorador memoize.


## run.py

1. Se ha creado la función `pedirNivel()` la cual se encarga de pedir el nivel ("fácil (1), medio(2), difícil(3)") al comienzo de la partida.
2.	Se ha creado la función `pedirModo()` la cual se encarga de pedir el modo de juego ("Maquina VS Humano (1) | Maquina VS Maquina (2)") al comienzo de la partida.
3.	Se ha creado la función `pedirPlayer()` la cual se encarga de pedir que jugador empieza a jugar ("X o O") al comienzo de la partida.
4.	Una vez termina el juego indica quien ha ganado o si ha terminado en empate la partida.


## h.py

1. Se ha creado la función `memoize(f)` define el patrón memoize para reducir el tiempo de cálculo de la heurística, reutilizando los estados que han sido previamente calculados.
2. `hX(state)` y `hO(state)` llaman a `h(state,player)` mandándole el jugador correspondiente.
3. Se ha creado la función `h(state,player)` la cual crea dos listas, en una se almacenan las posiciones de las fichas del jugador y en el otro las del rival, en caso de que el **state.utility** sea distinto de 0 se devuelve este multiplicado por un número muy grande positivo en caso de ser el jugador **X** o negativo si es el jugador **O**, si no es así a partir del tablero empieza a recorrerlos mirando si cada ficha es una X o un O, dependiendo de eso y del jugador que sea las meterá en **listaJugador** o en **listaOponente**, luego llamara a `buscar(lista,ind)` mandando la lista correspondiente y la posición de la ficha actual, esta función devolverá *True* o *False* si es *True* suma o resta dependiendo de si es el oponente o el jugador.
4. La función `buscar(lista,ind)` devulve *True* si encuentra otra ficha a su alrededor o *False* si no.


## h2.py

1. Prácticamente igual solo que al encontrar una ficha contigua con otro continua para saber si son mas de 2 juntas.
2. `buscar(lista,pos)` se ha convertido en un metodo que llama 4 veces a `buscar(lista,pos,dir1,dir2)` que se encarga de comprobar si hay parejas, trios o mas, dandole un valor según lo que sea.
3. En la anterior version se elimiaba siempre al que se encontraba en esta version ya no se hace.
