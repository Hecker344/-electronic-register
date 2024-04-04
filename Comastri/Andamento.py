def Andamento():
    materia_prof = "matematica"
    classe='terza_h'
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
