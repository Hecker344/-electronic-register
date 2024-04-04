import matplotlib.pyplot as plt #importo matplotlib

def media_dei_singoli(dizionarioclassi, subjects): #funzione che calcola la media generale di ogni studente

    tot=0 #variabile che contiene la somma di tutti i voti di uno studente
    diz={

        'terza_m':[] #dizionario che contiene le medie degli studenti divisi per classe
        ,
        'terza_h': []
    }

    primechiavi = dizionarioclassi.keys() #primechiavi contiene le chiavi 'terza_m' e 'terza_h'

    for classe in primechiavi:

        studenti = dizionarioclassi[classe].keys() #studenti = studenti della 3m o della 3h in base al valore di primechiavi

        for nome in studenti:

            voti=0 #numero di voti per studente

            for mat in subjects:

                tot = tot + sum(dizionarioclassi[classe][nome][mat]) #sommatoria dei voti

                voti = voti + len(dizionarioclassi[classe][nome][mat]) #contatore dei voti

            tot = round(tot/voti, 1) #la sommatoria diventa la media e viene approssimata ai decimi

            if classe == 'terza_m':

                diz['terza_m'].append(tot) #in base alla chiave in uso inserisco la media nella class relativa

            elif classe == 'terza_h':

                diz['terza_h'].append(tot)

    return diz #ritorno il dizionario delle medie

def media_delle_classi(dizionarioclassi, subjects): #funzione che definisce la media totale di una classe

    lista = []

    primechiavi = dizionarioclassi.keys()

    for classe in primechiavi:

        studenti = dizionarioclassi[classe].keys()

        tot = 0 #in questo caso dobbiamo spostare alcuni comandi di qualche for indietro per non azzerare le variabili troppo presto
        voti = 0

        for nome in studenti:

            for mat in subjects:

                tot = tot + sum(dizionarioclassi[classe][nome][mat]) #la somma continua e non viene mai azzerata, vale anche per il contatore di voti

                voti = voti + len(dizionarioclassi[classe][nome][mat])

        tot = round(tot / voti, 1) #una volta che gli studenti di una classe sono stati tutti contati viene eseguita la media e aggiunta alla lista delle medie totali per classe

        lista.append(tot)

    return lista #ritorno la lista totale

def grafico_uno(mediatot): #funzione del primo grafico che richiede solo la media totale

    titoli = ['Media Generale 3^M','Media Generale 3^H']

    colori = ['green', 'blue']

    plt.bar(titoli, mediatot, color=colori) #definisco le caratteristiche ed i parametri parametri del grafico a barre

    plt.title('Confronto della media di 2 classi')

    plt.xlabel('Classi')
    plt.ylabel('Media')

    plt.show()

def grafico_due(mediasing): #grafico 2 che richiede la media dei singolari studenti

    insufficienti_terza_m=0 #2 variabili che conterranno il rispettivo numero di alunni con una media generale inferiore al 6
    insufficienti_terza_h=0

    for k in mediasing.keys(): #k assume il valore della chiave 3m o della chiave 3h che permette di accedere alle relative medie

        for counter in mediasing[k]:

            if counter<6 and k=='terza_m': #se la media è inferiore al 6 e stiamo usando la 3m andiamo ad incrementare il counter degli studenti insufficienti in 3m di 1

                insufficienti_terza_m+=1

            elif counter<6 and k=='terza_h': #se la media è inferiore al 6 e stiamo usando la 3h andiamo ad incrementare il counter degli studenti insufficienti in 3h di 1

                insufficienti_terza_h+=1


    insufficientitot=[]

    insufficientitot.append(insufficienti_terza_m) #andiamo ad aggiungere i 2 contatori degli insufficienti in una sola lista

    insufficientitot.append(insufficienti_terza_h)

    titoli = ['Alunni insufficienti in 3^M','Alunni insufficienti in 3^H']

    plt.bar(titoli, insufficientitot, color=['red','red'])


    plt.title('Confronto del numero di insufficienti delle due 2 classi') #definisco il grafico a barre degli insufficienti e lo mostro

    plt.xlabel('Classi')
    plt.ylabel('Numero di insufficienti')

    plt.show()

def grafico_tre(mediasing): #creo la funzione del terzo grafico che chiede la media dei singoli studenti

    intervalli = [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ] #creo la lista degli intervalli, che contiene per ogni intervallo un contatore degli studenti che rientrano in quell'intervallo

    for k in mediasing.keys():

        for counter in mediasing[k]: #vado a ciclare le medie degli studenti

            if counter<2:

                intervalli[0]+=1

            elif counter >= 2 and counter < 3:

                intervalli[1]+=1

            elif counter >= 3 and counter < 4: #è come uno switch case, se la media rientra in un intervallo viene incrementato il relativo contatore, sennò si passa all'intervallo successivo

                intervalli[2]+=1

            elif counter >= 4 and counter < 5: #4 intervalli di voti rossi

                intervalli[3]+=1

            elif counter >= 5 and counter < 6: #1 intervallo di voti arancioni

                intervalli[4]+=1

            elif counter >= 6 and counter < 7: #4 intervalli di voti verdi

                intervalli[5]+=1

            elif counter >= 7 and counter < 8:

                intervalli[6]+=1

            elif counter >= 8 and counter < 9:

                intervalli[7]+=1

            elif counter >= 9 and counter < 10:

                intervalli[8]+=1

    indexdaeliminare=[] #creo la lista degli intervalli da eliminare poiché vuoti


    for var in range(len(intervalli)):

        if intervalli[var]==0:
             #mi salvo tutti gli indici della lista degli intervalli di voti che sono senza studenti così li elimino
            indexdaeliminare.append(var) #salvo l'indice dell'intervallo che vale 0


    colori = ['red','red','red','red','yellow','green','green','green','green']

    nomiintervalli = ['Inferiori al 2','Compresi tra il 2 ed il 3','Compresi tra il 3 ed il 4','Compresi tra il 4 ed il 5','Compresi tra il 5 ed il 6','Compresi tra il 6 ed il 7','Compresi tra il 7 e 8','Compresi tra 8 e 9','Compresi tra il 9 ed il 10']

    z=0
    #variabile ausiliaria z
    for k in indexdaeliminare:
        del intervalli[k-z]
        del colori[k-z] #elimino gli elementi che si riferiscono all'intervallo da eliminare tramite lo stesso indice - Z, che è una variabile che tiene conto anche di quanti indici sono stati rimossi e quindi aiuterà a rimuovere indici sempre esistenti e non esistenti, ad esemepio se rimuovo l'indice 1, la lista si accorcia di 1 e quindi l'indice che prima era 8 diventa 7 e diventa necessario ridurre l'indice da rimuovere di 1
        del nomiintervalli[k-z]
        z+=1


    plt.pie(intervalli, labels=nomiintervalli, autopct='%1.1f%%', colors=colori)
    plt.axis('equal') #creo il grafico a torta
    plt.title('Numero di studenti totali presenti in determinati intervalli di voti')
    plt.show()


classi = {

        'terza_m': {
                                'ansaloni': { #1 stutente di 3m
                                        'matematica': [4,5.5], 'italiano': [6.7,7.25], 'storia': [5, 6], 'inglese': [8,8], 'informatica':[3,4.5]
                                    }
                                ,

                                'barchetti': { #2 stutente di 3m
                                        'matematica': [7,7.75], 'italiano': [8,7.25], 'storia': [7, 7.5], 'inglese': [7,6.5], 'informatica':[7.75,7.25]
                                    }

                                ,

                                'bonfatti': { #3 stutente di 3m
                                        'matematica': [7,8], 'italiano': [6.5,7.25], 'storia': [10, 6.75], 'inglese': [8.75,9.5], 'informatica':[10,7]
                                    }
                                ,

                                'brugnano': { #4 stutente di 3m
                                        'matematica': [4,5.5], 'italiano': [6.7,7.3], 'storia': [5, 6], 'inglese': [8,8], 'informatica':[3,4.5]
                                    }
                                ,

                                'bruni': { #5 stutente di 3m
                                        'matematica': [4,5.5], 'italiano': [6.7,7.3], 'storia': [5, 6], 'inglese': [8,8], 'informatica':[3,4.5]
                                    }
                                ,

                                'capponi': { #6 stutente di 3m
                                        'matematica': [8,7], 'italiano': [6.5,7.25], 'storia': [8, 8.5], 'inglese': [7.75,8.25], 'informatica':[10,8]
                                    }

                                ,

                                'cenolli': { #7 stutente di 3m
                                        'matematica': [3,6], 'italiano': [5.75,6.25], 'storia': [6.25, 7], 'inglese': [4,6], 'informatica':[6,5.5]
                                    }
                                ,

                                'crispino': { #8 stutente di 3m
                                        'matematica': [3,7.5], 'italiano': [5.25,6], 'storia': [5.75, 6], 'inglese': [6,6], 'informatica':[5,4.5]
                                    }
                                ,

                                'comastri': { #9 stutente di 3m
                                        'matematica': [5,6], 'italiano': [6.75,6], 'storia': [5.75, 6], 'inglese': [7,6.25], 'informatica':[5,6.75]
                                    }
                                ,

                                'demkollari': { #10 stutente di 3m
                                        'matematica': [3,5.5], 'italiano': [6,6.5], 'storia': [7, 6.25], 'inglese': [8,7.75], 'informatica':[7.25,10]
                                    }
                    }
        ,

        'terza_h': {

                                'scorcioni': { #1 stutente di 3h
                                        'matematica': [3,3.75], 'italiano': [6.25,6.75], 'storia': [6, 7], 'inglese': [6,6.5], 'informatica':[10,6.75]
                                    }
                                ,

                                'nappa': { #2 stutente di 3h
                                        'matematica': [8,6.5], 'italiano': [8,7.5], 'storia': [8, 9], 'inglese': [7,7], 'informatica':[7.5,8]
                                    }

                                ,

                                'serafini': { #3 stutente di 3h
                                        'matematica': [7,7.25], 'italiano': [8,8.25], 'storia': [10, 7.25], 'inglese': [8.25,7.75], 'informatica':[9,7]
                                    }
                                ,

                                'tagliavini': { #4 stutente di 3h
                                        'matematica': [5.5,6.75], 'italiano': [6.75,7.5], 'storia': [6.75, 7.5], 'inglese': [7.25,7], 'informatica':[4,6]
                                    }
                                ,

                                'lombardi': { #5 stutente di 3h
                                        'matematica': [9,7.5], 'italiano': [9,8.5], 'storia': [8, 8.75], 'inglese': [9,8], 'informatica':[8,8]
                                    }
                                ,

                                'merli': { #6 stutente di 3h
                                        'matematica': [7.5,8], 'italiano': [7,7.25], 'storia': [6.5, 7.25], 'inglese': [4,5], 'informatica':[7,8]
                                    }

                                ,

                                'napoletano': { #7 stutente di 3h
                                        'matematica': [4,5.5], 'italiano': [6,5.75], 'storia': [6, 6.25], 'inglese': [6,6], 'informatica':[5,6]
                                    }
                                ,

                                'cordero': { #8 stutente di 3h
                                        'matematica': [5,6.5], 'italiano': [6.7,7.3], 'storia': [5, 6], 'inglese': [5,5.75], 'informatica':[6,6.5]
                                    }
                                ,

                                'poppi': { #9 stutente di 3h
                                        'matematica': [3,4.5], 'italiano': [5.25,6], 'storia': [5.5, 6], 'inglese': [4,5.75], 'informatica':[4,5.5]
                                    }
                                ,

                                'gazzotti': { #10 stutente di 3h
                                        'matematica': [7,6.5], 'italiano': [7,6.25], 'storia': [8, 7], 'inglese': [6.5,7.5], 'informatica':[7,8]
                                    }
        }
}

materie = ['matematica', 'italiano', 'storia', 'inglese', 'informatica']

#occorre ottenere la media generale di ambo le classi, e quella degli studenti singoli
#serve una lista di medie della 3m, della 3h, una della generale totale in 3m, una della generale totale della 3h

mediasingoli = media_dei_singoli(classi, materie)

grafico_uno( media_delle_classi(classi, materie) )

grafico_due(mediasingoli) #chiamo tutte le funzioni

grafico_tre(mediasingoli)
#serve una lista di medie della 3m, della 3h, una della generale totale in 3m, una della generale totale della 3h

mediasingoli = media_dei_singoli(classi, materie)

grafico_uno( media_delle_classi(classi, materie) )

grafico_due(mediasingoli)

grafico_tre(mediasingoli)
