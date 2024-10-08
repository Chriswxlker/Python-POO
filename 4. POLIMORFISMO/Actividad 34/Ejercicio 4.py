# Clase Guitarra
class Guitarra:
    def __init__(self, cuerdas, tipo, marca):
        self.cuerdas = cuerdas
        self.tipo = tipo
        self.marca = marca

    def tocar(self):
        print(f"Esta es una guitarra de {self.cuerdas} cuerdas, del tipo {self.tipo}.")
        print(f"Marca: {self.marca}. Es un instrumento de cuerda frotada o pulsada.")

# Clase Piano
class Piano:
    def __init__(self, teclas, tipo, marca):
        self.teclas = teclas
        self.tipo = tipo
        self.marca = marca

    def tocar(self):
        print(f"Este es un piano con {self.teclas} teclas, del tipo {self.tipo}.")
        print(f"Marca: {self.marca}. Es un instrumento de cuerda percutida.")

# Clase Trompeta
class Trompeta:
    def __init__(self, material, tipo, marca):
        self.material = material
        self.tipo = tipo
        self.marca = marca

    def tocar(self):
        print(f"Esta es una trompeta de {self.material}, del tipo {self.tipo}.")
        print(f"Marca: {self.marca}. Es un instrumento de viento metal.")

# Función para tocar el instrumento
def tocar_instrumento(instrumento):
    instrumento.tocar()

# Instancias de cada clase
guitarra = Guitarra(6, "Eléctrica", "Fender")
piano = Piano(88, "Acústico", "Yamaha")
trompeta = Trompeta("latón", "Bb", "Bach")

# Llamada al método tocar()
tocar_instrumento(guitarra)
tocar_instrumento(piano)
tocar_instrumento(trompeta)
