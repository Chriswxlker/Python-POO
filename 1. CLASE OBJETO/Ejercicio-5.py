#Defino la clase
class Figura:
    
    #Método constructor
    def __init__(self, nombre, lados, alto, ancho, color):
        
        #Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.lados = lados
        self.alto = alto
        self.ancho = ancho
        self.color = color

    #Método para mostrar los detalles de cada objeto
    def mostrar_detalles(self):
        print(f"Información de la figura geométrica:")
        print(f"Nombre: {self.nombre}")
        print(f"Lados: {self.lados}")
        print(f"Alto: {self.alto}")
        print(f"Ancho: {self.ancho}")
        print(f"Color: {self.color}")
        print("---------------------------------------")

    #Método para calcular el area de la figura
    def calcular_area(self):
        
        #Defino el atributo privado laborar solo para el método laborar
        self.calcular_area = int(input("Desea calcular el área de la figura? Seleccione una opción \n1. Sí \n2. No \n"))
        
        #Evaluamos la decisión
        if self.calcular_area == 1:
            print("---------------------------------------")
            base = 10
            altura = 10
            
            area = (base * altura) / 2
            
            print(f"El area de la figura geométrica es {area}")
            print("---------------------------------------")
        
        else:
            print("No se calculará ningún area.")

#Creamos los objetos a partir de instanciar la clase Figura
figura1 = Figura("Triangulo", "3", "10 cm", "10 cm", "Azul")
figura2 = Figura("Círculo", "0", "5 cm", "5 cm", "Rojo")
figura3 = Figura("Cuadrado", "4", "7 cm", "7 cm", "Verde")

#Mostrar los detalles de cada objeto
figura1.mostrar_detalles()
figura1.calcular_area() #método que evalúa si se va a calcular el área
figura2.mostrar_detalles()
figura3.mostrar_detalles()