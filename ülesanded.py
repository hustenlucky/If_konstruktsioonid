from random import *from math import *
#�lesanne 1nimi=input("Mis on sinu nimi?: ")
vanus=int(input("Kui vana sa oled?: "))
print(f"Tere, maailm! Tervitan sind {nimi} Sa oled {vanus} aastat vana. ")print("Tere, maailm! Tervitan sind" ,nimi, "Sa oled",vanus,"aastat vana.")
print("Tere, maailm! Tervitan sind"+nimi+"Sa oled"+str(vanus)+"aastat vana")#�lesanne 2
from re import Matchvanus = 18
eesnimi = "Jaak"pikkus = 16.5
kas_k�ib_koolis = Trueprint(f"Muutuja {vanus} on {type(vanus)} t��bi")
print(f"Muutuja {eesnimi} on {type(eesnimi)} t��bi")print(f"Muutuja {pikkus} on {type(pikkus)} t��bi")
print(f"Muutuja {kas_k�ib_koolis} on {type(kas_k�ib_koolis)} t��bi")#�lesanne 3
kommidearv=randint(1,100)print(f"Laual on {kommidearv} kommid")
kommidv�tmud=int(input("Mitu kommi tahad �ra v�tta?"))onj��nud=kommidearv-kommidv�tmud
print(f"Laual on j��nud{onj��nud} komme")#�lesanne 4
�mberm��t=int(input("kui suur on �mberm�tt: "))l�bim��t=�mberm��t//pi
print(f"l�bim��t on +f{l�bim��t}")#�lesanne 5
N=float(input("Sisesta ristk�liku pikkus(N): "))M=float(input("Sisesta ristk�liku laius (M): "))
diagonaal=sqrt(N**2 + M**2)print(diagonaal)
#�lesanne 6aeg = float(input("Mitu tundi kulus s�iduks? "))
teepikkus = float(input("Mitu kilomeetrit s�itsid? "))kiirus = aeg / teepikkus
print("Sinu kiirus oli " + str(kiirus) + " km/h")
#�lesanne 7a1=randint(0,100)
a2=randint(0,100)a3=randint(0,100)
a4=randint(0,100)a5=randint(0,100)
keskmine=(a1+a2+a3+a4+a5)/5print(f"Arvud olid: {a1}, {a2}, {a3}, {a4}, {a5}. Nende keskmine on {keskmine}")
#�lesanne 8tekst= """ 
    @..@   (----)
  ( \__/ )  ^^ "" ^^ """
print(tekst)
print(      "@..@")
print(     "(----)")print(    "( \__/ )")
print("""  ^^ "" ^^   """)  
#�lesanne 9a=randint(1,100)
b=randint(1,100)c=randint(1,100)
P=a+b+c print(f"a={a}, b={b}, c={c}, P={P}")
#�lesanne 10pitsa = 12.90
hind = pitsa * 1.10person=randint(1,5)
hind_na_person=hind/personprint(f"pitsa={pitsa}, hind={hind}, hind_na_person={hind_na_person}, person={person}")
