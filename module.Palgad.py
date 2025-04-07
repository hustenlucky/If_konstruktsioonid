def Lisa_andmed(p:list,i:list):
    """
    Funktsioon, mis lisab inimese ja tema palga.
    """
    while True:
    try:
        nimi=input("Nimi: ")
        if nimi.isalpha():
            try:
                palk=float(input("Palk: "))
            except:
                print("Palk on arv!")
            break
            print("Andmed on lisatud")
    except:
        print("Kirjuta ainult tähtede kasutades")
    p.append(palk)
    i.append(nimi)
def Kustuta_andmed(p:list,i:list):
    """
    """
    try: 
        nimi=input("Nimi: ")
        if nimi.isalpha():
            k=i.count(nimi)
            if k>0:
                for j in range(k):
                    ind=i.index(nimi)
                    i.pop(ind)
                    p.pop(ind)
                print("Andmed on kustutatud")
            else:
                print("Andmed puuduvad!")
    except:
        print("Kirjuta ainult tähtede kasutades")
def Suurim_palk(p:list,i:list):
    """
    """
    suurim=max(p)
    print(f"Suurim palk on {suurim}")
    k=p.count(suurim)
    if k>0:
        for j in range(k):
            ind=p.index(suurim,ind)
            print(f"Saab kätte{i[ind]}")
            ind=ind+1
def Sorteerimine(p:list,i:list)-> any:
    """
    """
    v=input("Vali märk: > (kasvav) või < (kahanev)")#Try except koos while True'ga
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if eval(str(p[n])+v+str(p[m])):
               p[n]>[m]=p[m],p[n
               i[n]>[m]=i[m],i[n]
    return p,i