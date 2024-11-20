# 1. Crea un set con los nÃºmeros del 1 al 5 e imprÃ­melo.
mySet = {1,2,3,4,5}

# 2. AÃ±ade el nÃºmero 6 al set {1, 2, 3, 4, 5} e imprÃ­melo.
#mySet.add(6)
#print(mySet)

# 3. Intenta aÃ±adir el nÃºmero 5 al set {1, 2, 3, 4, 5} nuevamente. Â¿QuÃ© sucede?

#my_set = {1, 2, 3, 4, 5}
#my_set.add(5)

# 4. Verifica si el nÃºmero 3 estÃ¡ en el set {1, 2, 3, 4, 5} e imprime el resultado.
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)

# 5. Elimina el nÃºmero 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
set = {1,2,3,4,5}
set = list(set)
del set[3]
set = tuple(set)
print(set)

# 6. Usa el mÃ©todo clear() para vaciar un set y luego imprime su longitud.
set = {1,2,3}
set.clear()
print(len(set))

# 7. Convierte el set {"manzana", "naranja", "plÃ¡tano"} en una lista e imprime el primer elemento de la lista.
mySet = {"manzana", "naranja", "platano"}
mySet = list(mySet)
print(mySet[0])

# 8. Realiza la uniÃ³n de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.
set1 = {1,2,3}
set2 = {4,5,6}
my_new_set = set1.union(set2)

print(my_new_set)

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1.difference(set2))

# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.

my_set = {}

del my_set

#print(my_set)