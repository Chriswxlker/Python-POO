#Defino la clase
class Dispositivo:
    
    #Método constructor
    def __init__(self, marca, modelo, año):
        
        #Defino los atributos de instancia de la clase
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.capacidad = input("Cual es la capacidad de la batería (en mAh)?: ")

    #Método para mostrar los detalles de cada objeto
    def mostrar_detalles(self):
        print(f"----------------------------------------------")
        print(f"Detalles iniciales del producto:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Capacidad de la batería: {self.capacidad} mAh")
        print(f"----------------------------------------------")

    def detalles_actualizados(self):
        print(f"-----------------------------------------------")
        print(f"Detalles actualizados del producto:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Capacidad de la batería: {self.capacidad} mAh")
        print(f"Sistema operativo: {self.so}")
        print(f"Tipo de conectividad: {self.conectividad}")
        print(f"-----------------------------------------------")
        
    #Método para encender el dispositivo
    def encender(self):
        
        self.encender = int(input("Quiere encender el dispositivo? Seleccione una opción \n1. Sí \n2. No \n"))
        
        #Evaluamos la decisión
        if self.encender == 1:
            print("-------------------------------------------------------------")
            print(f"Acción de encender el dispositivo:")
            print(f"Marca: {self.marca}")
            print(f"Modelo: {self.modelo}")
            print(f"Año: {self.año}")
            print(f"Capacidad de la batería: {self.capacidad} mAh")
            print(f"El dispositivo {self.marca} {self.modelo} está encendido.")
            print("------------------------------------------------------------")
        
        else:
            print(f"El dispositivo {self.marca} {self.modelo} está apagado.")


#Subclase
class Smartphone(Dispositivo):
    
    #Método constructor
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año) #super clase heredada
        self.so = input("Qué sistema operativo tiene el celular?: \n-iOS \n-Android \n")
        self.conectividad = input("Cual es el tipo de conectividad?: \n-4G \n-5G \n")

#Instanciando la sub clase
objeto_deispositivo = Smartphone("Samsung", "S21 Ultra", "2022")
objeto_deispositivo.mostrar_detalles()
objeto_deispositivo.encender()
objeto_deispositivo.detalles_actualizados()