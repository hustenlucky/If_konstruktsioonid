from math import *
import math
#-------------
print("Ruudu karakteristikud")
try:
    a=int(input('Sisesta ruudu külje pikkus => '))
    if a>0:
        S=a**2
        print("Ruudu pindala", S)
        P=4*a
        print("Ruudu ümbermõõt", P)
        di=a*math.sqr(2)
        print("Ruudu diagonaal", round(di,2))
    else: 
        print("Külg ei saa olla <=0-ga")
except:
    print("Külje suurus on vaja int formaadis sisestada!")
#-------------

#-------------
print("Ristküliku karakteristikud")
try:
    b=int(input("Sisesta ristküliku 1. külje pikkus => "))
    c=int(input("Sisesta ristküliku 2. külje pikkus => "))
    if b>0 and c>0:
                S=b*c
                print("Ristküliku pindala", S)
                P=2*(b+c)
                print("Ristküliku ümbermõõt", P)
                di=math.sqrt(b*2+c*2)
    else:
        print("Ristküliku diagonaal", round(di))
except:
    print("Ristküliku 1. või 2. on vaja int formaadis sisestada!")
#-------------


#-------------
print("Ringi karakteristikud")
try:
    r=int(input("Sisesta ringi raadiusi pikkus =>"))
    if r>0:
        d=2*r
        print("Ringi läbimõõt", d)
        S=pi*r*2
        print("Ringi pindala", round (S))
        C=2*pi*r
        print("Ringjoone pikkus", round (C))
    else:
        print("Külg ei saa olla <=0-ga")
except:
    print("Ristküliku raadius on vaja int formaadis sisestada!")