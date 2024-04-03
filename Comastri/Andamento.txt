def Andamento():
    materia_prof = "matematica"
    classe='terza_h'
    cognome = input("Inserire il cognome dello studente del queale si vuole sapere i voti e la media:")
    if classi[classe][cognome][materia_prof]!=0:
        print("I voti di",cognome,"in",materia_prof,"sono:",classi[classe][cognome][materia_prof])
        voti = classi[classe][cognome][materia_prof]
        somma=0
        for x in voti:
            somma=somma+voti[x]
        media=somma/len(voti)
        print("La media di",cognome,"in",materia_prof,"è:",media)
    else:
        print(cognome,"in",materia_prof,"non ha voti")
Andamento()