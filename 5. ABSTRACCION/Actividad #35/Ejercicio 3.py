from abc import ABC, abstractmethod

# Clase abstracta TareaEmpleado
class TareaEmpleado(ABC):
    
    # Método abstracto que debe ser implementado por las subclases
    @abstractmethod
    def realizar_tarea(self):
        pass

# Clase Ingeniero que hereda de TareaEmpleado
class Ingeniero(TareaEmpleado):
    
    def __init__(self, especialidad):
        self.especialidad = especialidad
    
    # Implementación del método realizar_tarea específico para Ingeniero
    def realizar_tarea(self):
        return f"El ingeniero especializado en {self.especialidad} está diseñando y construyendo estructuras."

# Clase Doctor que hereda de TareaEmpleado
class Doctor(TareaEmpleado):
    
    def __init__(self, especialidad):
        self.especialidad = especialidad
    
    # Implementación del método realizar_tarea específico para Doctor
    def realizar_tarea(self):
        return f"El doctor especializado en {self.especialidad} está diagnosticando y tratando a los pacientes."

# Ejemplos de uso

# Crear un Ingeniero con especialidad en 'Civil'
ingeniero = Ingeniero("Ingeniería Civil")
print(ingeniero.realizar_tarea())  # Output: El ingeniero especializado en Ingeniería Civil está diseñando y construyendo estructuras.

# Crear un Doctor con especialidad en 'Cardiología'
doctor = Doctor("Cardiología")
print(doctor.realizar_tarea())  # Output: El doctor especializado en Cardiología está diagnosticando y tratando a los pacientes.
