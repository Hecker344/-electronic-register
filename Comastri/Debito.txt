def Debito():
    materia_prof = "matematica"
    for x in classi:
        for y in classi[x]:
            voti=classi[x][y][materia_prof]
            somma = 0
            media = sum(voti)/len(voti)
            if media < 6:
                print(y,"ha la media insufficente")




Debito()