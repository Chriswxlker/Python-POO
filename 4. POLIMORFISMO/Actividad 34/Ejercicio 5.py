# Clase Medico
class Medico:
    def __init__(self, nombre, especialidad, experiencia):
        self.nombre = nombre
        self.especialidad = especialidad
        self.experiencia = experiencia

    def trabajar(self):
        print("-----------------------------------------------")
        print(f"Nombre del médico: {self.nombre}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Experiencia: {self.experiencia} años")
        print("-----------------------------------------------")

# Clase Ingeniero
class Ingeniero:
    def __init__(self, nombre, especialidad, experiencia):
        self.nombre = nombre
        self.especialidad = especialidad
        self.experiencia = experiencia

    def trabajar(self):
        print("-----------------------------------------------")
        print(f"Nombre del ingeniero: {self.nombre}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Experiencia: {self.experiencia} años")
        print("-----------------------------------------------")

# Clase Docente
class Docente:
    def __init__(self, nombre, area, experiencia):
        self.nombre = nombre
        self.area = area
        self.experiencia = experiencia

    def trabajar(self):
        print("-----------------------------------------------")
        print(f"Nombre del docente: {self.nombre}")
        print(f"Área: {self.area}")
        print(f"Experiencia: {self.experiencia} años")
        print("-----------------------------------------------")

# Función trabajar
def trabajar_profesion(profesiones):
    profesiones.trabajar()

# Instancias de cada clase
medico = Medico("Juan Aragon", "Neurólogo", 19)
ingeniero = Ingeniero("David Visbal", "Ingeniero de sistemas", 8)
docente = Docente("Carlos Salcedo", "Química", 35)

# Llamada al método trabajar()
trabajar_profesion(medico)
trabajar_profesion(ingeniero)
trabajar_profesion(docente)
