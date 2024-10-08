#Defino la clase
class Carro:
    
    #Método constructor
    def __init__(self, marca, modelo, potencia, color, nacionalidad):
        
        #Defino los atributos de instancia de la clase
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.color = color
        self.nacionalidad = nacionalidad

    #Método para mostrar los detalles de cada objeto
    def mostrar_detalles(self):
        print(f"Información del Carro:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Potencia: {self.potencia}")
        print(f"Color: {self.color}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print("---------------------------------------")

    #Método para hacer que el auto encienda
    def encender(self):
        
        #Defino el atributo privado encender solo para el método encender
        self.encender = int(input("Quiere encender el carro? Seleccione una opción \n1. Sí \n2. No \n"))
        
        #Evaluamos la decisión
        if self.encender == 1:
            print("-----------------------------------")
            print(f"El carro {self.marca} {self.modelo} está encendido.")
            print("-----------------------------------")
        
        else:
            print(f"El carro {self.marca} {self.modelo} está apagado.")

#Creamos los objetos a partir de instanciar la clase Carro
carro1 = Carro("Toyota", "Prado", "300hp", "Gris", "Japonés")
carro2 = Carro("Ford", "f150", "260hp", "Rojo", "Americano")
carro3 = Carro("Lamborghinni", "Huracán", "700hp", "Anaranjado", "Italiano")

#Mostrar los detalles de cada objeto
carro1.mostrar_detalles()
carro1.encender() #método que evalúa si el carro va a encender
carro2.mostrar_detalles()
carro3.mostrar_detalles()