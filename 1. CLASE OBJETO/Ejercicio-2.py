#Defino la clase
class Animal:
    
    #Método constructor
    def __init__(self, nombre, especie, dieta, habitad, caracter):
        
        #Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.especie = especie
        self.dieta = dieta
        self.habitad = habitad
        self.caracter = caracter

    #Método para mostrar los detalles de cada objeto
    def mostrar_detalles(self):
        print(f"Información del animal:")
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Dieta: {self.dieta}")
        print(f"Habitad: {self.habitad}")
        print(f"Carácter: {self.caracter}")
        print("---------------------------------------")

    #Método para hacer que el animal haga un sonido
    def sonar(self):
        
        #Defino el atributo privado sonido solo para el método sonar
        self.sonido = int(input("Quiere que el animal reproduzca un sonido? Seleccione una opción \n1. Sí \n2. No \n"))
        
        #Evaluamos la decisión
        if self.sonido == 1:
            print("-----------------------------------")
            print(f"El animal {self.nombre} está haciendo un sonido.")
            print("-----------------------------------")
        
        else:
            print(f"El animal {self.nombre} no está haciendo ningún sonido.")

#Creamos los objetos a partir de instanciar la clase Animal
animal1 = Animal("León", "Felino", "Carnívoro", "Sabana", "Salvaje")

animal2 = Animal("Ballena", "Cetáceos", "Herbívoro", "Acuático", "Salvaje")

animal3 = Animal("Pájaro", "Aves", "Herbívoro", "Aéreo", "Salvaje")

#Mostrar los detalles de cada objeto
animal1.mostrar_detalles()
animal1.sonar() #método que evalúa si el animal va a reproducir un sonido
animal2.mostrar_detalles()
animal3.mostrar_detalles()