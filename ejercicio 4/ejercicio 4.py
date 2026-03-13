# Una pelota se deja caer desde una altura h

#---------------------------------- 
# libreria
import math

#----------------------------------
# input
print("-------------------")
h=float(input("ingresa la altura desde la que se deja caer la pelota: "))
print("-------------------") 
print("-------------------")

#----------------------------------
# proceso
#----------------------------------
while True:
    h=h-(h*0.1)
    n=n+1
    if h <= 0.1:
        break

#----------------------------------
# output
print("--------------------")
print(" RESULTADO ")
print("--------------------")
print("la pelota llego a menos de 1/5 de su altura inicial despues de rebotar: "+str(n)+" veces")
print("--------------------")
print("fin del programa")
print("--------------------")