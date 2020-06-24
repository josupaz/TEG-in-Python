import generala

def jugada(cant_de_jugadores,lista_de_jugadores):
    conteo_dados = {}
    listaPosicionesAModificar = []
    
    #Recorre los 11 turnos del juego
    for i in range(11):

        #Recorre la cantidad de jugadores
        for j in range(cant_de_jugadores):


            #Recorre la cantidad de tiros (3) de dados disponibles por jugador
            for k in range(3):
                lista_posibles_jugadas = [0,0,0,0,0,0,0,0,0,0,0,0]

                if k==0:
                    generala.tirarDados(lista_de_jugadores[j].listaDeDados)

                if k>0:
                    generala.tirarDadosNuevamente(lista_de_jugadores[j].listaDeDados, listaPosicionesAModificar)
                
                generala.ordenarDados(lista_de_jugadores[j].listaDeDados)
                
                conteo_dados = generala.conteoDados(lista_de_jugadores[j].listaDeDados)
                #Evalua las posibles opciones de juego y las guarda en lista_posibles_jugadas[]
                if lista_de_jugadores[j].tabla_puntaje[11] == 0:
                    generala.isDobleGenerala(conteo_dados,lista_posibles_jugadas)
                if lista_de_jugadores[j].tabla_puntaje[10] == 0:
                    generala.isGenerala(conteo_dados, lista_posibles_jugadas)
                if lista_de_jugadores[j].tabla_puntaje[9] == 0:
                    generala.isPoker(conteo_dados, lista_posibles_jugadas)
                if lista_de_jugadores[j].tabla_puntaje[8] == 0:
                    generala.isFull(conteo_dados, lista_posibles_jugadas)
                if lista_de_jugadores[j].tabla_puntaje[7] == 0:
                    generala.isEscalera(conteo_dados, lista_posibles_jugadas)
                if lista_de_jugadores[j].tabla_puntaje[6] == 0:
                    generala.isSeis(conteo_dados, lista_posibles_jugadas)
                if lista_de_jugadores[j].tabla_puntaje[5] == 0:
                    generala.isCinco(conteo_dados, lista_posibles_jugadas)
                if lista_de_jugadores[j].tabla_puntaje[4] == 0:
                    generala.isCuatro(conteo_dados, lista_posibles_jugadas)
                if lista_de_jugadores[j].tabla_puntaje[3] == 0:
                    generala.isTres(conteo_dados, lista_posibles_jugadas)
                if lista_de_jugadores[j].tabla_puntaje[2] == 0:
                    generala.isDos(conteo_dados, lista_posibles_jugadas)
                if lista_de_jugadores[j].tabla_puntaje[1] == 0:
                    generala.isUno(conteo_dados, lista_posibles_jugadas)
                
                #Analiza si la jugada es servida
                if k == 0:
                    if lista_posibles_jugadas[10] != 0:
                        #Devuelve 1 para finalizar el juego por generala servida
                        return 1
                    if lista_posibles_jugadas[9] != 0:
                        lista_posibles_jugadas[9] += 5
                    if lista_posibles_jugadas[8] != 0:
                        lista_posibles_jugadas[8] += 5
                    if lista_posibles_jugadas[7] != 0:
                        lista_posibles_jugadas[7] += 5

                print("Los dados fueron los siguientes: ")
                for l in range (5):
                    print("Dado {}: {} \t".format(l+1,lista_de_jugadores[j].listaDeDados[l]))
                print("\n")
                generala.mostrarListaDePosiblesJugadas(lista_posibles_jugadas)

                input()
                
                listaPosicionesAModificar = generala.menuJugada()

            
            