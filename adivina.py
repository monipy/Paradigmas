# Alumna: Mónica González
# C.I.: 3.757.986

# Descripción de la tarea 1
# Adivina un número
# Escribir un programa en Python que realice lo siguiente:
# -Solicitar al usuario un número que definirá el rango dentro del cual el programa elegirá un número al azar.
# -Solicitar al usuario un número que definirá la cantidad de oportunidades que tiene el usuario para adivinar el número elegido por el programa.
# -En base a los datos obtenidos, ejecutar un ciclo solicitando al usuario un número, y finalizando cuando se agoten las oportunidades o el usuario adivine el número.
# Para obtener el número al azar, se recomienda usar el módulo random de la biblioteca estándar de Python.

# Descripción de la tarea 2
# Una vez finalizada la tarea anterior, aplicar en el código desarrollado los factores internos de calidad del software:
#1. Mejorar la legibilidad del código en base a lo establecido en los documentos PEP 8 y Python Idiomático.
#2. Agregar al código manejo de excepciones (control de errores) con la estructura try..except.
#3. Aplicar el paradigma modular para lograr reusabilidad de código:
#a) Identificar bloques de código redundantes y convertirlos en procedimientos o funciones independientes, respetando el principio de "caja negra".
#b) Identificar cuáles de estos subprogramas podrían ser utilizados en proyectos distintos al actual, y agruparlos en su propio módulo externo.
# !/usr/local/bin/python
import random

print('Adivina un número')
print('Ingresa el rango de los numeros para adivinar ')
rango1 = input("Desde: ")
rango1 = int(rango1)
rango2 = input("Hasta: ")
rango2 = int(rango2)

def generarAleatorio(rango1, rango2):
    try:
        if rango1 > rango2:
            aux = rango1
            rango1 = rango2
            rango2 = aux
        return random.randint(rango1, rango2)
    except TypeError:
        print("Debes ingresar valores numericos.  Intente nuevamente...")
        return -1


num_buscado = generarAleatorio(rango1, rango2)

oportunidades = input("Ingresa la cantidad de oportunidades para adivinar: ")
oportunidades = int(oportunidades)
intentos = 0

while intentos < oportunidades:
    print('Intenta adivinar.')
    estimacion = int(input())
    intentos = intentos + 1
    if estimacion < num_buscado:
        print('Es un numero mas alto.')
    if estimacion > num_buscado:
        print('Es un numero mas bajo')
    if estimacion == num_buscado:
        break

if estimacion == num_buscado:
    intentos = str(intentos)
    print('¡Bien! ¡Adivinaste en ' + intentos + ' intentos!')

if estimacion != num_buscado:
    num_buscado = str(num_buscado)
    print('No adivinaste, el numero es ' + num_buscado)
