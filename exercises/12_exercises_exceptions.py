# 1. Crea una funciÃ³n que intente dividir dos nÃºmeros proporcionados por el usuario. Usa try-except para capturar cualquier error 
# de divisiÃ³n (por ejemplo, divisiÃ³n por cero).
numberOne = 5
numberTwo = 0

try:
    print(numberOne/numberTwo)
except ValueError as error:
    print(f"Error: {error}")
except ZeroDivisionError as divisionZero: #Si la division es cero arroja este mensaje
    print(f"Error: {divisionZero}")
except:
    print("Error")

# 2. Crea una funciÃ³n que tome una cadena e intente convertirla en un nÃºmero entero. 
# Usa try-except para capturar cualquier error en la conversiÃ³n.

try:
    cadena = "Esto es una cadena"
    cadenaNumerica = int(cadena)
except:
    print("Error en la conversion")    

# 3. Crea una funciÃ³n que abra un archivo, lea su contenido y maneje posibles errores 
# (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones de 
# archivos de forma segura.

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: Fichero no encontrado.")

# 4. Crea una funciÃ³n que realice mÃºltiples operaciones (suma, resta, divisiÃ³n, multiplicaciÃ³n) 
# con dos nÃºmeros. Usa try-except-else-finally para manejar errores y asegurar que se imprima un 
# mensaje final, independientemente de los errores.

numero1 = 5
numero2 = 6

try:
    numero1*numero2
    numero1+numero2
    numero1-numero2
    numero1/numero2
except:
    "Error en la conversion"
else:
    "Problema detectado"
finally:
    "El programa continua"
# 5. Crea una funciÃ³n que le pida al usuario su edad y lance un ValueError si la entrada no es un 
# nÃºmero entero positivo. Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones 
# personalizadas cuando sea necesario.

def edadPositiva(edad):
    try:
        if edad <= 0:
            print("La edad debe contener un valor positivo")
        return edad
    except ValueError as e:
        print(f"Error: {e}")
edadPositiva(1)
# 6. Crea una funciÃ³n que intente acceder a un elemento de una lista por Ã­ndice. 
# Usa try-except para manejar el caso donde el Ã­ndice estÃ© fuera de rango.

def access_element(elemento):
    lista = [1,2,3,4,5,6]
    #tam = len(lista)
    
    try:
        print(lista[elemento])
    except IndexError as error:
        print(f"Error: {error}")
        
# 7. Crea una funciÃ³n que use try-except para manejar mÃºltiples excepciones: ZeroDivisionError, ValueError 
# y TypeError.
def funcion(valor1,valor2):
    try:
        valor1/valor2
    except ZeroDivisionError as zeroError:
        print(f"Error: {zeroError}")
    except ValueError as valError:
        print(f"Error: {valError}")
    except TypeError as typeError:
        print(f"Error: {typeError}")
    except:
        print("Error indefinido")

# 8. Crea una funciÃ³n que simule una transacciÃ³n. Lanza una excepciÃ³n personalizada llamada 
# InsufficientFundsError si el saldo es menor que la cantidad a retirar.
def transaccion(totalCompra):
    saldoTotal = 100000
    try:
        if saldoTotal-totalCompra < 0:
            print("InsufficientFundsError")
    except:
        print("Error")
transaccion(200000)
# 9. Crea una funciÃ³n que intente convertir una lista de cadenas en enteros. 
# Maneja cualquier error que surja cuando una cadena no pueda convertirse.
def convert_list_to_integers(string_list):
    integers = []
    for string in string_list:
        try:
            integers.append(int(string))
        except ValueError:
            print(f"Error: '{string}' no se puede transformar en un entero.")
    return integers
    
# 10. Crea una funciÃ³n que calcule la raÃ­z cuadrada de un nÃºmero. 
# Lanza un ValueError si el nÃºmero es negativo.

def calculate_square_root(number):
    try:
        if number < 0:
            raise ValueError(
                "No se puede calcular la raÃ­z cuadrada de un nÃºmero negativo.")
        return number ** 0.5
    except ValueError as e:
        print(f"Error: {e}")
        
calculate_square_root(-1)