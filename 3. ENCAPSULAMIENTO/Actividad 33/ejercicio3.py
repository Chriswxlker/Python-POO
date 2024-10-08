class Libro:
    # Método constructor
    def __init__(self, titulo, autor, isbn, editorial):
        self.__titulo = titulo  # privado
        self.__autor = autor  # privado
        self.__isbn = isbn  # privado
        self.editorial = editorial  # público

    # Método getter
    def obtener_titulo(self):
        return self.__titulo

    # Método getter
    def obtener_autor(self):
        return self.__autor

    # Método getter
    def obtener_isbn(self):
        return self.__isbn

    # Método setter
    def establecer_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    # Método setter
    def establecer_autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    # Método setter
    def establecer_editorial(self, nuevo_editorial):
        self.editorial = nuevo_editorial  # Cambia el atributo público

    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print(f"\nTítulo: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"ISBN: {self.__isbn}")
        print(f"Editorial: {self.editorial}")

# Objeto
libro = Libro("Meditaciones", "Marco Aurelio", 321654653, "eBOOK")

# Imprimir atributos públicos y privados
libro.mostrar_detalles()

print("---------------------------------------------------")

# Modificar atributos encapsulados usando setters
libro.establecer_titulo("Cómo ser un Estoico")  # setter
print(f"Título: {libro.obtener_titulo()}")  # getter
libro.establecer_autor("Massimo Pigliucci")  # setter
print(f"Autor: {libro.obtener_autor()}")  # getter
libro.establecer_editorial("Nueva Editorial")  # setter
print(f"Editorial: {libro.editorial}")  # público