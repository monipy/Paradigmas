#Alumna: Mónica González
#C.I.: 3.757.986
#Descripción de la tarea
#Adivina un número
#Escribir un programa en Python que realice lo siguiente:
#-Solicitar al usuario un número que definirá el rango dentro del cual el programa elegirá un número al azar.
#-Solicitar al usuario un número que definirá la cantidad de oportunidades que tiene el usuario para adivinar el número elegido por el programa.
#-En base a los datos obtenidos, ejecutar un ciclo solicitando al usuario un número, y finalizando cuando se agoten las oportunidades o el usuario adivine el número.
#Para obtener el número al azar, se recomienda usar el módulo random de la biblioteca estándar de Python.
#!/usr/local/bin/python
import random
intentos = 0
print('Adivina un número')
print('Ingresa el rango de los numeros para adivinar ')
rango1 = int(input())
rango2 = int(input())
numero = random.randint(rango1, rango2)
print('Ingresa la cantidad de oportunidades para adivinar ')
optunidades = int(input())
while intentos < optunidades:
     print('Intenta adivinar.') # Hay cuatro espacios delante de print.
     estimacion = int(input())
     intentos = intentos + 1
     if estimacion < numero:
         print('Es un numero mas alto.') # Hay ocho espacios delante de print.
     if estimacion > numero:
         print('Es un numero mas bajo')
     if estimacion == numero:
         break
if estimacion == numero:
      intentos = str(intentos)
      print('¡Bien! ¡Adivinaste en ' + intentos + ' intentos!')
if estimacion != numero:
      número = str(numero)
      print('No adivinaste, el numero es ' + número)
