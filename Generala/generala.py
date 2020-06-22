import random
from os import system, name

class Jugador():

    def __init__(self, nombre, tabla_puntaje, dados, turno):
        self.nombre = nombre
        self.tabla_puntaje = tabla_puntaje
        self.dados = dados
        self.turno = turno

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

def tirarDados(lista):
    for i in range(5):
        azar = random.randint(1,6)
        lista[i] = azar

def mostrarDadosOrdenados(lista):
    lista.sort(reverse=True)

def mostrarPrimerDado(lista):
    return lista[0]

def ingresarJugadores():
    cant_jugadores = 1
    while(cant_jugadores < 2 or cant_jugadores > 6):
        try:
            cant_jugadores = int(input("Ingrese la cantidad de jugadores (cantidad maxima 6 jugadores):"))
        except:
            clear()
            print("Error, introduzca numero entre 2 y 6 \n")
    return cant_jugadores

def inicializarJugadores(cant_jugadores):
    jugadores = []
    for i in range(cant_jugadores):
        nombre = input("Ingrese el nombre del jugador {j}:".format(j=i+1))
        jugadores.append(Jugador(nombre,[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0],0))

    return jugadores        

def imprimirJugadores(lista):
    print ("Jugador\t\tPuntaje")
    for i in range(len(lista)):
        print("{}\t\t{}".format(lista[i].nombre,lista[i].tabla_puntaje))

def imprimirPuntajeCompleto(jugadores):
    print("Tabla de puntajes \n")
    print("""
    Jugadores \t 1 \t 2 \t 3 \t 4 \t 5 \t 6 \t Escalera\t Full \t Poker \t Generala\t D.Generala\tPuntaje Total
    """)

    for jugador in jugadores:
        print("""\
        {} \t {} \t {} \t {} \t {} \t {}  \t {}   \t {}   \t\t {}   \t {}   \t {} \t \t  {} \t \t {} \
        """.format(jugador.nombre, jugador.tabla_puntaje[0], jugador.tabla_puntaje[1],
         jugador.tabla_puntaje[2], jugador.tabla_puntaje[3], jugador.tabla_puntaje[4],
          jugador.tabla_puntaje[5], jugador.tabla_puntaje[6], jugador.tabla_puntaje[7],
           jugador.tabla_puntaje[8], jugador.tabla_puntaje[9], jugador.tabla_puntaje[10],
            jugador.tabla_puntaje[11]))


def imprimirJugadoresCompleto(listaDeJugadores, cant_de_jugadores):
    for i in range(cant_de_jugadores):
        print("Jugador: {} turno: {} \n ".format(listaDeJugadores[i].nombre,listaDeJugadores[i].turno ))


def conteoDados(listado_dados):
    conteo_numeros = {1:0,2:0,3:0,4:0,5:0,6:0}
    #for para recorrer lista de dados
    for i in range(5):
        #for para recorrer numeros del 1 al 6
        for j in range(6):
            k = j + 1
            if listado_dados[i] == k:
                aux = str(conteo_numeros.get(k))
                conteo_numeros[k] = int(aux) +1

    return conteo_numeros



def jugar(diccionario):
    pass
