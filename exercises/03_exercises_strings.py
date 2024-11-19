# 1. Declara una variable text con la frase â€œAprendiendo Pythonâ€ y luego imprime la longitud de la cadena usando len().
text = "Aprendiendo Python"

print(len(text))
# 2. Concatena dos cadenas: â€œHolaâ€ y â€œPythonâ€, y muestra el resultado en una sola lÃ­nea.
text1 = "Hola"
text2 = "Python"

print("{} {}".format(text1, text2))

# 3. Crea una cadena que incluya un salto de lÃ­nea, y luego imprÃ­mela para ver el resultado.
print("Esto es un\n salto de linea")

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
nombre, apellido, edad = "mario", "villagra", 33
print(f"mi nombre es {nombre} {apellido} y tengo {edad}")

# 5. Desempaqueta los caracteres de la palabra â€œPythonâ€ en variables separadas y luego imprÃ­melos uno por uno.
palabra = "Python"
a, b, c, d, e, f = palabra

print(f"{a,b,c,d,e,f}")
# 6. Extrae un â€œsliceâ€ de la palabra â€œProgramaciÃ³nâ€ para obtener los caracteres desde la posiciÃ³n 3 hasta la 7.
palabra_slide = "Programacion"
print(palabra_slide[3:8])

# 7. Invierte la cadena â€œPythonâ€ usando slicing y muestra el resultado.
cadena = "Python"
print(cadena[::-1])

# 8. Convierte la cadena â€œaprendiendo pythonâ€ en mayÃºsculas usando el mÃ©todo 
# adecuado e imprÃ­mela.
cadena = "Aprendiendo Python"
print(cadena.upper())

# 9. Cuenta cuÃ¡ntas veces aparece la letra â€œnâ€ en la cadena â€œProgramaciÃ³n en Pythonâ€.
cadena = "Programacion"
print(cadena.count("a"))

# 10. Verifica si la cadena â€œ12345â€ es numÃ©rica usando el mÃ©todo adecuado e imprime el resultado.
cadena = 123456789
print(cadena.is_integer())