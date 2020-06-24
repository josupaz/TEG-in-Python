import random
from os import system, name

class Jugador():

    def __init__(self, nombre, tabla_puntaje, listaDeDados, turno):
        self.nombre = nombre
        self.tabla_puntaje = tabla_puntaje
        self.listaDeDados = listaDeDados
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

def tirarDadosNuevamente(listaDeDados, listaPosicionesAModificar):
    if (len(listaPosicionesAModificar) > 0):
        for i in range(len(listaPosicionesAModificar)):
            azar = random.randint(1,6)
            listaDeDados[listaPosicionesAModificar[i]-1] = azar       

def ordenarDados(listaDeDados):
    listaDeDados.sort(reverse=True)

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

def imprimirJugadores(lista_de_jugadores):
    print ("Jugador\t\tPuntaje")
    for i in range(len(lista_de_jugadores)):
        print("{}\t\t{}".format(lista_de_jugadores[i].nombre,lista_de_jugadores[i].tabla_puntaje))

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


def imprimirTurnos(listaDeJugadores, cant_de_jugadores):
    for i in range(cant_de_jugadores):
        print("Jugador {} turno: {} \n ".format(listaDeJugadores[i].nombre,listaDeJugadores[i].turno ))


def conteoDados(listaDeDados):
    conteo_numeros = {1:0,2:0,3:0,4:0,5:0,6:0}
    #for para recorrer lista de dados
    for i in range(5):
        #for para recorrer numeros del 1 al 6
        for j in range(6):
            k = j + 1
            if listaDeDados[i] == k:
                aux = str(conteo_numeros.get(k))
                conteo_numeros[k] = int(aux) +1

    return conteo_numeros

def asignarTurno(orden_dados,cant_de_jugadores,lista_de_jugadores):
    maneja_turno = 1
    for i in range(len(orden_dados)):
        for j in range(cant_de_jugadores):
            if(lista_de_jugadores[j].listaDeDados[0] == orden_dados[i] and lista_de_jugadores[j].turno == 0):
            
                lista_de_jugadores[j].turno = maneja_turno
                maneja_turno += 1

def tirarDadosComienzo(cant_de_jugadores,lista_de_jugadores,orden_dados):
    for i in range(cant_de_jugadores):
        tirarDados(lista_de_jugadores[i].listaDeDados)
        dado = mostrarPrimerDado(lista_de_jugadores[i].listaDeDados)
        #Creamos lista con los valores de los dados para analizar el mayor
        orden_dados.append(dado)

def ordenarListaJugadores(lista_de_jugadores):
    lista_de_jugadores.sort(key=lambda x: x.turno)


def calcularPuntajeTotal(tabla_puntaje):
    for i in range(10):
        tabla_puntaje[0] = tabla_puntaje[0] + tabla_puntaje[i+1] 

def isDobleGenerala(conteo_numeros_dados, lista_posibles_jugadas):
    for i in range(6):
        if(conteo_numeros_dados[i+1] == 5 and lista_posibles_jugadas[10] > 0):
            lista_posibles_jugadas[11] = 120

def isGenerala(conteo_numeros_dados, lista_posibles_jugadas):
    for i in range(6):
        if(conteo_numeros_dados[i+1] == 5):
            lista_posibles_jugadas[10] = 60

def isPoker(conteo_numeros_dados, lista_posibles_jugadas):
    for i in range(6):
        if(conteo_numeros_dados[i+1] == 4):
            lista_posibles_jugadas[9] = 40

def isFull(conteo_numeros_dados, lista_posibles_jugadas):
    for i in range(6):
        if(conteo_numeros_dados[i+1] == 3):
            for j in range(6):
                if(conteo_numeros_dados[j+1] == 2):
                    lista_posibles_jugadas[8] = 30

def isEscalera(conteo_numeros_dados, lista_posibles_jugadas):
    if conteo_numeros_dados[1] == 1 and conteo_numeros_dados[2] == 1 and conteo_numeros_dados[3] == 1 and conteo_numeros_dados[4] == 1:
        lista_posibles_jugadas[7] = 20

def isSeis(conteo_numeros_dados, lista_posibles_jugadas):
    if(conteo_numeros_dados[6] > 0):
        lista_posibles_jugadas[6] = conteo_numeros_dados[6] * 6

def isCinco(conteo_numeros_dados, lista_posibles_jugadas):
    if(conteo_numeros_dados[5] > 0):
        lista_posibles_jugadas[5] = conteo_numeros_dados[5] * 5

def isCuatro(conteo_numeros_dados, lista_posibles_jugadas):
    if(conteo_numeros_dados[4] > 0):
        lista_posibles_jugadas[4] = conteo_numeros_dados[4] * 4

def isTres(conteo_numeros_dados, lista_posibles_jugadas):
    if(conteo_numeros_dados[3] > 0):
        lista_posibles_jugadas[3] = conteo_numeros_dados[3] * 3

def isDos(conteo_numeros_dados, lista_posibles_jugadas):
    if(conteo_numeros_dados[2] > 0):
        lista_posibles_jugadas[2] = conteo_numeros_dados[2] * 2

def isUno(conteo_numeros_dados, lista_posibles_jugadas):
    if(conteo_numeros_dados[1] > 0):
        lista_posibles_jugadas[1] = conteo_numeros_dados[1] * 1

def mostrarListaDePosiblesJugadas(lista_posibles_jugadas):
    print("Posibles jugadas \n")
    print("""
    Opcion-\t 1 \t 2 \t 3 \t 4 \t 5 \t 6   \t 7\t \t 8\t9 \t 10   \t   \t 11\
    """)
    print("""
    Jugada-\t Uno \t Dos \t Tres \t Cuatro   Cinco\t Seis \t Escalera\t Full \t Poker \t Generala\t D.Generala
    """)
    print("""Puntaje-\t {} \t {} \t {} \t {} \t {} \t {}   \t {}\t \t {}\t{} \t {}   \t   \t {}\
        """.format( lista_posibles_jugadas[1],
         lista_posibles_jugadas[2], lista_posibles_jugadas[3], lista_posibles_jugadas[4],
          lista_posibles_jugadas[5], lista_posibles_jugadas[6], lista_posibles_jugadas[7],
           lista_posibles_jugadas[8], lista_posibles_jugadas[9], lista_posibles_jugadas[10],
            lista_posibles_jugadas[11]))

def menuJugada():
    opcion = int(input("""Seleccione la opcion deseada:
    \t 1- Tirar dados nuevamente
    \t 2- Anotar puntaje
    \t 3- Tachar jugada
    """))

    if opcion == 1:
        dados_a_tirar = input("""Seleccione los dados a tirar:
            
        """)
        listaPosicionesAModificar = []
        for i in range(len(dados_a_tirar)):
            listaPosicionesAModificar.append(int(dados_a_tirar[i]))

    elif opcion == 2:
        dados_a_tirar = int(input("""Seleccione el puntaje a anotar:
            
        """))

    elif opcion == 3:
        dados_a_tirar = int(input("""Seleccione el puntaje a tachar:
            
        """))

    else:
        print("Ingrese una opcion valida")

    return listaPosicionesAModificar
