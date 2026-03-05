# programa para  Crea un juego donde la computadora elija

#---------------
#librerias
import random
#---------------

#---------------
#input
print("-------------------")
print("bienvenido al juego de adivinar el número")
print("-------------------")

#------------
co=input("numero: ")
print("-------------------")


#---------------
#proceso
numero_computadora = random.randint(1, 100)
intentos = 0
while True:
    intento_usuario = int(input("ingresa un número entre 1 y 100: "))
    intentos += 1
    if intento_usuario < numero_computadora:
        print("demasiado bajo, intenta de nuevo")
    elif intento_usuario > numero_computadora:
        print("demasiado alto, intenta de nuevo")
    else:
        print(f"¡felicidades! has adivinado el número en {intentos} intentos.")
        break

# fin del programa
