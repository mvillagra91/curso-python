# 1. Realiza las siguientes operaciones aritmÃ©ticas:
# â€¢	Suma: 15 + 25
suma = 25+15
# â€¢	Resta: 50 - 22
resta = 50-22
# â€¢	MultiplicaciÃ³n: 8 * 7
multiplicacion = 8*7
# â€¢	DivisiÃ³n: 100 / 20
division = 100/20

# 2. Calcula el resto de la divisiÃ³n de 37 entre 5 y almacÃ©nalo en una variable remainder. Luego imprÃ­melo.
resto = 37 % 5
print(resto)

# 3. Convierte el nÃºmero 7 en una cadena de texto y concatÃ©nalo con la frase â€œ es mi nÃºmero favoritoâ€. Imprime el resultado.
numero = str(7)
print("Cual es mi numero favorito "+numero)

# 4. Repite la palabra â€œPythonâ€ 10 veces usando el operador de multiplicaciÃ³n para cadenas y luego imprÃ­mela.
palabra = "python"
print(palabra * 7)

# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y almacena el 
# resultado en una variable booleana resultado. Imprime el valor de resultado.
a,b = 12,8

resultado = a>b
print(resultado)

# 6. Compara dos cadenas de texto (â€œappleâ€ y â€œbananaâ€) usando los operadores > y < y explica cuÃ¡l tiene mayor orden alfabÃ©tico.
a = "apple"
b = "banana"

if len(a) < len(b):
    print(a + " tiene menos letras que " + b)
elif a > b:
    print(a + " tiene mas letras que " +b)
elif a == b:
    print(a + " tiene las misma cantidad de letras que " + b)
else:
    print("Error al ingresar variables")

# 7. Realiza una comparaciÃ³n lÃ³gica usando and para verificar si el nÃºmero 
# 10 es mayor que 5 y menor que 20. Imprime el resultado.
print(10>5 and 5<20)

# 8. Usa el operador or para verificar si el nÃºmero 7 es menor que 3 o mayor que 5. Imprime el resultado.
print(7<3 or 3>5)

# 9. Aplica el operador not para invertir el resultado de la comparaciÃ³n 15 > 20. Â¿CuÃ¡l es el resultado?
print(not(15>20))

# 10. Combina operadores aritmÃ©ticos y lÃ³gicos: Verifica si el nÃºmero resultante de la expresiÃ³n 
# (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.
var1 = (5*3)+2

print(var1>10 and var1<20)