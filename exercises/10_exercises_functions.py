# 1. Crea una funciÃ³n llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, 
# <nombre>". Si no se proporciona ningÃºn nombre, debe saludar diciendo "Hola, desconocido".
def personalized_greeting(nombre = "desconocido"):
    print(f"Hola, {nombre}")
    
personalized_greeting("Mario")
# 2. Escribe una funciÃ³n llamada "multiply" que reciba dos nÃºmeros como argumentos y retorne el resultado de multiplicarlos.
def multiply(number1, number2):
    return number1*number2

# 3. Crea una funciÃ³n llamada "is_even" que reciba un nÃºmero entero como argumento y retorne True si es par y False si es impar.
def is_even(numero_entero):
    return numero_entero % 2 == 0

# 4. Escribe una funciÃ³n llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayÃºsculas.
def convert_to_uppercase(cadena_texto):
    return cadena_texto.upper()

# 5. Crea una funciÃ³n llamada "arbitrary_sum" que reciba un nÃºmero arbitrario de nÃºmeros como argumentos 
# y retorne la suma de todos ellos.
def arbitrary_sum(*numeros):
    return sum(numeros)

# 6. Escribe una funciÃ³n llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, 
# y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.
def generate_full_greeting(nombre = "<nombre>", apellido = "<apellido>"):
    print(f"Hola, {nombre} {apellido}")

generate_full_greeting()

# 7. Crea una funciÃ³n llamada "power" que reciba dos nÃºmeros: base y exponente, y retorne el 
# resultado de elevar la base al exponente.
def power(base, exponente):
    return base ** exponente

# 8. Escribe una funciÃ³n llamada "calculate_average" que reciba tres nÃºmeros y retorne su promedio.
def calculate_average(num1, num2, num3):
    return (num1+num2+num3)/3

print(calculate_average(5,5,5))
    
# 9. Crea una funciÃ³n llamada "count_characters" que reciba una cadena de texto y retorne el nÃºmero de caracteres que contiene.
def count_characters(cadena_texto):
    return len(cadena_texto)
    
print(count_characters("hola"))

# 10. Escribe una funciÃ³n llamada "display_messages" que reciba un nÃºmero indefinido de cadenas
# y las imprima en mayÃºsculas, una por una, tal como se hizo en el archivo proporcionado.
def display_messages(*cadenas):
    print((f" {cadenas}").upper())
    
display_messages("prueba", "prueba2", "prueba3")