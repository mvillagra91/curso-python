# 1. Escribe un programa que verifique si un nÃºmero es positivo, negativo o cero.
numero = 1
if numero<0:
   print("El numero es negativo")
else:
    print("El numero es positivo")



# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 aÃ±os o mÃ¡s) o menor de edad.
#edad = input("Ingresa tu edad")
edad = 17

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# 3. Escribe un programa que verifique si una cadena de texto estÃ¡ vacÃ­a y muestre un mensaje en consecuencia.
cadenaTexto = ""

if cadenaTexto == "":
    print("Cadena de texto vacia")

# 4. Crea un programa que solicite dos nÃºmeros al usuario y compare cuÃ¡l es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
n1 = 1
n2 = 1

if n1 > n2:
    print("{} es mayor que {}".format(n1,n2))
elif n1<n2:
    print("{} es mayor que {}".format(n2,n1))
elif n1==n2:
    print("Las variables son iguales")
    
# 5. Escribe un programa que verifique si un nÃºmero es divisible por 3 y por 5 al mismo tiempo.
numero = 30

if numero%3 == 0 and numero%5 ==0:
    print("El numero es divisible por 3 y 5")

# 6. Solicita al usuario que ingrese un nÃºmero y verifica si es par o impar.
numero = 1

if numero %2 == 0:
    print("Es par")
else:
    print("Es impar")

# 7. Escribe un programa que determine si una persona puede votar en funciÃ³n de su edad(mayor o igual a 18). Si tiene 16 o 17 aÃ±os, indica que puede votar con permiso especial.
edad = 18

if edad >= 18:
    print("Puedes votar")
elif edad == 16 or edad == 17:
    print("Puedes votar pero con permiso especial")
else:
    print("No puedes votar eres menor de edad")

# 8. Crea un programa que solicite una contraseÃ±a al usuario y verifique si coincide con una contraseÃ±a predefinida. 
# Si no coincide, muestra un mensaje de error.
password = 1234

if password == 1234:
    print("Ingreso exitoso..")
else:
    print("Error. Contraseña invalida.")

# 9. Escribe un programa que determine si un nÃºmero estÃ¡ entre 10 y 20 (ambos incluidos).
numero = 15

if numero >= 10 and numero <=20:
    print("El numero esta entre 10 y 20")
else:
    print("El numero no se encuentra en el rango")

# 10. Escribe un programa que simule un semÃ¡foro: solicita al usuario que ingrese 
# un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, 
# estar alerta o avanzar.
color = "rojo"

if color == "rojo":
    print("Detenerse")
elif color == "amarillo":
    print("Debes estar alerta")
elif color == "verde":
    print("Avanza")
else:
    print("Error. Semafoto apagado")