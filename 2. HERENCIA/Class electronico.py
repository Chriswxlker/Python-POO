#Defino la clase
class Electronico:
    
    #Método constructor
    def __init__(self, marca, modelo, tipo_procesador):
        
        #Defino los atributos de instancia de la clase
        self.marca = marca
        self.modelo = modelo
        self.tipo_procesador = tipo_procesador
        self.ram = int(input("Cual es la cantidad de memoria RAM?: "))

    #Método para mostrar los detalles de cada objeto
    def mostrar_detalles(self):
        print(f"--------------------------------------")
        print(f"Detalles del producto:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Tipo del procesador: ${self.tipo_procesador}")
        print(f"Cantidad de memoria RAM: {self.ram}gb")
        print(f"--------------------------------------")

    def encender(self):
        
        self.encender = int(input("Quiere encender el la laptop? Seleccione una opción \n1. Sí \n2. No \n"))
        
        #Evaluamos la decisión
        if self.encender == 1:
            print("-------------------------------------------------------------")
            print("LA LAPTOP ESTÁ ENCENDIDA")
            print(f"Detalles del producto:")
            print(f"Marca: {self.marca}")
            print(f"Modelo: {self.modelo}")
            print(f"Tipo del procesador: {self.tipo_procesador}")
            print(f"Cantidad de memoria RAM: {self.ram}gb")
            print(f"Tipo de disco duro: {self.tipo_disco_duro}")
            print(f"Duración de la batería en horas: {self.duracion_bateria}")
            print("------------------------------------------------------------")
        
        else:
            print(f"La laptop {self.marca} {self.modelo} está apagada.")

#Subclase
class Laptop(Electronico):
    
    #Método constructor
    def __init__(self, marca, modelo, tipo_procesador, tipo_disco_duro):
        super().__init__(marca, modelo, tipo_procesador) #super clase heredada
        self.tipo_disco_duro = tipo_disco_duro
        self.duracion_bateria = input("Cual es la duración de la batería en horas?: ")

#Instanciando la sub clase refrigerador
objeto_electronico = Laptop("ASUS", "Notebook", "Intel i7", "Sólido")
objeto_electronico.mostrar_detalles()
objeto_electronico.encender()