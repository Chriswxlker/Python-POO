#Defino la clase
class Reloj:
    
    #Método constructor
    def __init__(self, marca, tipo_reloj, material):
        
        #Defino los atributos de instancia de la clase
        self.marca = marca
        self.tipo_reloj = tipo_reloj
        self.material = material
        self.precio = int(input("Cual es el precio del reloj?: "))

    #Método para mostrar los detalles de cada objeto
    def mostrar_detalles(self):
        print(f"--------------------------------------")
        print(f"Detalles del producto:")
        print(f"Marca: {self.marca}")
        print(f"Tipo del reloj: {self.tipo_reloj}")
        print(f"Material de la caja: ${self.material}")
        print(f"Precio: ${self.precio}")
        print(f"--------------------------------------")

    def encender(self):
        
        self.encender = int(input("Quiere encender el reloj inteligente? Seleccione una opción \n1. Sí \n2. No \n"))
        
        #Evaluamos la decisión
        if self.encender == 1:
            print("-------------------------------------------------------------")
            print("EL RELOJ INTELIGENTE ESTÁ ENCENDIDO")
            print(f"Detalles del producto:")
            print(f"Marca: {self.marca}")
            print(f"Tipo del reloj: {self.tipo_reloj}")
            print(f"Material de la caja: {self.material}")
            print(f"Precio: ${self.precio}")
            print(f"Tipo de pantalla: {self.tipo_pantalla}")
            print(f"Sistema operativo del reloj: {self.so}")
            print("------------------------------------------------------------")
        
        else:
            print(f"El reloj inteligente {self.marca} {self.tipo_reloj} está apagado.")

#Subclase
class RelojInteligente(Reloj):
    
    #Método constructor
    def __init__(self, marca, tipo_reloj, material, tipo_pantalla):
        super().__init__(marca, tipo_reloj, material) #super clase heredada
        self.tipo_pantalla = tipo_pantalla
        self.so = input("Cual es el sistema operativo del reloj?: \n-Wear os? \n-Otro? \n")

#Instanciando la sub clase refrigerador
objeto_reloj = RelojInteligente("Samsung", "Smart", "Aluminio", "OLED")
objeto_reloj.mostrar_detalles()
objeto_reloj.encender()