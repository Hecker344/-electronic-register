import datetime as dt
import dictcsv as dtc
import matplotlib.pyplot as plt
import csv

def nuovo_studente(classi,login,classe,mat):   # questa riga definisce la funzione nuovo_studenti
    cognome = str(input("Inserire il cognome dello studente da aggiungere:")) # inserimento del cognome dello studente
    password = str(input("Inserire la password dello studente da aggiungere:")) # inserimento della password dello studente
    classi[classe][cognome]={}
    classi[classe][cognome]['matematica'] = []
    classi[classe][cognome]['italiano'] = []
    classi[classe][cognome]['storia'] = []
    classi[classe][cognome]['inglese'] = []
    classi[classe][cognome]['informatica'] = [] # questa riga aggiunge il cognome al dizionario classi
    login[1]['studenti'][cognome] = [cognome,password]
    mat[1]['studenti'][cognome]=[0,classe]
    return classi,login,mat  # restituisce il dizionario con lo studente aggiunto


def nuovo_voto(aule,materia,classe): # definisco la funzione nuovo_voto 
    cognome = str(input("Inserire il cognome:")) # richiediamo all'utente di inserire il cognome
    voto = float(input("Inserisci il nuovo voto da aggiungere:")) # chiediam di inserire un nuovo voto
    voti = aule[classe][cognome][materia] # abbiamo ogni singolo voto dello studenti con la materia specificata
    voti.append(voto) # aggiunge il nuovo voto ai voti precedenti
    return aule # restituisce il dizionario con i voti aggiunti


def Andamento(classi,materia_prof,classe):
    cognome = input("Inserire il cognome dello studente del queale si vuole sapere i voti e la media:") #qua andiamo a prendere come input lo studente che si vuole analizzare
    if classi[classe][cognome][materia_prof]!=0: #qua controlliamo se lo studente nella materia ha almeno 1 voto
        print("I voti di",cognome,"in",materia_prof,"sono:",classi[classe][cognome][materia_prof]) #In questo print stampiamo tutti i voti dello studente in quella materia
        voti = classi[classe][cognome][materia_prof] #attribuiamo a una variabile i voti per comodità
        somma=0
        for x in voti:
            somma=somma+x #facciamo un ciclo per sommare fra di loro tutti i voti
        media=somma/len(voti) #facciamo la media
        print("La media di",cognome,"in",materia_prof,"è:",media) #mandiamo in out la media
    else:
        print(cognome,"in",materia_prof,"non ha voti") #nel caso in qui lo studente non abbia voti:


def Debito(classi,materia_prof):
    for x in classi:
        for y in classi[x]:
            voti=classi[x][y][materia_prof] #andiamo a fare tutti i possibili casi di studenti
            media = sum(voti)/len(voti) # facciamo la media di ogni studente
            if media < 6: # in caso in qui lo studente abbia la media inferiore al 6 lo stampiamo
                print(y,"ha la media insufficente")

def Pagella(aula,classe,cognome):
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

def media(nome, materia, classi): #definisco la funzione che esegue la media di una materia

    tot = sum(classi[nome][materia]) #sommatoria degli elementi della lista
    numero = len(classi[nome][materia]) #media = somma/numero di elementi

    return round(tot/numero, 1) #ritorno la media arrotondata ai decimi


#andiamo a definire un prototipo del dizionario delle classi




def media_dei_singoli(classi, subjects): #funzione che calcola la media generale di ogni studente

    diz={

        'terza_m':[] #dizionario che contiene le medie degli studenti divisi per classe
        ,
        'terza_h': []
    }

    primechiavi = classi.keys() #primechiavi contiene le chiavi 'terza_m' e 'terza_h'

    for classe in primechiavi:

        studenti = classi[classe].keys() #studenti = studenti della 3m o della 3h in base al valore di primechiavi

        for nome in studenti:

            voti=0 #numero di voti per studente
            tot = 0  # variabile che contiene la somma di tutti i voti di uno studente
            for mat in subjects:

                tot = tot + sum(classi[classe][nome][mat]) #sommatoria dei voti

                voti = voti + len(classi[classe][nome][mat]) #contatore dei voti

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
def oscar(classi,classe):
    a=0 #variabile contatore ausiliaria
    i=0 #contatore del for
    z=0 #contatore aux 2
    materie = ['matematica', 'italiano', 'storia', 'inglese', 'informatica']
    medie=[] #definisco le variabili che serviranno nel programma
    if classe=='terza_m': #se stiamo usando la 3m
        scelta = 'M'
    else:
        scelta='H' #se stiamo usando la 3h
    if scelta == 'M': #scelta la tabella della 3m

        nomi = classi['terza_m'].keys() #nomi = lista dei cognomi degli alunni in 3m

        if a==0: #se ci troviamo al primo ciclo

            print('Nome studente:      Media Matematica:    Media Italiano:      Media storia:        Media inglese:       Media informatica:')
            print('')

        for i in nomi:

            c=i
            while len(c)<14: #standardizzo la lunghezza del nome per evitare problemi di indentazione
                c = c + ' '
                print(c, end = '      ')


        for z in materie:

            if z!='informatica':
                print( media(i, z, classi['terza_m']), end='                  ' )

            else: #se la materia è informatica non smetto di scrivere sulla stessa riga
                print(media(i, z, classi['terza_m']))

    else: #scelta la tabella della 3h

        nomi = classi['terza_h'].keys()

        if a == 0:  # se ci troviamo al primo ciclo

            print('Nome studente:       Media Matematica:    Media Italiano:      Media storia:        Media inglese:       Media informatica:')
            print('')

        for i in nomi:

            c = i
            while len(c) < 14:  # standardizzo la lunghezza del nome per evitare problemi di indentazione
                c = c + ' '
            print(c, end='       ')

            for z in materie:

                if z != 'informatica':
                    print(media(i, z, classi['terza_h']), end='                  ' )

                else:
                    print(media(i, z, classi['terza_h']))

    materie = ['matematica', 'italiano', 'storia', 'inglese', 'informatica']

    #occorre ottenere la media generale di ambo le classi, e quella degli studenti singoli
    #serve una lista di medie della 3m, della 3h, una della generale totale in 3m, una della generale totale della 3h

    mediasingoli = media_dei_singoli(classi, materie)

    grafico_uno( media_delle_classi(classi, materie) )

    grafico_due(mediasingoli) #chiamo tutte le funzioni

    grafico_tre(mediasingoli)

def andamento_materia(classi,classe,nomut):   # definisco una funzione per l'andamento della materia
    cognome = nomut
    opzione = int(input("Quale materia vuoi visualizzare\n1. Matematica\n2. Storia\n3. Inglese\n4. Italiano\n5. Informatica\nInserisci un'opzione: "))  # si richiede all'utente di scegliere una materia  stampa le materie nella quale posso visualizzare l'andamento

    if opzione == 1:       # assegna a materia in base alla scelta del dell'utente

        mat = 'matematica'

    elif opzione == 2:

        mat = 'storia'

    elif opzione == 3:

        mat = 'inglese'


    elif opzione == 4:

        mat = 'italiano'

    elif opzione == 5:

        mat = 'informatica'

    voti = classi[classe][cognome][mat]   # ottengo i voti dello studente per la materia selezionata

    print(voti)  #stampo i voti 

    plt.plot(range(1, len(voti) + 1), voti, marker="o", linestyle='-', color='r')  # crea un grafico dove il primo argomento è l'asse delle x e il secondo è l'asse delle y

    plt.title(mat)  # titoli delle materie

    plt.xlabel('Verifiche')   # etichetta sull'asse delle x

    plt.ylabel('Voti')   # etichetta sull'asse della y

    plt.grid(True)   # attiva la griglia del grafico

    plt.show()  # mostra il grafico

def andamento5voti(studente):

    for materie in studente.keys():

        while len(studente[materie])>5:

            del studente[materie][5] #tramite i for ed i delete riduco a 5 o meno il numero di voti per ogni materia da inserire nel grafico

        z=len(studente[materie]) #questo è il range da usare per il grafico lineare, corrispondente al numero di voti per materia


        plt.plot(range(1, z+1), studente[materie], marker='o', linestyle='-', color='r')
        plt.title('Andamento degli ultimi 5 voti delle materie')
        plt.ylabel("Voto")
        plt.xlabel(materie) #ad ogni ciclo mostro il grafico relativo alla materia che il ciclo sta usando in quel momento
        plt.grid(True)
        plt.show()


def scrittura(classi):
    with open('classi.csv', 'w', newline='') as f:
        writer = csv.writer(f) 
        writer.writerow(['Classi', 'Studente', 'Materia', 'Voti'])
        for classe, studenti in classi.items():
            for studente, materie in studenti.items():
                for materia, voti in materie.items():       
                    # Controlla se ci sono voti duplicati
                    if len(voti) > len(set(voti)):
                        # Rimuovi i duplicati
                        voti = list(set(voti))       
                    writer.writerow([classe, studente, materia, ','.join(map(str, voti))])


def lettura(): 
    classi = {} 
    with open('classi.csv', 'r') as f:
        reader = csv.reader(f)
        headers = next(reader) 
        col_classe = headers.index('Classi') 
        col_studente = headers.index('Studente')
        col_materia = headers.index('Materia')
        col_voti = headers.index('Voti') 
        for row in reader:
            classe = row[col_classe]
            studente = row[col_studente]
            materia = row[col_materia]
            voti = []
            for x in row[col_voti].split(','):
                if x:
                    voti.append(float(x))

            #voti = [float(x) for x in row[col_voti].split(',')]
            classe_dict = classi.setdefault(classe, {})
            studente_dict = classe_dict.setdefault(studente, {})
            studente_dict[materia] = voti         
    return classi   

classi=lettura()

login=dtc.read("login")

scelt=int(input("Se sei un prof premi 0, se sei uno studente premi 1: ")) #scelta in input dall'utente se prof o studente
if scelt==0: #if condizionale per l'opzione
    nomut=input("Inserisci il nome utente: ") #input nome utente
    psw=input("Inserisci la password: ") #input password
    mat=dtc.read('prof')
    if mat[0]['prof'][nomut][1]=="terza_m":
        classe="terza_m"
        materia=mat[0]['prof'][nomut][0]
    else:
        classe="terza_h"
        materia=mat[0]['prof'][nomut][0]
    print(materia)
    if nomut==login[0]['prof'][nomut][0] and psw==login[0]['prof'][nomut][1]: #controllo nome utente e password prof
        print("Login eseguito!")
        j=0
        while j!=7: #ciclo che ripete fino a quando l'utente non inserisce l'opzione 7
            print("Ecco la lista di opzioni che hai a disposizione\n1. Nuovo studente\n2. Nuovo voto\n3. Andamento studente\n4. Debito\n5. Scrutinio\n6. Confronto\n7. Esci")
            j=int(input("Inserisci un'opzione: ")) #input scelta
            if j==1: #se l'utente inserisce l'opzione 1
                classi,login,mat=nuovo_studente(classi,login,classe,mat) #chiamo la funzione nuovo_studente #FUNZIONA#
            elif j==2: #se l'utente inserisce l'opzione 2
                classi=nuovo_voto(classi,materia,classe) #chiamo la funzione nuovo_voto #FUNZIONA#
            elif j==3: #se l'utente inserisce l'opzione 3
                Andamento(classi,materia,classe) #chiamo la funzione Andamento #FUNZIONA#
            elif j==4: #se l'utente inserisce l'opzione 4
                Debito(classi,materia) #chiamo la funzione Debito #FUNZIONA#
            elif j==5: #se l'utente inserisce l'opzione 5
                cognome = input("Inserire il cognome dello studente di cui si vuole vedere la pagella:") #qui andiamo a prendere come input lo studente che si vuole analizzare
                Pagella(classi,classe,cognome) #chiamo la funzione Pagella #FUNZIONA#
            elif j==6: #se l'utente inserisce l'opzione 6
                oscar(classi,classe) #FUNZIONA#
            elif j==7: #se l'utente inserisce l'opzione 7
                j==7 #fine ciclo
                print("Uscendo...")
                scrittura(classi) #chiamo la funzione scrittura
                esc="login"
                dtc.write(login,esc) #ripristino il login
                dtc.write(mat,'prof')
    else:
        print("Login non eseguito, password o nome utente non corretto!")

elif scelt==1:
    nomut=input("Inserisci il nome utente: ")
    psw=input("Inserisci la password: ")
    mat=dtc.read('prof')
    classe=mat[1]['studenti'][nomut][1]
    if nomut==login[1]['studenti'][nomut][0] and psw==login[1]['studenti'][nomut][1]: #controllo nome utente e password studente
        print("Login eseguito!")
        j=0
        while j!=4: #ciclo che ripete fino a quando l'utente non inserisce l'opzione 7
            print("Ecco la lista di opzioni che hai a disposizione\n1. Vedi l'andamento\n2. Visualizzazione pagella\n3. Andamento ultimi 5 voti\n4. Esci")
            j=int(input("Inserisci un'opzione: ")) #input scelta
            if j==1: #se l'utente inserisce l'opzione 1
                andamento_materia(classi,classe,nomut) #chiamo la funzione nuovo_studente #FUNZIONA#
            elif j==2: #se l'utente inserisce l'opzione 2
                Pagella(classi,classe,nomut)
            elif j==3: #se l'utente inserisce l'opzione 3
                andamento5voti(classi[classe][nomut])
            elif j==4: #se l'utente inserisce l'opzione 7
                j==4 #fine ciclo
                print("Uscendo...")
                scrittura(classi) #chiamo la funzione scrittura
                esc="login"
                login=dtc.write(login,esc) #ripristino il login 
    else:
        print("Login non eseguito, password o nome utente non corretto!")
else:
    print("opzione non esistente")
