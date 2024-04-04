def Pagella(aula):
    classe = 'terza_h'
    cognome = 'gazzotti'
    medie = []
    somma = 0
    materie = ['matematica','italiano','storia','informatica','inglese']
    if classe in aula and cognome in aula[classe]:
        for x in range(5):
            voti = aula[classe][cognome][materie[x]]
            somma = sum(voti)
            media=somma/len(voti)
            medie.append(media)
    else:
        print("Cognome non trovato")
    print(medie)
    colori=[]
    for z in medie:
        if z<=5.5:
            colori.append('red')
        elif z>5.51 and z<=6:
            colori.append('yellow')
        else:
            colori.append('green')
    print(colori)
    plt.bar(materie,medie,color=colori)
    plt.title('Pagella')
    plt.xlabel('Materie')
    plt.ylabel('Voti')
    plt.show()
    return medie