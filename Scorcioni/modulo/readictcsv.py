def read(namefile):
    import csv
    login1=[{},{}]
    with open(f"{namefile}.csv") as csvfile:
        k=0
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
    k1=0; m=""; m1=""
    stopper=s.count("],")+1
    a,b,c=0,1,2
    while stopper!=0:
        if stopper==s.count("],")+1:
            len1=s.find(":")
            len2=s.find(",")
            len3=s.find("],")
            iniz=0
        else:
            #iniz=s.find("],")

            vird=a;no=0;ido=0
            while no!=vird:
                iniz=s.find("],",ido)
                ido=iniz+1
                no=no+1

            vird=b;no=0;ido=0
            while no!=vird:
                len1=s.find(":",ido)
                ido=len1+1
                no=no+1


            vird=c;no=0;ido=0
            while no!=vird:
                len2=s.find(",",ido)
                ido=len2+1
                no=no+1


            vird=a+1;no=0;ido=0
            if stopper!=1:
                while no!=vird:
                    len3=s.find("],",ido)
                    ido=len3+1
                    no=no+1
            else:
                len3=s.find("']}")
            #len1=s.find(":", (s.find(":")+1))
            #len2=s.find(",", (s.find(",", s.find(",")+1)+1))
            #if s.count("],")<2:
            
            #else:    
                #len3=s.find("],", (s.find("],")+1))
        for l in range(iniz,(len1+1)):
            if s[l]!="{" and s[l]!="'" and s[l]!=":" and s[l]!=" " and s[l]!="]":
                if s[l]!="[" and s[l]!=",":
                    m=m+s[l]
        
        for l in range((len1),(len2)):
            if s[l]!="{" and s[l]!="'" and s[l]!=":" and s[l]!=" ":
                if s[l]!="[" and s[l]!=",":
                        m1=m1+s[l]
        if k1==0:
            login1[0][n][m]=[]
        login1[0][n][m].append(m1)
        m1=""
        for l in range((len2),(len3)):
            if s[l]!="{" and s[l]!="'" and s[l]!=":" and s[l]!=" ":
                if s[l]!="[" and s[l]!=",":
                        m1=m1+s[l]
        login1[0][n][m].append(m1)
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

    k1=0; m=""; m1=""
    stopper=s1.count("],")+1
    a,b,c=0,1,2
    while stopper!=0:
        if stopper==s1.count("],")+1:
            len1=s1.find(":")
            len2=s1.find(",")
            len3=s1.find("],")
            iniz=0
        else:
            #iniz=s.find("],")

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
                print(s1[len3]);print(len3)
            else:
                len3=s1.find("']}")
            #len1=s.find(":", (s.find(":")+1))
            #len2=s.find(",", (s.find(",", s.find(",")+1)+1))
            #if s.count("],")<2:
            
            #else:    
                #len3=s.find("],", (s.find("],")+1))   
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
    fieldnames = [list(login[0].keys())[0],list(login[1].keys())[0]]#intestazioni csv
    #dati csv 
    with open(f'{namefile}.csv', 'w', encoding='UTF8', newline='') as f:#apro per contrllo- l'ultimo metodo toglie la riga vuota che
    #solitamente c'è fra dati e intestazioni
        writer = csv.DictWriter(f, fieldnames=fieldnames) #nome delfile e la lista con intestazioni
        writer.writeheader()#scrivo intestazione
        writer.writerows(login)#scrivo riga per volta
