# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.

diccionario = {}

diccionario = {
    "name" : "Mario",
    "age" : 33,
    "country" : "Iquique"
}
print(diccionario)

# 2. Accede al valor de la clave name en el diccionario.
print(diccionario["name"])

# 3. AÃ±ade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
diccionario.setdefault("programador", "JavaScript")
print(diccionario)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
diccionario["age"] = 38
print(diccionario)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
del diccionario["country"]
print(diccionario)

# 6. Crea un diccionario donde las claves sean nÃºmeros del 1 al 5 y los valores sean sus cuadrados 
# (ejemplo: 1: 1, 2: 4, ...).
diccionario2 = {
    "1" : "1",
    "2" : "4",
    "3" : "9",
    "4" : "16",
    "5" : "25"
}

# 7. Verifica si la clave age estÃ¡ presente en el diccionario 
# {"name": "Brais", "age": 37, "country": "Galicia"}.
diccionarioBrais = {
    "name": "Brais", 
    "age": 37, 
    "country": "Galicia"
    }

print("here")
print(diccionarioBrais.values())
print("age" in diccionarioBrais)

# 8. Imprime solo las claves del diccionario.
print(diccionarioBrais.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
diccionarioBrais = list(diccionarioBrais)
print(diccionarioBrais)

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), 
# asignando a todas las claves el valor "Desconocido".

# Lista de claves
listaKeys = ["name", "age", "job"]

# Crear un diccionario usando fromkeys() con valor "Desconocido"
diccionario = dict.fromkeys(listaKeys, "Desconocido")

# Mostrar el resultado
print(diccionario)
