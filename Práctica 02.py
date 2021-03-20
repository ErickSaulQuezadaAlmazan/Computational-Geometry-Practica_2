'''
INTSITUTO POLITÉCNICO NACIONAL
ESCUELA SUPERIOR DE CÓMPUTO
ESCOM

COMPUTATIONAL GEOMETRY

ALUMNO: QUEZADA ALMAZÁN ERICK SAÚL
PRÁCTICA 02: 19-03-21
FECHA DE ENTREGA: 26-03-21 
'''

print("B I E N V E N I D O\n")
# Inciso A) Describe el conjunto de puntos.
print("Considerando S en E^2 un conjunto finito de puntos, podemos establecer el conjunto de puntos de S de la siguiente manera:")
A=[]
coordenada = int(input("Ingrese la coordenada x del punto A: "))
A.append(coordenada)
coordenada = int(input("Ingrese la coordenada y del punto A: "))
A.append(coordenada)
print(f"El punto A es: {A}\n")

B=[]
coordenada = int(input("Ingrese la coordenada x del punto B: "))
B.append(coordenada)
coordenada = int(input("Ingrese la coordenada y del punto B: "))
B.append(coordenada)
print(f"El punto B es: {B}\n")

C=[]
coordenada = int(input("Ingrese la coordenada x del punto C: "))
C.append(coordenada)
coordenada = int(input("Ingrese la coordenada y del punto C: "))
C.append(coordenada)
print(f"El punto C es: {C}\n")

#Inciso B) Defina los segmentos de línea ordenados en S.
print("Posteriormente, definimos los segmenentos de recta.")
print(f"Unimos el punto A: {A} y el punto B: {B} con líneas rectas para construir nuestro polígono.")
print(f"Luego, unimos el punto B: {B} y el punto C: {C} con líneas rectas para construir nuestro polígono.")

#Inciso C) Genere un polígono para S.
print(f"De esta manera tenemos construido nuestro polígono, se trata de un triángulo con los puntos\nA={A}, B={B} y C={C}")
print("\n")

#Inciso d) Genere un polígono en forma de estrella para S.
print("Para poder estrellar el polígono generado, debe seleccionar uno de los puntos como referencia.")
NuevoPunto= input("¿Cuál de los puntos ingresados desea tomar como referencia para estrellar (A, B, C)? ")
print("\n")

if (NuevoPunto == 'A'):
    Z=A
    print("El punto referencia se llamará 'Z' y procederemos a unir el punto 'Z' a los otros restantes")
    print(f"Con Z={Z}, tenemos que:")
    print(f"Unimos el punto Z al punto B: {B} y luego unimos Z al punto C: {C}")
    print("De esta manera tenemos el polígono en forma de estrella para S")

elif (NuevoPunto == 'B'):
    Z = B
    print("El punto referencia se llamará 'Z' y procederemos a unir el punto 'Z' a los otros restantes")
    print(f"Con Z={Z}, tenemos que:")
    print(f"Unimos el punto Z al punto A: {A} y luego unimos Z al punto C: {C}")
    print("De esta manera tenemos el polígono en forma de estrella para S")

elif(NuevoPunto == 'C'):
    Z = C
    print("El punto referencia se llamará 'Z' y procederemos a unir el punto 'Z' a los otros restantes")
    print(f"Con Z={Z}, tenemos que:")
    print(f"Unimos el punto Z al punto A: {A} y luego unimos Z al punto B: {B}")
    print("De esta manera tenemos el polígono en forma de estrella para S")

else:
    print(f"ERROR!. No hay un punto con la etiqueta '{NuevoPunto}'. Intente Nuevamente, por favor.")