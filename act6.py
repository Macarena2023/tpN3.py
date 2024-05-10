import math
coordenadas_cartesianas= (3, 6)

radio= math.sqrt(coordenadas_cartesianas[0]**2+coordenadas_cartesianas[1]**2)
angulo= math.atan2(coordenadas_cartesianas[1],coordenadas_cartesianas[0])

print("radio(distancia desde el origen:)", radio)
print("angulo(en radianes):", angulo)
