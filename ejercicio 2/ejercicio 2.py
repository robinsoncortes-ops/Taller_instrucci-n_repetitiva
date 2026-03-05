# programa para Tu jefe tiene 50 puntos de vida (HP)

#---------------
# librerías
import math

#---------------
# input
#---------------
print("-------------------")
print("Tu jefe tiene 50 puntos de vida (HP)")
print("-------------------")

#---------------
# proceso
#---------------
hp = 50
while hp > 0:
    ataque = int(input("ingresa el daño del ataque: "))
    hp -= ataque
    print(f"tu jefe tiene {hp} HP")
print("-------------------")
print("tu jefe ha muerto")
print("-------------------")
# fin del programa
