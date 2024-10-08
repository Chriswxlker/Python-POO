class Personas:
    # Método constructor
    def __init__(self, nombres, apellidos, identidad, fechanacimiento, sexo):
        self.__nombres = nombres  # privado
        self.__apellidos = apellidos  # privado
        self.__identidad = identidad  # privado
        self.fechanacimiento = fechanacimiento  # público
        self.sexo = sexo  # público

    # Método getter
    def obtener_nombres(self):
        return self.__nombres

    # Método getter
    def obtener_apellidos(self):
        return self.__apellidos

    # Método getter
    def obtener_identidad(self):
        return self.__identidad

    # Método setter
    def establecer_nombres(self, nuevo_nombres):
        self.__nombres = nuevo_nombres

    # Método setter
    def establecer_apellidos(self, nuevo_apellidos):
        self.__apellidos = nuevo_apellidos

    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print(f"\nNombres: {self.__nombres}")
        print(f"Apellidos: {self.__apellidos}")
        print(f"N° Identidad: {self.__identidad}")
        print(f"Fecha de nacimiento: {self.fechanacimiento}")
        print(f"Sexo: {self.sexo}")

# Objeto
persona = Personas("Jorge", "Rojas", 1102345678, "14/09/2000", "M")

# Imprimir atributos públicos y privados
persona.mostrar_detalles()

print("---------------------------------------------------")

# Imprimir el atributo encapsulado modificando su acceso con getter y setter
persona.establecer_nombres("Carlos")  # setter
print(f"Nombres: {persona.obtener_nombres()}")  # getter
persona.establecer_apellidos("Perez")  # setter
print(f"Apellidos: {persona.obtener_apellidos()}")  # getter
print(f"N° de Identidad: {persona.obtener_identidad()}")  # getter
print(f"Fecha nacimiento: {persona.fechanacimiento}")  # público
print(f"Sexo: {persona.sexo}")  # público