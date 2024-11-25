#Clases

class MyEmptyPerson:
    pass
    
print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.fullname = f"{name} {surname} ({alias})"
        self.__name = name #propiedad privada
        
    def walk(self):
        print(f"{self.fullname} Está caminando")
    
    def get_name(self):
        return self.__name

my_person = Person("Mario", "Villagra", "Mariiotte")
print(my_person.fullname)
my_person.walk()

print(my_person.get_name())