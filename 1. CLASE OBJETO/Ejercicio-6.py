#Defino la clase
class Moto:
    
    #Método constructor
    def __init__(self, marca, modelo, potencia, color, peso):
        
        #Defino los atributos de instancia de la clase
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.color = color
        self.peso = peso

    #Método para mostrar los detalles de cada objeto
    def mostrar_detalles(self):
        print(f"Información de la moto:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Potencia: {self.potencia}")
        print(f"Color: {self.color}")
        print(f"Peso: {self.peso}")
        print("---------------------------------------")

    #Método para hacer que el auto encienda
    def encender(self):
        
        #Defino el atributo privado encender solo para el método encender
        self.encender = int(input("Quiere encender la moto? Seleccione una opción \n1. Sí \n2. No \n"))
        
        #Evaluamos la decisión
        if self.encender == 1:
            print("-----------------------------------")
            print(f"La moto {self.marca} {self.modelo} está encendida.")
            print("-----------------------------------")
        
        else:
            print(f"La moto {self.marca} {self.modelo} está apagada.")

#Creamos los objetos a partir de instanciar la clase Carro
moto1 = Moto("Yamaha", "Bwis", "10hp", "Azul", "120kg")
moto2 = Moto("Yamaha", "V80", "12hp", "Rojo", "90kg")
moto3 = Moto("Kawasaki", "ZX10R", "180hp", "Verde", "180kg")

#Mostrar los detalles de cada objeto
moto1.mostrar_detalles()
moto1.encender() #método que evalúa si la moto va a encender
moto2.mostrar_detalles()
moto3.mostrar_detalles()