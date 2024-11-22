#Functions
#Las funciones son declaradas con def... no sirve declarar 
# con function como en otros lenguajes

#definir una funcion

def my_function():
    print("Esto es una funcion")
    
my_function()

def sum_two_values(first_number, second_number):
    
    print("La suma es: {}".format(first_number+second_number))
    
sum_two_values(2,2)

def sum_two_values_with_return(firt_value, second_value):
    return firt_value + second_value

my_result = sum_two_values_with_return(10,5)
print("prueba")
print(my_result)
my_result = sum_two_values(10,5)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")
    
print_name(surname="Mario", name="Villagra")

def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")
    
print_name_with_default("Mario", "Villagra", "Mariioote")

def print_text(*text):
    print(text)
    
print_text("hola", "como estas", "??")
print_text("hola")