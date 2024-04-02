
def media(nome, materia, diz):

    tot = sum(diz[nome][materia])
    numero = len(diz[nome][materia])

    return round(tot/numero, 1)


#andiamo a definire un prototipo del dizionario delle classi

classi = {

        'terza_m': {
                                'Vancini': {
                                        'matematica': [5, 7, 8.5, 9], 'italiano': [2, 5, 4.3, 7], 'storia': [5, 2, 8, 4]
                                    }
                                ,

                                'Tostati': {
                                        'matematica': [6, 3, 5.5, 8], 'italiano': [10, 6, 9, 8.75], 'storia': [2, 3, 4, 5]
                                    }

                                ,

                                'Galeone': {
                                        'matematica': [2, 3, 8, 1], 'italiano': [5, 2, 1, 5], 'storia': [7, 3, 6, 6]
                                    }
                    }
        ,

        'terza_h': {

                                'Crispino': {
                                    'matematica': [1, 1, 1, 1], 'italiano': [1, 1, 1, 2], 'storia': [1, 1, 1, 3]
                                }
                                ,

                                'Bruni': {
                                    'matematica': [2, 2, 2, 2], 'italiano': [2, 2, 2, 3], 'storia': [2, 2, 2, 4]
                                }

                                ,

                                'Comastri': {
                                    'matematica': [3, 3, 3, 3], 'italiano': [3, 3, 3, 4], 'storia': [3, 3, 3, 5]
                                }
        }
}




a=0 #variabile contatore ausiliaria
i=0 #contatore del for
z=0 #contatore aux 2
materie = ['matematica', 'italiano', 'storia']
medie=[]



scelta = input("Scegliere la classe, M/H: ")




if scelta == 'M': #scelta la tabella della 3m

    nomi = classi['terza_m'].keys()

    if a==0: #se ci troviamo al primo ciclo

        print('Nome studente:      Media italiano:      Media matematica:    Media storia:')


    for i in nomi:

      c=i
      while len(c)<14: #standardizzo la lunghezza del nome per evitare problemi di indentazione
          c = c + ' '
      print(c, end = '      ')


      for z in materie:

          if z!='storia':
            print( media(i, z, classi['terza_m']), end='                  ' )

          else:
              print(media(i, z, classi['terza_m']))

else: #scelta la tabella della 3h

    nomi = classi['terza_h'].keys()

    if a == 0:  # se ci troviamo al primo ciclo

        print('Nome studente:       Media italiano:    Media matematica:  Media storia:')

    for i in nomi:

        c = i
        while len(c) < 14:  # standardizzo la lunghezza del nome per evitare problemi di indentazione
            c = c + ' '
        print(c, end='       ')

        for z in materie:

            if z != 'storia':
                print(media(i, z, classi['terza_h']), end='                ' )

            else:
                print(media(i, z, classi['terza_h']))