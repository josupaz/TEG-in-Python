import  generala

#Variables
orden_dados = []
maneja_turno = 1

### Comienzo de partida
generala.clear()
cant_de_jugadores=generala.ingresarJugadores()
lista_de_jugadores = generala.inicializarJugadores(cant_de_jugadores)


generala.clear()
input("Todos los Jugadores arrojaran un dado.")


for i in range(cant_de_jugadores):
    generala.tirarDados(lista_de_jugadores[i].dados)
    dado = generala.mostrarPrimerDado(lista_de_jugadores[i].dados)
    #Creamos lista con los valores de los dados para analizar el mayor
    orden_dados.append(dado)

#Ordenamos la lista y buscamos que el mayor no tenga coincidencias
generala.mostrarDadosOrdenados(orden_dados)

print(orden_dados)

for i in range(len(orden_dados)):
    for j in range(cant_de_jugadores):
        if(lista_de_jugadores[j].dados[0] == orden_dados[i] and lista_de_jugadores[j].turno == 0):
           
            lista_de_jugadores[j].turno = maneja_turno
            maneja_turno += 1


for i in range(cant_de_jugadores):
     print("{} es {}".format(lista_de_jugadores[i].dados[0],lista_de_jugadores[i].nombre))

generala.imprimirJugadoresCompleto(lista_de_jugadores, cant_de_jugadores)

print(orden_dados)

#for i in range(cant_de_jugadores):
print(lista_de_jugadores[0].dados)
conteo_numeros = generala.conteoDados(lista_de_jugadores[0].dados)
print(lista_de_jugadores[0].nombre)
print(conteo_numeros)
