#VERSION 8_ajedrez - AUTOR : Fernando Alfonso


def amenaza_alfil (x1,x2,y1,y2):
    if abs(x2 - y2) == abs(y1 - x1):
        return True
    else :
        return False

x1 = int(input("Ingrese columna 1 = "))
x2 = int(input("Ingrese fila 1 = "))
casa1 = (x1, x2)
y1 = int(input("Ingrese columna 2 = "))
y2 = int(input("Ingrese fila 2 = "))
casa2 = (y1, y2)

import math

p1 = ((casa2[0] - casa1[0]) ** 2 + (casa2[1] - casa1[1]) ** 2)

r = math.sqrt(p1)

#if x1 == y1 or x2 == y2 :
    #print("Estas en JaqueMate")
#else :
    #print ("Aun estas a salvo")


if amenaza_alfil (x1,x2,y1,y2)  :
   print("Estas en JaqueMate")
else :
    print ("Aun estas a salvo")



