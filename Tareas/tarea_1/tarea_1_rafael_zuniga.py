# -*- coding: utf-8 -*-
"""Tarea#1 Rafael Zuniga.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18RlwnGSMY0ntQr6CGqnRAfHze_a1JGfA
"""

print("Ejercicio Bisiesto")
anio = int(input("Ingrese el año: "))
if(anio % 400 == 0) or (anio % 4 == 0) and (anio % 100 != 0):
  print ("El año es Bisiesto")
else:
  print ("El año no es Bisiesto")

print("Ejercicio Meses Switch")
switcher={1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
argument=int(input("Ingrese un numero:"))
nombreDeMes=switcher.get(argument,"Mes invalido")
print(nombreDeMes)

print("Ejercicio Capital Ciclos")
C=-1
I=0
M=0
while(C<0) or (I<=0) or (I>=100) or (M<=0):
  print ("Introduce el capital, el interes, y el tiempo apropiados")
  C=int(input("Capital: "))
  I=int(input("Interes: "))
  M=int(input("Tiempo en Annios: "))

for i in range(M):
  C=C*(1+ I/100)
  print("Monto", C, "Colones")

print("Ejercicio Suma Ciclos")
print("Digite un numero")
numero=int(input("Numero: "))

while numero>0:
  Suma=0
  for i in range(1,numero+1):
    if(numero % i==0):
      Suma=Suma + i
  print (Suma)
  numero=int(input("Numero: "))