# from random import randint
# from kasutaja_funktsioonide import *

# #1
# while True:
#     try:
#         a=float(input("Arv1: "))
#         break
#     except:
#         print("Viga! Sisesta arv")
# while True:
#     try:
#         b=float(input("Arv2: "))
#         break
#     except:
#         print("Viga! Sisesta arv")
# while True:
#     try:
#         t=input("Tehe: ")
#         break
#     except:
#         print("Viga! Sisesta (/);(*);(+);(-)")
# vastus=arithmetic(a,b,t)
# print(vastus)


# #2
# aasta=int(input("Mis aasta tahad kontrollida: "))
# if aasta>0:
#     v=is_year_leap(aasta)
#     print(v)
#     if v:
#         print(f"{aasta} on liigasta")
#     else:
#         print(f"{aasta} ei ole liigasta")

# #3 square() kasutaimine
# #Kontroll while True ja try except
# while True:
#     try:
#         a=float(input("Ruudu külje pikkus: "))
#         break
#     except:
#         print("Viga! Sisesta arv")
# S,P,d=square(a)
# print(f"Ruudu pindala on {S}, ümbermõõt on {P} ja diagonaal on {d}")

# #4
# while True:
#         try:
#             a=int(input("Kuu number: "))
#             break
#         except:
#             print("Viga! Sisesta arv")
# vastus=season(a)
# print(vastus)
# #5
# def bank(summa:float, aastad:int, intress:float)->float:
#     """Funktsioon arvutab summa, mis on saadud intressi arvelt
#     :param float summa: Sisend kasutajalt
#     :param int aastad: Sisend kasutajalt
#     :param float intress: Sisend kasutajalt
#     :rtype: float summa
#     """
#     for aasta in range(aastad):
#         summa*=1.1
#     return summa
# #6
# def is_prime(a=randint(1,10000)):
#     """kirjeldage fuktsioon 
#     :param ....
#     :param ....
#     :rtype:...
#     """
#     print (a)
#     v=Truefor
#     for jagaja in range (2,a):
#        if a%jagaja==a:
#             v=False
#     return v
# #7
# def date(päev:int,kuu:int,aasta:int)->bool:
#     """
#     """
#     if päev in range(1,32) and kuu in [1,3,5,7,8,10,12] and aasta>0:
#         v=True
#     elif päev in range(1,30) and kuu==2 and is_year_leap(aasta):
#         v=True
#     elif päev in range(1,29) and kuu==2 and not is_year_leap(aasta):
#         v=True
#     elif päev in range(1,31) and kuu in [4,6,9,11] and aasta>0:
#         v=True
#     else:
#         v=False
#     return v 
        
