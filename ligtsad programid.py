from datetime import *
from math import *
from time import strptime
from cgi import print_arguments
from datetime import *
from calendar import *
# tana=date.today()
# print(f"Tere! T�na on {tana}.")

# # 27/12/2022
# tana1 = tana.strftime("%d/%m/%Y")
# print(tana1)
# # December 27, 2022
# tana2 = tana.strftime("%B %d, %Y")
# print(tana2)
# # 12/27/22
# tana3 = tana.strftime("%m/%d/%y")
# print(tana3)
# # Dec-27-2022
# tana4 = tana.strftime("%b-%d-%Y")
# print(tana4)

# p�ev=tana.day
# kuu=tana.month
# aasta=tana.year
# print(f"P�ev on {p�ev}, \nKuu on {kuu}, \nAasta on {aasta}")
# paevad=monthrange(2025,2)[1]
# onjaanud=paevad-p�ev
# print(f"Kuu l�puni on j��nud {onjaanud} p�evad")

# p�evad_aastal = (date(aasta, 12, 31) - tana).days
# print(f"Kuni aasta l�puni on j��nud {p�evad_aastal} p�evad")

# try:
#     s�nnip�ev=input("S�nnip�ev: ") #YYYY-MM-DD
#     sp=datetime.strptime(s�nnip�ev, "%Y-%m-%d")
#     print(sp)
#     vanus_aastades=tana.year-sp.year
#     vanus_kuudes=vanus_aastades*12
#     print(f"Vastus: Vanus {vanus_aastades} aastad")
# except:
#     print("Sa pead YYYY-MM-DD format kasuada sisestamisel.")
   

# #�lesanne 2
# #sulgude kasutamine

# print("a=3 + 8 / (4-2) * 4")
# a=3 + 8 / (4-2) * 4
# print (a)
# print("a=(3 + 8)/ (4 - 2) * 4")
# a=(3 + 8) / (4 - 2) * 4
# print (a)

#�lesanne 3
try:
    R=float(input("Sisesta R, kus R on ringi raadius:"))
    #==,!=, <, >, <=, >=
    if R<=0:
        print("Nulliga ja neg. arvudega ei ole m�tte t��tada!")
    else:
        Ringi_S=round(pi*R**2,2)
        Ringi_P=round(2*pi*R,2)
        Ruudsu_S=2*R*2*R
        Ruudu_P=4*2*R
        print(f"Ringi_S={Ringi_S}\nRingi_P={Ringi_P}\nRuudsu_S={Ruudsu_S}\nRuudu_P={Ruudu_P}")
except: 
    print("Sisesta ainult arvud!!!")


