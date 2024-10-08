#Defino la clase
class Instrumento:
    
    #Método constructor
    def __init__(self, tipo, marca, material):
        
        #Defino los atributos de instancia de la clase
        self.tipo = tipo
        self.marca = marca
        self.material = material
        self.precio = int(input("Cual es el precio del instrumento?: $"))

    #Método para mostrar los detalles de cada objeto
    def mostrar_detalles(self):
        print(f"--------------------------------------")
        print(f"Detalles del producto:")
        print(f"Tipo de instrumento: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Material: {self.material}")
        print(f"Precio del instrumento: ${self.precio}")
        print(f"--------------------------------------")

    def tocar(self):
        
        tocar = int(input("Desea tocar la guitarra con los a    cordes proporcionados? \n1.Sí \n2.No \n"))
        if tocar == 1:
            print(f"--------------------------------------")
            print(f"Detalles del producto:")
            print(f"Tipo de instrumento: {self.tipo}")
            print(f"Marca: {self.marca}")
            print(f"Material: {self.material}")
            print(f"Precio del instrumento: ${self.precio}")
            print(f"Número de cuerdas: {self.n_cuerdas}")
            print(f"Acordes: {self.acordes}")
            print(f"La guitarra está tocando los acordes '{self.acordes}' proporcionados en la petición.")
            print(f"--------------------------------------")
            
        else:
            print(f"La guitarra no se está tocando en este momento...")

#Subclase
class Guitarra(Instrumento):
    
    #Método constructor
    def __init__(self, tipo, marca, material):
        super().__init__(tipo, marca, material) #super clase heredada
        self.n_cuerdas = input("Cual es el número de cuerdas de la guitarra?: ")
        self.acordes = input("Qué acordes básicos conoce?: ")

#Instanciando la sub clase refrigerador
objeto_instrumento = Guitarra("Guitarra", "Yamaha", "Madera")
objeto_instrumento.mostrar_detalles()
objeto_instrumento.tocar()