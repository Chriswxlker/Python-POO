from abc import ABC, abstractmethod

class Empleado(ABC):
    
    @abstractmethod
    def calcular_salario(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    
    def __init__(self, salario_mensual):
        self.salario_mensual = salario_mensual
    
    def calcular_salario(self):
        return self.salario_mensual

class EmpleadoPorHoras(Empleado):
    
    def __init__(self, horas_trabajadas, tarifa_por_hora):
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora
    
    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora

empleado_tc = EmpleadoTiempoCompleto(3000)
print(f"Salario de empleado a tiempo completo: {empleado_tc.calcular_salario()}")

empleado_ph = EmpleadoPorHoras(120, 20)
print(f"Salario de empleado por horas: {empleado_ph.calcular_salario()}")
