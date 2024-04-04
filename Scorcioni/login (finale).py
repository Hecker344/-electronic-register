import datetime as dt
import readdictcsv as redict
login=[
    {
        'prof':{
            'Gino':["Gino","ciaone"],
            'eino':["eino","tino"],
            'wino':["wino","aatino"],
            'tino':["tino","ciaone"],
            'uino':["uino","tino"],
            'Rino':["Rino","aatino"],
            'Fonti':["Fonti","taino"]
            
        }
        
    },
    {
        'studenti':{
            'Toni':["Toni","mucca"],
            'Fino':["Buino","tamino"]
        }
        
    }
        ]

scelt=int(input("Se sei un prof premi 0, se sei uno studente premi 1: "))
if scelt==0:
    nomut=input("Inserisci il nome utente: ")
    psw=input("Inserisci la password: ")
    if nomut==login[0]['prof'][nomut][0] and psw==login[0]['prof'][nomut][1]:
        print("Login eseguito!")
elif scelt==1:
    nomut=input("Inserisci il nome utente: ")
    psw=input("Inserisci la password: ")
    if nomut==login[0]['studenti'][nomut][0] and psw==login[1]['studenti'][nomut][1]:
        print("Login eseguito!")
else:
    print("opzione non esistente")

f=redict.read("login")
print(f)
