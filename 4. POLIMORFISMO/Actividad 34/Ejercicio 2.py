# Clase base Vehiculo
class Vehiculo:
    def mostrar_detalles(self):
        pass

# Clase Carro
class Carro(Vehiculo):
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_detalles(self):
        print(f"Automóvil marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Del año: {self.año}")

# Clase Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.cilindrada = cilindrada

    def mostrar_detalles(self):
        print(f"Motocicleta marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Cilindrada: {self.cilindrada} cc")

# Clase Bicicleta
class Bicicleta(Vehiculo):
    def __init__(self, marca, material, tipo):
        self.marca = marca
        self.material = material
        self.tipo = tipo

    def mostrar_detalles(self):
        print(f"Bicicleta marca: {self.marca}")
        print(f"Material: {self.material}")
        print(f"Tipo: {self.tipo}")

# Función para mostrar los detalles del vehículo
def mostrar_descripcion(vehiculo):
    vehiculo.mostrar_detalles()

# Instancias de cada clase
carro = Carro("Ford", "Mustang", "2015")
moto = Moto("Ducati", "Panigale", "2020", "1299")
bicicleta = Bicicleta("Shimano", "aluminio", "Carreras")

# Llamada al método mostrar_detalles() usando polimorfismo
mostrar_descripcion(carro)
mostrar_descripcion(moto)
mostrar_descripcion(bicicleta)
