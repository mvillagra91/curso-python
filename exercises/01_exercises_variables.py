# 1. Declara y asigna valores a las siguientes variables:
# â€¢	name: una cadena que contenga tu nombre.
name = "mario"
# â€¢	age: un nÃºmero entero que represente tu edad.
age = 33
# â€¢	height: un nÃºmero flotante que represente tu altura.
height = 1.66
# â€¢	Imprime cada variable en una lÃ­nea separada.
print(name)
print(age)
print(height)

# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuÃ¡ntos aÃ±os tienes.
print("Tengo "+str(age))

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False segÃºn corresponda e imprÃ­mela.
is_student = True
print(is_student)

# 4. Usa la funciÃ³n len() para calcular cuÃ¡ntos caracteres tiene tu nombre completo, almacenado en una variable.
tam_name = len(name)

# 5. Declara tres variables en una sola lÃ­nea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
nombre, apellido, ciudad_origen = "mario", "villagra", "iquique"
print(nombre, apellido, ciudad_origen)

# 6. Usa la funciÃ³n input() para solicitar al usuario su color favorito y almacÃ©nalo en una variable color. Luego, imprime el valor ingresado.
#color_favorito = input("Ingresa tu color favorito")
#print(color_favorito)

# 7. Declara una variable fruit e inicialÃ­zala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit = "manzana"
print(fruit)
fruit = "pera"
print(fruit)

# 8. Convierte un nÃºmero decimal, almacenado en la variable price, a un nÃºmero entero y luego imprÃ­melo.
price = 1.50
price = int(price)
print(price)

# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una direcciÃ³n usando la funciÃ³n len(). Imprime el resultado.
address_len = len("Libertador Bernardo Ohiggins")
print(address_len)

# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurÃ¡ndote de que siempre serÃ¡ un nÃºmero. 
# Luego, cambia su valor a un nÃºmero diferente y verifica el tipo de la variable con type().

phone: int = 123456789
print(type(phone))
phone = 954952753
print(type(phone))
