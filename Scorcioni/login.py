import datetime as dt
import csv

login=[
    {
        'prof':{
            'Gino':["Gino","ciaone"],
            'Bino':["Bino","tino"],
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


print(login)



import csv
fieldnames = ['prof','studenti']#intestazioni csv
#dati csv 


with open('login.csv', 'w', encoding='UTF8', newline='') as f:#apro per contrllo- l'ultimo metodo toglie la riga vuota che
#solitamente c'è fra dati e intestazioni
    writer = csv.DictWriter(f, fieldnames=fieldnames) #nome delfile e la lista con intestazioni
    writer.writeheader()#scrivo intestazione
    writer.writerows(login)#scrivo riga per volta

login1=[{},{}]
k=0;k1=0; m=""; m1=""
with open("login.csv") as csvfile:
  spamreader = csv.reader(csvfile)
  for row in spamreader:
        print(row[0])
        if k==0:
            n=row[0]
            t=row[1]
        elif k==1:
            s=row[0]
            login1[0][n]={}
        elif k==2:
            s1=row[1]
            login1[1][t]={}
        k=k+1
print(login1)
print(s)
print()
stopper=s.count("],")+1
stopperd=s.count(":")-1
while stopper!=0:
    if stopper==s.count("],")+1:
        len1=s.find(":")
        len2=s.find(",")
        len3=s.find("],")
        iniz=0
    else:
        #iniz=s.find("],")

        vird=s.count("],")-stopperd;no=0;ido=0
        while no!=vird:
            iniz=s.find("],",ido)
            ido=iniz+1
            no=no+1
        print(s[iniz]);print(iniz)

        vird=s.count(":")-stopperd;no=0;ido=0
        while no!=vird:
            len1=s.find(":",ido)
            ido=len1+1
            no=no+1
        print(s[len1]);print(len1)


        vird=s.count(",");no=0;ido=0
        while no!=vird:
            len2=s.find(",",ido)
            ido=len2+1
            no=no+1
        print(s[len2]);print(len2)


        vird=s.count("],")-stopperd;no=0;ido=0
        if stopper==1:
            len3=s.find("]}")
        else:
            while no!=vird:
                len3=s.find("],",ido)
                ido=len3+1
                no=no+1
        print(s[len3]);print(len3)
        #len1=s.find(":", (s.find(":")+1))
        #len2=s.find(",", (s.find(",", s.find(",")+1)+1))
        #if s.count("],")<2:
        
        #else:    
            #len3=s.find("],", (s.find("],")+1))
    print(iniz,len1)   
    for l in range(iniz,(len1+1)):
        if s[l]!="{" and s[l]!="'" and s[l]!=":" and s[l]!=" " and s[l]!="]":
            if s[l]!="[" and s[l]!=",":
                m=m+s[l]
    print(m)
    print(len1,len2)
    
    for l in range((len1),(len2)):
        if s[l]!="{" and s[l]!="'" and s[l]!=":" and s[l]!=" ":
            if s[l]!="[" and s[l]!=",":
                    m1=m1+s[l]
    print(m1)
    if k1==0:
        login1[0][n][m]=[]
    login1[0][n][m].append(m1)
    m1=""
    print(len2,len3)
    for l in range((len2),(len3)):
        if s[l]!="{" and s[l]!="'" and s[l]!=":" and s[l]!=" ":
            if s[l]!="[" and s[l]!=",":
                    m1=m1+s[l]
    print(m1)
    login1[0][n][m].append(m1)
    m1=""
    m=""
    #k1=k1+1
    k1=0
    stopper=stopper-1
    stopperd=stopperd-1
print(m)
print(m1)
print(login1)
print(s.find(",", (s.find(",", s.find(","))+1)))
'''
vir=3;n=0;indiceold=0
while n!=vir:
    indice=s.find(",",indiceold)
    indiceold=indice+1
    n=n+1
print(s[indice])
print(indice)
'''
