# 1. Imprime "Â¡Hola Mundo!" por consola.

print("¡Hola Mundo!")

# 2. Escribe un comentario de una sola lÃ­nea explicando quÃ© hace el cÃ³digo del Ejercicio 1.

#Imprime por consola ¡Hola Mundo!

# 3. Imprime tu nombre y edad en la misma lÃ­nea utilizando la funciÃ³n print.
edad = 33
nombre = "Mario Villagra"

mensaje = "Mi nombre es " + nombre + " y tengo " + str(edad) #La funcion str transforma una variable a string
print(mensaje)

# 4. Usa la funciÃ³n type() para imprimir el tipo de dato de una cadena de texto, un nÃºmero entero y un nÃºmero decimal.

a = "cadena de texto"
b = 1
c = 0.2 

print(type(a))
print(type(b))
print(type(c))

# 5. Escribe un comentario en varias lÃ­neas explicando quÃ© son los tipos de datos en Python.
'''
    Los tipos de datos se pueden dividir en:
    string variable de texto
    int valores enteros
    float decimales
    etc
'''

# 6. Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".

print("Hola" + "Mundo")

# 7. Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma lÃ­nea.

nombre = "Mario"
edad = 33

print("Mi nombre es: "+nombre +" y mi edad es: "+ str(edad))

# 8. Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.

#nombre = input("Ingresa tu nombre")
#print("Hola {nombre}, bienvenido!")

# 9. Usa print() para mostrar el resultado de la suma de dos nÃºmeros enteros y el tipo de dato resultante.

a = 2
b = 3
resultado = a+b

print("El resultado es: " + str(resultado) + " y el tipo de dato del resultado es: "+ str(type(resultado)))

# 10. Comenta el cÃ³digo del Ejercicio 9, y explica quÃ© hace cada lÃ­nea usando comentarios de una sola lÃ­nea.

#Agrego valores a las variables a y b
a = 2
b = 3
#Guardo la suma de las variables a y b en resultado
resultado = a+b

#Imprimo el resultado y el tipo del resultado, para esto convierto las variables en string para evitar conflictos
print("El resultado es: " + str(resultado) + " y el tipo de dato del resultado es: "+ str(type(resultado)))