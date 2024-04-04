def media(nome, materia, diz):

    tot = sum(diz[nome][materia])
    numero = len(diz[nome][materia])

    return round(tot/numero, 1)


#andiamo a definire un prototipo del dizionario delle classi

classi = { #dizionario principale contiene le 2 classi

        'terza_m': { #dizionario 3m contiene tutti gli studenti
                                'ansaloni': { #1 stutente di 3m
                                        'matematica': [4,5.5], 'italiano': [6.7,7.25], 'storia': [5, 6], 'inglese': [8,8], 'informatica':[3,4.5] #gli studenti contengono come chiavi le materie, le materie sono delle liste di voti
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




a=0 #variabile contatore ausiliaria
i=0 #contatore del for
z=0 #contatore aux 2
materie = ['matematica', 'italiano', 'storia', 'inglese', 'informatica']
medie=[]



scelta = input("Scegliere la classe, M/H: ")
print("")




if scelta == 'M': #scelta la tabella della 3m

    nomi = classi['terza_m'].keys()

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

          else:
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
