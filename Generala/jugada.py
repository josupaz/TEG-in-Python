import generala

def jugada(cant_de_jugadores,lista_de_jugadores):
    conteo_numeros_dados = {}
    #Recorre los 11 turnos del juego
    for i in range(11):
        #recorre la cantidad de jugadores
        for j in range(len(cant_de_jugadores)):
            #Recorre la cantidad de tiros
            for k in range(3):
                generala.tirarDados(lista_de_jugadores[j].listaDeDados)
                generala.ordenarDados(lista_de_jugadores[j].listaDeDados)
                conteo_numeros_dados = generala.conteoDados(lista_de_jugadores[j].listaDeDados)
                

            