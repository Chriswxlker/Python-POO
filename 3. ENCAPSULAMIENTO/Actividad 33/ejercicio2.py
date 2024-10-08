class Producto:
    # Método constructor
    def __init__(self, nombre, precio, cantidad, categoria):
        self.__nombre = nombre  # privado
        self.__precio = precio  # privado
        self.cantidad = cantidad  # público
        self.categoria = categoria  # público

    # Método getter
    def obtener_nombre(self):
        return self.__nombre

    # Método getter
    def obtener_precio(self):
        return self.__precio

    # Método setter
    def establecer_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Método setter
    def establecer_precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print(f"\nNombre: {self.__nombre}")
        print(f"Precio: {self.__precio}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Categoría: {self.categoria}")

# Objeto
producto = Producto("Caja de zapatos", 300.000, 2, "Zapatos")

# Imprimir atributos públicos y privados
producto.mostrar_detalles()

print("---------------------------------------------------")

# Imprimir el atributo encapsulado modificando su acceso con getter y setter
producto.establecer_nombre("Camisetas")  # setter
print(f"Nombres: {producto.obtener_nombre()}")  # getter
producto.establecer_precio(400.000)  # setter
print(f"Precio: {producto.obtener_precio()}")  # getter
print(f"Cantidad: {producto.cantidad}")  # público
print(f"Categoría: {producto.categoria}")  # público