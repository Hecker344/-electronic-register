def Pagella(aula):
    classe = 'terza_m'
    cognome = 'comastri'
    medie = []
    materie = ['matematica','italiano','storia','informatica','inglese']
    if classe in aula and cognome in aula[classe]: #Controlliamo che lo studente esista
        for x in range(5): #usiamo un for range di 5 dato che ci sono 5 materie
            somma=0 #azzeriamo somma per i cicli successivi
            voti = aula[classe][cognome][materie[x]] #Andiamo in ogni materia utilizzando x
            for y in voti:
                somma=somma+y #sommiamo e facciamo la media per ogni materia
            media=somma/len(voti)
            medie.append(media) #aggiungiamo il risultato media a una lista(medie)
    else:
        print("Cognome non trovato")#Nel caso in cui il cognome non esista comparirà un avviso
    colori=[]
    for z in medie:
        if z<=5.5: #utilizziamo una serie di if per attribuire a ogni voto un colore che verrà aggiunto a una lista(colori)
            colori.append('red')
        elif z>5.51 and z<=6:
            colori.append('yellow')
        else:
            colori.append('green')
    plt.bar(materie,medie,color=colori) #utillizziamo matplot per creare un grafico a barre
    plt.title('Pagella')
    plt.xlabel('Materie')
    plt.ylabel('Voti')
    plt.show()
