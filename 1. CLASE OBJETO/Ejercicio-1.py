#Defino la clase
class Celular:
    
    #Método constructor
    def __init__(self, marca, modelo, almacenamiento, ram, camara):
        
        #Defino los atributos de instancia de la clase
        self.marca = marca
        self.modelo = modelo
        self.almacenamiento = almacenamiento
        self.ram = ram
        self.camara = camara

    #Método para mostrar los detalles de cada objeto
    def mostrar_detalles(self):
        print(f"Información del celular:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Almacenamiento: {self.almacenamiento}")
        print(f"Memoria RAM: {self.ram}")
        print(f"Megapixeles de la cámara: {self.camara}")
        print("---------------------------------------")

    #Método para encender el celular
    def encender(self):
        
        #Defino el atributo privado energía solo para el método encender
        self.energia = int(input("Digite el valor de la carga: "))
        
        #Evaluamos si tiene carga el celular
        if self.energia > 0:
            print("-----------------------------------")
            print(f"El celular {self.modelo} se puede encender.")
            print(f"La carga del celular es de {self.energia}%")
            print("-----------------------------------")
        
        else:
            print(f"El celular {self.modelo} no se puede encender")

#Creamos los objetos a partir de instanciar la clase Celular
celular1 = Celular("Apple", "iPhone 8 Plus", "64gb", "4gb", "12mp")

celular2 = Celular("Xiaomi", "Redmi Note 8 Pro", "128gb", "6gb", "108mp")

celular3 = Celular("Samsung", "A21", "256gb", "8gb", "200mp")

#Mostrar los detalles de cada objeto
celular1.mostrar_detalles()
celular1.encender() #método que evalúa el encendido del celular
celular2.mostrar_detalles()
celular3.mostrar_detalles()