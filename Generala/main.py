import  generala
import jugada

#Variables
orden_dados = []

### Comienzo de partida
generala.clear()

#Definimos la cantidad de jugadores
cant_de_jugadores=generala.ingresarJugadores()

#Se crea una lista de objetos y se los inicializa
lista_de_jugadores = generala.inicializarJugadores(cant_de_jugadores)

#Limpiamos la pantalla para el comienzo del juego
generala.clear()
input("Todos los Jugadores arrojaran un dado.")

#Se tiran el dado para cada jugador
generala.tirarDadosComienzo(cant_de_jugadores,lista_de_jugadores,orden_dados)

#Ordenamos la lista y buscamos que el mayor no tenga coincidencias
generala.mostrarDadosOrdenados(orden_dados)

#Asignamos turnos
generala.asignarTurno(orden_dados,cant_de_jugadores,lista_de_jugadores)
generala.ordenarListaJugadores(lista_de_jugadores)

#Mostramos el turno que le tocó a cada jugador
generala.imprimirTurnos(lista_de_jugadores, cant_de_jugadores)
input()

#Comenzamos con la jugada
##Limpiamos la pantalla para la primer jugada
generala.clear()

##Comienza el bucle que nos dará los 11 turnos
