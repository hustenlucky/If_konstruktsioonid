#töö 4.4
#1
from string import *
vokaali=["a","e";"o","i","ü,","õ","ä"]
konsonanti="qwrtpsdfghlzxcvbnmj"
numbrid=digits
märkid=punctuation
v=K=n=m=t=0
tekst=input("Sisend (sõna või lause):").lower()
tekst_list=list(tekst)
if tekst_list.index(" ")>0:
    print("see on lause")
    for s in tekst_list:
     if s in vokaali:
        v+=1
     elif s in konsonanti:
        k+=1
     elif s in numbrid:
        n+=1
     elif s in märkid:
        m+=1
     elif s==" ":
        t+=1
        print(f"V: {v \nK: {k}\nN: {n}\nM: {m}\nT: {t}")
else:
        print(f"kokku on {len(tekst_list)}")


# sõne="Programmeerimine"
# print(sõne)
# list_sõne=list(sõne)
# print(list_sõne)
# print(f"Viies täht: {list_sõne[4]}")
# print(f"Sõnes on {len(sõne)} t ")
# elemendid=[]
# for i in range(5):
#     elemendid.append(input(f"{i+1}. element: "))
# print(elemendid)
# for e in elemendid:
#     print(e)
# extend
# list_sõne.extend(elemendid)
# print(list_sõne)
# print(elemendid)
# insert
# elemendid.insert(0,"A")
# print(elemendid)
# remove
# elemendid.remove("A")
# print(elemendid)
# pop
# elemendid.pop()
# elemendid.pop()
# print(elemendid)
# index
# list_sõne.index("r")
# print(f"Täht r on {ind}-indeksiga")
# count
# k=list_sõne.count("r")
# print(f"Täht r kohtume {k} korda sõnas {sõne}")
# sort
# list_sõne.sort(reverse=True)
# print(list_sõne)
# reverse
# list_sõne.reverse()
# print(list_sõne)
# copy
# list_sõne2=list_sõne.copy() 
# clear
# list_sõne2.clear()
# print(list_sõne2)