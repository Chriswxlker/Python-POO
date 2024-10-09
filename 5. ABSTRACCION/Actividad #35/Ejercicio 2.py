#Crea una clase abstracta Empleado con un método abstracto calcular_salario(). Luego, crea dos clases concretas EmpleadoTiempoCompleto y EmpleadoPorHoras que implementen calcular_salario() de manera distinta.


from abc import ABC, abstractmethod

# Clase abstracta Empleado
class Empleado(ABC):
    
    # Método abstracto para calcular el salario
    @abstractmethod
    def calcular_salario(self):
        pass

# Clase concreta para empleados a tiempo completo
class EmpleadoTiempoCompleto(Empleado):
    
    def __init__(self, salario_mensual):
        self.salario_mensual = salario_mensual
    
    # Implementación del cálculo de salario para empleados a tiempo completo
    def calcular_salario(self):
        return self.salario_mensual

# Clase concreta para empleados por horas
class EmpleadoPorHoras(Empleado):
    
    def __init__(self, horas_trabajadas, tarifa_por_hora):
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora
    
    # Implementación del cálculo de salario para empleados por horas
    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora

# Ejemplos de uso

# Crear un empleado a tiempo completo con un salario mensual de 3000
empleado_tc = EmpleadoTiempoCompleto(3000)
print(f"Salario de empleado a tiempo completo: {empleado_tc.calcular_salario()}")

# Crear un empleado por horas que ha trabajado 120 horas con una tarifa de 20 por hora
empleado_ph = EmpleadoPorHoras(120, 20)
print(f"Salario de empleado por horas: {empleado_ph.calcular_salario()}")
