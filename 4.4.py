# #töö 4.4
# #1
# from string import *
# vokaali=["a","e";"o","i","ü,","õ","ä"]
# konsonanti="qwrtpsdfghlzxcvbnmj"
# numbrid=digits
# märkid=punctuation
# v=K=n=m=t=0
# tekst=input("Sisend (sõna või lause):").lower()
# tekst_list=list(tekst)
# if tekst_list.index(" ")>0:
#     print("see on lause")
#     for s in tekst_list:
#      if s in vokaali:
#         v+=1
#      elif s in konsonanti:
#         k+=1
#      elif s in numbrid:
#         n+=1
#      elif s in märkid:
#         m+=1
#      elif s==" ":
#         t+=1
#         print(f"V: {v \nK: {k}\nN: {n}\nM: {m}\nT: {t}")
# else:
# print(f"kokku on {len(tekst_list)}")


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
# print(
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
#tund 4.4 "Listid"elemendid)
# pop
# elemendid.pop()
# elemendid.pop()
# print(elemendid)
# index
#1 ülesanne
# from string import *
# vokaali=["a","o","i","e","u","ü","õ","ä","ö"]
# konsonanti="qwrtypsdfghjklzxcvbnm"
# numbrid=digits
# märkid=punctuation
# v=k=n=m=t=0
# tekst=input("Sisend (sõna või lause): ").lower()
# tekst_list=list(tekst)
# if tekst_list.index(" ")>0:
#     print("See on lause")
#     for s in tekst_list:
#         if s in vokaali:
#             v+=1
#         elif s in konsonanti:
#             k+=1
#         elif s in numbrid:
#             n+=1
#         elif s in märkid:
#             m+=1
#         elif s==" ":
#             t+=1
#     print(f"V: {v}\nK: {k}\nN: {n}\nM: {m}\nT: {t}")
# else:
#     print(f"Kokku on {len(tekst_list)}")

# #2 ülesanne
# # 2.1 Попросит пользователя назвать пять имен, сохранит их в списке, отобразит в алфавитном порядке и добавит фамилию
# nimed=[]
# for i in range(5):
#     nimi=input(f"Sisesta {i+1}. nimi: ")
#     nimed.append(nimi)
# print("Tähestikulises järjekorras:", sorted(nimed))
# print("Viimati lisatud nimi:", nimed[-1])
# #Возможность изменения имен в списке
# muuda=input("Kas soovid nime muuta? (jah/ei): ")
# if muuda.lower()=="jah":
#     vana_nimi=input("Sisesta nimi, mida soovid muuta: ")
#     if vana_nimi in nimed:
#         uus_nimi=input("Sisesta uus nimi: ")
#         indeks=nimed.index(vana_nimi)
#         nimed[indeks]=uus_nimi
#         print("Uuendatud loend:", nimed)
#     else:
#         print("Nime ei leitud.")
# # 2.2 Список без повторов
# õpilased=["Juhan","Kati","Mario","Mario","Mati","Mati"]
# unikaalsed_õpilased=list(set(õpilased))
# print('Unikaalsed õpilased:', unikaalsed_õpilased)
# # 2.3 Возрастной список и расчеты
# vanused=[15, 22, 17, 19, 22, 16, 18]
# print("Vanuste kogusumma:", sum(vanused))
# print("Vanuste keskmine:", sum(vanused)/len(vanused))

# #3 ülesanne
# print("Lintdiagramm:")
# for vanus in vanused:
#     print("*" * vanus)

# #4 ülesanne
# postiindeks=input("Sisestage postiindeks: ")
# try:
#     postiindeks=int(postiindeks)
# except ValueError:
#     print("Vigane sisend! Palun sisesta viiekohaline number.")
#     exit()
# if postiindeks<10000 or postiindeks>99999:
#     print("Vigane sisend! Postiindeks peab olema viiekohaline number.")
#     exit()
# esimene_nr=postiindeks//10000
# if esimene_nr==1:
#     maakond="Tallinn"
# elif esimene_nr==2:
#     maakond="Narva, Narva-Jõesuu"
# elif esimene_nr==3:
#     maakond="Kohtla-Järve"
# elif esimene_nr==4:
#     maakond="Ida-Virumaa, Lääne-Virumaa, Jõgevamaa"
# elif esimene_nr==5:
#     maakond="Tartu linn"
# elif esimene_nr==6:
#     maakond="Tartumaa, Põlvamaa, Võrumaa, Valgamaa"
# elif esimene_nr==7:
#     maakond="Viljandimaa, Järvamaa, Harjumaa, Raplamaa"
# elif esimene_nr==8:
#     maakond="Pärnumaa"
# elif esimene_nr==9:
#     maakond="Läänemaa, Hiiumaa, Saaremaa"
# else:
#     maakond="Tundmatu piirkond"
# teade="Оставайтесь дома!" if esimene_nr in [1, 2, 3] else "Носите маски!"
# print(f"Postiindeks {postiindeks} kuulub piirkonda: {maakond}. {teade}")

# #ülesanne 5
# sisend=input("Sisestage numbrid komadega eraldatult: ")
# numbrid=(int(input(f"Sisestage {i+1}. number: ")) for i in range(int(input("Mitu numbrit soovite sisestada?: "))))
# if(numbrid)>2:
#     print("Listis peab olema vähemalt 2 elementi!")
#     exit()
# n=int(input("Mitu elementi soovite vahetada?: "))
# if n>len(numbrid)//2:
#     print("Vahetatavate elementide arv ei saa olla suurem kui pool listi pikkusest!")
#     exit()
# pikkus=len(numbrid)
# for i in range(n):
#     numbrid[i], numbrid[pikkus-1-i]=numbrid[pikkus-1-i], numbrid[i]

# print("Muutunud list:", numbrid)