import math

print("Ruudu karakteristikud")
a = float(input("Sisesta ruudu k�lje pikkus => "))
S = a**2
P = 4 * a
di = a * math.sqrt(2)
print("Ruudu pindala", S)
print("Ruudu �mberm��t", P)
print("Ruudu diagonaal", round(di, 2))


print("Ristk�liku karakteristikud")
b = float(input("Sisesta ristk�liku 1. k�lje pikkus => "))
c = float(input("Sisesta ristk�liku 2. k�lje pikkus => "))
S = b * c
P = 2 * (b + c)
di = math.sqrt(b**2 + c**2)
print("Ristk�liku pindala", S)
print("Ristk�liku �mberm��t", P)
print("Ristk�liku diagonaal", round(di, 2))


print("Ringi karakteristikud")
r = float(input("Sisesta ringi raadiusi pikkus => "))
d = 2 * r
S = math.pi * r**2
C = 2 * math.pi * r
print("Ringi l�bim��t", d)
print("Ringi pindala", round(S, 2))
print("Ringjoone pikkus", round(C, 2))

