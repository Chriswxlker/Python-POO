from abc import ABC, abstractmethod

class TareaEmpleado(ABC):
    
    @abstractmethod
    def realizar_tarea(self):
        pass

class Ingeniero(TareaEmpleado):
    
    def __init__(self, especialidad):
        self.especialidad = especialidad
    
    def realizar_tarea(self):
        return f"El ingeniero especializado en {self.especialidad} está diseñando y construyendo estructuras."

class Doctor(TareaEmpleado):
    
    def __init__(self, especialidad):
        self.especialidad = especialidad
    
    
    def realizar_tarea(self):
        return f"El doctor especializado en {self.especialidad} está diagnosticando y tratando a los pacientes."


ingeniero = Ingeniero("Ingeniería Civil")
print(ingeniero.realizar_tarea())

doctor = Doctor("Cardiología")
print(doctor.realizar_tarea())