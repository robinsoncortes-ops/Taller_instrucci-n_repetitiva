# programa para que calcule e imprima en cuántos meses, uniendo los dos capitales, pueden hacer el negocio que desean

#-----------------------------------
# libreria
import math


#-----------------------------------
# input
print("-------------------")
c1=float(input("ingresa el capital de pedro: "))
c2=float(input("ingresa el capital de juan: "))
print("-------------------")

#-----------------------------------
# proceso
n=0
while True:
    c1=c1+(c1*0.03)
    c2=c2+(c2*0.04)
    n=n+1
    if (c1+c2) >= 100000:
        break

#-----------------------------------
# output
print("--------------------")
print(" RESULTADO ")
print("--------------------")
print("unidos los capitales de ambos socios, pueden hacer el negocio que desean despues de: "+str(n)+" meses")
print("--------------------")
print("fin del programa")
print("--------------------")