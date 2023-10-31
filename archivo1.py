#VERSION 7_Distancia - AUTOR : Fernando Alfonso

x1 = int(input("Ingrese columna 1 = "))
x2 = int(input("Ingrese fila 1 = "))
casa1 = (x1, x2)
y1 = int(input("Ingrese columna 2 = "))
y2 = int(input("Ingrese fila 2 = "))
casa2 = (y1, y2)

import math

p1 = ((casa2[0] - casa1[0]) ** 2 + (casa2[1] - casa1[1]) ** 2)

r = math.sqrt(p1)

print("La distancia entre las casas es de", r, "casas")