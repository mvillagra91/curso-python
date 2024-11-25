class Car:
    def __init__(self, marca, modelo, year):
        self.marca = marca
        self.modelo = modelo
        self.year = year
        
    def display_info(self):
        print(f"Marca: {self.marca} Modelo: {self.modelo} Año: {self.year}")