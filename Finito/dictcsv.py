def read(namefile):
    import csv #importazione del modulo csv usato per la lettura grezza del csv
    login1=[{},{}] #inizializzazione della lista di dizionari login1 dove verranno salvati i dati tradotti in dizionario
    with open(f"{namefile}.csv") as csvfile: #apertura del csv 
        k=0 #variabile contatore che ci servirà nel if
        spamreader = csv.reader(csvfile) 
        for row in spamreader: #for che ci permette di scorrere le righe del csv
                if k==0: #se var contatore ==0 (ovvero riga 0)
                    n=row[0] #salva in n riga 0 colonna 0
                    t=row[1] #salva in t riga 0 colonna 1
                elif k==1: #se var contatore == 1 (ovvero riga 1)
                    s=row[0] #salva riga 0 colonna 0 in s
                    login1[0][n]={} #inizializzazione del dizionario situato dentro il dizionario in login1 con come indice n (riga 9)
                elif k==2: #se var contatore ==2 (ovvero riga 2)
                    s1=row[1] #salva riga 0 colonna 1 in s1
                    login1[1][t]={} #inizializzazione del dizionario situato dentro il dizionario in login1 con come indice t (riga 10)
                k=k+1 #incremento var contatore
    k1=0; m=""; m1="" #inizializzazione k1 (var per l'inizializzazione del dizionario), inizializzazione di m (variabile che definirà la chiave del utente [nome utente]), inizializzazione m1 (variabile contenuto dati utente)
    stopper=s.count("],")+1 #definizione di stopper; variabile che definirà il numero di cicli da fare basandosi sulla lettura delle occorrenze di ], + 1 ovvero il numero di chiusure di liste nel dizionario 'prof'.
    a,b,c=0,1,2 #inizializzazione variabili per trovare i successivi ","   ":"   "],"  (utilizzo 0 per ], dato che ce n'è solo uno e non bisogna incrementarlo, 1 per : dato che ce ne sono due e vanno incrementati, 2 in c dato che di virgole a noi utili ce ne sono una ogni 3 infatti poi dopo il primo ciclo while PRINCIPALE verrà incrementato di 2 in 2)
    while stopper!=0:# while definito dalla variabile stopper decrescente
        if stopper==s.count("],")+1: #questo if definisce se si è al primo ciclo o no controllando il valore di stopper
            len1=s.find(":") #definisco len1 ovvero l'indice della prima occorrenza di :
            len2=s.find(",") #definisco len2 ovvero l'indice della prima occorrenza di ;
            len3=s.find("],") #definisco len3 ovvero l'indice della prima occorrenza di ],
            iniz=0 #definisco inizio ovvero per ora 0
        else:
            vird=a;no=0;ido=0  #qui uso un costrutto formata con un while che permette di andare tramite i parametri a,b o c a trovare i ","   ":"   "]," successivi agli ultimi trovati
            while no!=vird:
                iniz=s.find("],",ido)
                ido=iniz+1
                no=no+1

            vird=b;no=0;ido=0  #ripeto il costrutto di riga 28
            while no!=vird:
                len1=s.find(":",ido)
                ido=len1+1
                no=no+1


            vird=c;no=0;ido=0  #ripeto il costrutto di riga 28
            while no!=vird:
                len2=s.find(",",ido)
                ido=len2+1
                no=no+1


            vird=a+1;no=0;ido=0  #ripeto il costrutto di riga 28
            if stopper!=1: #condizione if che permette a len 3 di variare a ]} nel caso stopper sia all'ultimo ciclo
                while no!=vird:
                    len3=s.find("],",ido)
                    ido=len3+1
                    no=no+1
            else:
                len3=s.find("']}")

        for l in range(iniz,(len1+1)): #for con range che parte da iniz e va a len1 + 1 (ovvero primo indice di : +1)
            if s[l]!="{" and s[l]!="'" and s[l]!=":" and s[l]!=" " and s[l]!="]": #if che non permette l'ingresso di tutti i dati che non siano lettere a noi utili
                if s[l]!="[" and s[l]!=",":
                    m=m+s[l] #salvataggio in m della chaive
        
        for l in range((len1),(len2)): #for con range che parte da len1 e va a len2 (ovvero primo indice di ,)
            if s[l]!="{" and s[l]!="'" and s[l]!=":" and s[l]!=" ": #stesso if di riga 58
                if s[l]!="[" and s[l]!=",":
                        m1=m1+s[l] #salvataggio in m1 del primo dato della lista
        if k1==0: #if con var contatore k1
            login1[0][n][m]=[] #generazione della lista con chiave m
        login1[0][n][m].append(m1) #aggiunta di m1 nella lista appena creata con indice m in login[0][n]<----- ovvero intestazione del csv
        m1="" #reset di m1
        for l in range((len2),(len3)): #for con range da len2 a len3 che permette di salvare il secondo dato della lista 
            if s[l]!="{" and s[l]!="'" and s[l]!=":" and s[l]!=" ": #stesso if di riga 58
                if s[l]!="[" and s[l]!=",":
                        m1=m1+s[l] #salvataggio in m1 del secondo dato della lista
        login1[0][n][m].append(m1) #aggiunta di m1 nella lista creata a riga 67 con indice m in login[0][n]<----- ovvero intestazione del csv
        m1="" #reset m1
        m="" #reset m
        #k1=k1+1
        k1=0 #reset k1
        stopper=stopper-1 #decremento stopper
        a=a+1;b=b+1 #incremento a e b (ovvero variabili per trovare gli indici)
        if b==2: #if nomimato in precedenza a riga 20 per poter incrementare in modo variato c (var contatore del while di len2)
            c=c+1
        else:
            c=c+2

    k1=0; m=""; m1=""  #RESTART DEL CODICE PRINCIPALE PER LA SECODA PARTE DEL CSV OVVERO COLONNA 2 (CON S1) [CODICE INVARIATO]
    stopper=s1.count("],")+1
    a,b,c=0,1,2
    while stopper!=0:
        if stopper==s1.count("],")+1:
            len1=s1.find(":")
            len2=s1.find(",")
            len3=s1.find("],")
            iniz=0
        else:
            vird=a;no=0;ido=0
            while no!=vird:
                iniz=s1.find("],",ido)
                ido=iniz+1
                no=no+1

            vird=b;no=0;ido=0
            while no!=vird:
                len1=s1.find(":",ido)
                ido=len1+1
                no=no+1


            vird=c;no=0;ido=0
            while no!=vird:
                len2=s1.find(",",ido)
                ido=len2+1
                no=no+1


            vird=a+1;no=0;ido=0
            if stopper!=1:
                while no!=vird:
                    len3=s1.find("],",ido)
                    ido=len3+1
                    no=no+1
            else:
                len3=s1.find("']}")
  

        for l in range(iniz,(len1+1)):
            if s1[l]!="{" and s1[l]!="'" and s1[l]!=":" and s1[l]!=" " and s1[l]!="]":
                if s1[l]!="[" and s1[l]!=",":
                    m=m+s1[l]
        
        for l in range((len1),(len2)):
            if s1[l]!="{" and s1[l]!="'" and s1[l]!=":" and s1[l]!=" ":
                if s1[l]!="[" and s1[l]!=",":
                        m1=m1+s1[l]
        if k1==0:
            login1[1][t][m]=[]
        login1[1][t][m].append(m1)
        m1=""
        for l in range((len2),(len3)):
            if s1[l]!="{" and s1[l]!="'" and s1[l]!=":" and s1[l]!=" ":
                if s1[l]!="[" and s1[l]!=",":
                        m1=m1+s1[l]
        login1[1][t][m].append(m1)
        m1=""
        m=""
        #k1=k1+1
        k1=0
        stopper=stopper-1
        a=a+1;b=b+1
        if b==2:
            c=c+1
        else:
            c=c+2
    return login1

def write(login,namefile):
    import csv
    fieldnames = [list(login[0].keys())[0],list(login[1].keys())[0]]#intestazioni csv prese dalle chiavi di login
    with open(f'{namefile}.csv', 'w', encoding='UTF8', newline='') as f:#apro per contrllo- l'ultimo metodo toglie la riga vuota che solitamente c'è fra dati e intestazioni con nome del csv a scelta variabile
        writer = csv.DictWriter(f, fieldnames=fieldnames) #nome del file e la lista con intestazioni
        writer.writeheader()#scrivo intestazione
        writer.writerows(login)#scrivo riga per volta