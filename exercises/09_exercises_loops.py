# 1. Usa un bucle while para imprimir los nÃºmeros del 1 al 10.
numero = 1
while numero <=10:
    print(numero)
    numero+=1

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada nÃºmero.

lista = [10,20,30,40,50]

for numeros in lista:
    print(numeros)

# 3. Escribe un programa que use un bucle while para sumar los nÃºmeros del 1 al 100 e imprime el resultado.
tam = 1
while tam <=100:
    print(tam)
    tam +=1

# 4. Escribe un bucle for que imprima cada carÃ¡cter de la cadena "Python".
cadena = "Python"
for Python in cadena:
    print(Python)

# 5. Usa un bucle while para encontrar el primer nÃºmero divisible por 7 entre 1 y 50.
tam = 1
while tam <=50:
    if tam%7 == 0:
        print("El primer numero divisible por 7 es: {}".format(tam))
        tam = 50
    else:
        tam+=1

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e 
# imprime las claves.
diccionario = {"name": "Brais", "age": 37, "country": "Galicia"}

for imprimir in diccionario.keys():
    print(imprimir)

# 7. Escribe un programa que use un bucle while para imprimir los nÃºmeros pares entre 1 y 20.
numero = 1
while numero <= 20 and numero >=10:
    print(numero)

# 8. Usa un bucle for con la funciÃ³n range() para imprimir los nÃºmeros del 1 al 10 en orden inverso.

# Usar un bucle for con range() para imprimir números del 10 al 1
for i in range(10, 0, -1):  # Comienza en 10, termina en 1 (sin incluir 0), con paso -1
    print(i)

# 9. Escribe un programa que use un bucle for para contar cuÃ¡ntas veces aparece el nÃºmero 30 en la 
# lista[30, 10, 30, 20, 30, 40].
lista = [30, 10, 30, 20, 30, 40]
contador = 0
for imprimir in lista:
    if imprimir == 30:
        contador+=1

print(contador)
# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el 
# nombre "Brais".

nombre = ["mario", "k", "brais"]

for imprimir in nombre:
    if imprimir == "brais":
        print("brais fue encontrado")