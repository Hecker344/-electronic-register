def Debito():
    materia_prof = "matematica"
    for x in classi:
        for y in classi[x]:
            voti=classi[x][y][materia_prof] #andiamo a fare tutti i possibili casi di studenti
            somma = 0
            media = sum(voti)/len(voti) # facciamo la media di ogni studente
            if media < 6: # in caso in qui lo studente abbia la media inferiore al 6 lo stampiamo
                print(y,"ha la media insufficente")




Debito()
