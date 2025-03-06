# #Ainult positiivsed arvud korrutame
# a=float(input("A: "))
# b=float(input("B: "))
# if a>0 and b>0:
#     print(f"Korrutis võrdub: {a*b}")



#   #Kas a on paaris või paaritu arv?
#   if a%2==0 and a!=0:
#         print(f"Arv {a} on paaris")
#  elif a==0:
#        print(f"Arv {a} on märamatu")
#  else:
#     print(f"Arv {a} on paaritu")

#    #Ema-robot 5-, 4-, 3-, 2-, 1-,
# try:
#     hinne=int(input("Mis hinne sai täna koolis?"))
#     if hinne in range(1,6):
#         print("Hinne")
#         if hinne==5:
#             print("VH")
#         elif hinne==4:
#             print("H")
#         elif hinne==3:
#             print("R")
#         else:
#             print("MR")
#     else:
#         print("Ei ole hinne")
# except Exception as e:
#     print("Viga:", e)
# from curses.ascii import isupper


# # #Ülesanne 1
# nimi=input("Mis su nimi on?")
# if nimi=="JUKU":
#     print("Lähme kinno")
#     vanus=int(input("Kui vana sa oled?"))
#     if 0<vanus<6:
#         print("Tasuta")
#     elif 6<=vanus<=14:
#         print("Lastepilet")
#     elif 14<=vanus<=65: 
#         print("Täispilet")
#     elif 65<=vanus<=100:
#         print("Sooduspilet")
#     elif vanus<=0 or vanus>=100:
#         print("Viga andmega")
# else:
#     print("Ma olen hõivatud! Mino kinno ise!")
    
# else:
#     print("ma olen hõivatud! Mine kinno ise!")

# #2 PINGINAABRID
# # ["Bohdan","Ruslan","ROBERT_PIKMI"]
# nimed=["Ruslan","RObert","BOhdan"]
# nimi1=input("sisetsta esimene nimi")
# nimi2=input("sisetsta teine nimi")
# nimi3=input("sisetsta kolmas nimi")
# if(nimi1 in nimed) and (nimi2 in nimed) and (nimi3 in nimed) and nimi1!=nimi2 and nimi2!=nimi3 and nimi1!=nimi3:
#     print("Pinginaabrid")
# else:
#     print("Ei ole pringinaabrid")
#3 remont
# try:
#     a = float(input("Sisesta pikkus: "))
#     b = float(input("Sisesta laius: "))
#     #--------
#     S = a * b
#     soov = input("Kas sa tahad remondi teha?: ")
#     if soov.lower() == "jah":
#         print("Remont")
#         hind = float(input("Hind: "))
#         #--------
#         koguhind = S * hind
#         print(f"Sul on vaja {koguhind} eur")
#     elif soov.lower() == "ei":
#         print("Head aega!")
#     else:
#         print("Palun sisesta jah või ei!")
# except:
#     print("Pikkus, laius ja hind peavad olema numbrid!")