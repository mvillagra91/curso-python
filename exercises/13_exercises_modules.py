# 1. Crea un mÃ³dulo llamado "calculator" que contenga funciones para sumar, restar, multiplicar y dividir 
# dos nÃºmeros. Importa este mÃ³dulo en otro archivo y usa sus funciones.

import calculator

calculator.dividir(2,2)
calculator.sumar(2,2)
calculator.multiplicar(2,2)
calculator.restar(2,2)

# 2. Crea un mÃ³dulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit. 
# Escribe un programa que importe este mÃ³dulo y realice conversiones.
from converter import celsius_to_farenheit
celsius_to_farenheit(1)

# 3. Crea un mÃ³dulo que contenga una lista de nombres de estudiantes y una funciÃ³n que imprima 
#todos los nombres. Importa este mÃ³dulo en otro archivo y usa la funciÃ³n para mostrar la lista.
from listaEstudiantes import imprimirLista

imprimirLista()
# 4. Crea un mÃ³dulo llamado "geometry" que tenga una funciÃ³n para calcular el Ã¡rea de un cÃ­rculo y un 
# cuadrado. Usa este mÃ³dulo en otro archivo para calcular Ã¡reas.
from geometry import area_circulo, area_cuadrado

print(area_cuadrado(5))
print(area_circulo(3))

# 5. Escribe un mÃ³dulo que contenga una funciÃ³n que acepte cualquier nÃºmero de argumentos y 
# devuelva su suma. Importa y usa la funciÃ³n en otro archivo.
print(calculator.sumar_valores(3,2,1,5))

# 6. Crea un mÃ³dulo que defina una clase llamada "Car" con propiedades como marca, modelo y aÃ±o. 
# Importa este mÃ³dulo en otro archivo y crea una instancia de la clase "Car".

import moduloCar

my_car = moduloCar.Car("Suzuki", "Escudo", 1993)
#print(my_car.display_info())
# 7. Escribe un mÃ³dulo que contenga funciones para leer y escribir en archivos de texto. 
# Crea un programa que use estas funciones para escribir y leer datos.
# file_module.py

#def write_to_file(filename, content):
#    with open(filename, 'w') as file:
#        file.write(content)
#
#
#def read_from_file(filename):
#    with open(filename, 'r') as file:
#        return file.read()

# 8. Crea un mÃ³dulo llamado "statistics" que tenga funciones para calcular la media y 
# la mediana de una lista de nÃºmeros. Usa este mÃ³dulo para calcular estos valores en una lista dada.

import statistics

def media(*lista):
    media = statistics.mean(lista)
    mediana = statistics.median(lista)
    
    print(f"La media es: {media} y la mediana es: {mediana}")


# 9. Crea un mÃ³dulo que contenga una funciÃ³n para contar cuÃ¡ntas veces aparece una palabra en un texto. 
# Escribe un programa que importe el mÃ³dulo y lo use para contar palabras en una cadena.
from condadorPalabras import contador
print(contador("Hola como estas, esto es una cadena de palabras"))

# 10 Crea un mÃ³dulo llamado "dates" que contenga funciones para obtener la fecha actual y 
# calcular la diferencia entre dos fechas. Usa este mÃ³dulo en un programa para mostrar la fecha 
# actual y la diferencia entre dos fechas especÃ­ficas.
from dateTime import date_difference, get_current_date

print(get_current_date())
print(date_difference("2024/01/01", "2024/10/01"))