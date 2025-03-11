from math import *
##5
a = input("Sisesta number või tekst: ")

if a.isdigit():
    print(f"50% arvust: {int(a) * 0.5}")
elif a.replace('.', '', 1).isdigit() and a.count('.') < 2:
    print(f"70% arvust: {float(a) * 0.7}")
elif a.isalpha():
    print(f"Sisestasite teksti: {a}")
else:
    # print("Vale sisend.")
#6:
try:
    küsimus = input("Kas sa tahad lahendada ruutvõrrandi? ")
    if küsimus.lower()=="jah":
        print("Võrrand: a*x**2+b*x+c=0")
        a=int(input("Sisesta arv a: "))
        b=int(input("Sisesta arv b: "))
        c=int(input("Sisesta arv c: "))
        D=b^2-4*a*c
        print(f"D={D}")
        if D>0:
            x1=(-b+sqrt(D))/2*a
            x2=(-b-sqrt(D)/2*a)
            print(f"Võrrand on lahendatud, x1={round(x1, 2)} ja x2={round(x2, 2)}")
        elif D==0:
            x=-b/(2*a)
            print(f"Võrrand on lahendatud,x={round(x, 2)}")
        elif D<0:
            print("Lahendusi pole")
    else:
        print("ok")
except:
    print("Viga")
