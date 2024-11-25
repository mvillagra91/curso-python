# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un mÃ©todo "make_sound" que imprima 
# un sonido genÃ©rico.

class Animal:
    def __init__(self, species):
        self.especie = species
        
    def make_sound(self):
        print("Sonido animal generico")
        
# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacÃ©nala en una propiedad 
# pÃºblica. AÃ±ade el mÃ©todo "make_sound" que imprima un sonido dependiendo de la especie.

class Animal:
    def __init__(self, species):
        self.species = species
        
    def make_sound(self):
        if self.species == "dog":
            print("Guaf")
        elif self.species == "cat":
            print("Miau")
        else:
            print("Sonido de especie no asignado")

# 3. Crea una clase llamada "Car" con las propiedades pÃºblicas "brand" y "model". AdemÃ¡s, debe 
# tener una propiedad privada "_speed" que inicialmente serÃ¡ 0.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._speed = 0

# 4. AÃ±ade a la clase "Car" un mÃ©todo llamado "accelerate" que aumente la velocidad en 10 unidades. 
# AÃ±ade tambiÃ©n un mÃ©todo "brake" que reduzca la velocidad en 10 unidades. AsegÃºrate de que la velocidad 
# no sea negativa.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._speed = 0
    
    def accelerate(self):
        self.accelerate +=10
        
    def brake(self):
        self._speed = max(0, self._speed - 10)
    
# 5. Crea una clase "Book" que tenga propiedades como "title" (pÃºblico) y "author" (privado). 
# AÃ±ade un mÃ©todo para obtener el autor y otro para cambiar el tÃ­tulo del libro.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author

    def get_author(self):
        return self.__author
    
    def update_title(self, new_title):
        self.title = new_title
# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. 
# AÃ±ade un mÃ©todo para calcular y devolver la nota media del estudiante.

class Estudiante:
    def __init__(self, nombre, apellido, notas):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = notas
    
    def calcular(self):
        return sum(self.notas)/len(self.notas)

# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". 
# AÃ±ade mÃ©todos para depositar y retirar dinero, asegurÃ¡ndote de que no se pueda retirar mÃ¡s 
# de lo que hay en la cuenta.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def retirar(self, total_retiro):
        if(total_retiro<=self.balance):
            self.balance = self.balance - total_retiro
            print(f"Se han retirado {total_retiro}. Su balance actual es de: {self.balance}")
        else:
            print(f"Retiro fallido. Usted cuenta con un balance de: {self.balance}")
            
    def deposito(self, total_deposito):
        self.balance += total_deposito
# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". 
# AÃ±ade un mÃ©todo que calcule la distancia entre dos puntos.
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def calculate_distance(self, other_point):
        distance_x = abs(self.x - other_point.x)
        distance_y = abs(self.y - other_point.y)
        return (distance_x ** 2 + distance_y ** 2) ** 0.5
        

# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y 
# "hours_worked". AÃ±ade un mÃ©todo que calcule el pago total basado en las horas trabajadas y el 
# salario por hora.
class Employee:
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        
    def pago_total(self):
        return self.hourly_wage*self.hours_worked

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). 
# AÃ±ade un mÃ©todo para agregar un producto al inventario y otro para mostrar todos los productos disponibles.
class Store:
    def __init__(self):
        self.inventory = []
    
    def agregar_producto(self, producto):
        self.inventory.append(producto)
        
    def mostrar_productos(self):
        for producto in self.inventory:
            print(producto)