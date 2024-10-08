#Defino la clase
class Empleado:
    
    #Método constructor
    def __init__(self, nombre, edad, cargo, experiencia, genero):
        
        #Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        self.experiencia = experiencia
        self.genero = genero

    #Método para mostrar los detalles de cada objeto
    def mostrar_detalles(self):
        print(f"Información del empleado:")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Cargo: {self.cargo}")
        print(f"Experiencia: {self.experiencia}")
        print(f"Género: {self.genero}")
        print("---------------------------------------")

    #Método para hacer que el empleado labore
    def laborar(self):
        
        #Defino el atributo privado laborar solo para el método laborar
        self.laborar = int(input("Quiere que el empleado empiece a laborar? Seleccione una opción \n1. Sí \n2. No \n"))
        
        #Evaluamos la decisión
        if self.laborar == 1:
            print("-----------------------------------")
            print(f"El empleado {self.nombre}, con el cargo {self.cargo} está laborando.")
            print("-----------------------------------")
        
        else:
            print(f"El empleado {self.nombre}, con el cargo {self.cargo} no está laborando.")

#Creamos los objetos a partir de instanciar la clase Empleado
empleado1 = Empleado("Luis Galán", "30 años", "Obrero", "5 años", "Masculino")
empleado2 = Empleado("Andrea Pérez", "25 años", "Secretaria", "2 años", "Femenino")
empleado3 = Empleado("Jose Campo", "50 años", "Director", "10 años", "Masculino")

#Mostrar los detalles de cada objeto
empleado1.mostrar_detalles()
empleado1.laborar() #método que evalúa si el empleado va a laborar
empleado2.mostrar_detalles()
empleado3.mostrar_detalles()