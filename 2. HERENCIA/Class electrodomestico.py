#Defino la clase
class Electrodomestico:
    
    #Método constructor
    def __init__(self, marca, color, capacidad):
        
        #Defino los atributos de instancia de la clase
        self.marca = marca
        self.color = color
        self.capacidad = capacidad
        self.consumo = input("Cual es el consumo eléctrico en kilowatts del electrodoméstico?: ")

    #Método para mostrar los detalles de cada objeto
    def mostrar_detalles(self):
        print(f"--------------------------------------")
        print(f"Detalles del producto:")
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Capacidad (en litros): {self.capacidad}")
        print(f"Consumo en kwh: {self.consumo}")
        print(f"--------------------------------------")

    def detalles_actualizados(self):
        print(f"--------------------------------------")
        print(f"Detalles actualizados del producto:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.color}")
        print(f"Capacidad (en litros): {self.capacidad}")
        print(f"Consumo en kwh: {self.consumo}")
        print(f"Tipo de refrigerador: {self.tipo}")
        print(f"Temperatura inicial: {self.temperatura}")
        print(f"Nueva temperatura: {self.nueva_temperatura}")
        print(f"--------------------------------------")

#Subclase
class Refrigerador(Electrodomestico):
    
    #Método constructor
    def __init__(self, marca, color, capacidad):
        super().__init__(marca, color, capacidad) #super clase heredada
        self.tipo = input("Que tipo de refrigerador es?: \n-Frost \n-No Frost \n")
        self.temperatura = int(input("Cual es la temperatura inicial? (en °C): "))
        self.nueva_temperatura = int(input("Cual es la nueva temperatura?: "))

#Instanciando la sub clase refrigerador
objeto_electrodomestico = Refrigerador("LG", "Gris", "500L")
objeto_electrodomestico.mostrar_detalles()
objeto_electrodomestico.detalles_actualizados()