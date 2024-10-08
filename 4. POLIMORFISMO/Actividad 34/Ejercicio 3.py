class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("------------------------------------------------------------------------")
        print("El perro ladra: ")
        return "GUAUUU"
        print("------------------------------------------------------------------------")

class Gato(Animal):
    def hacer_sonido(self):
        print("------------------------------------------------------------------------")
        print("El gato mahulla: ")
        return "MIAUUU"
        print("------------------------------------------------------------------------")

class Pajaro(Animal):
    def hacer_sonido(self):
        print("------------------------------------------------------------------------")
        print("El loro canta: ")
        return "RRUUUUAAA"
        print("------------------------------------------------------------------------")
    

def imprimir_sonido(animal):
    print(animal.hacer_sonido())

mi_perro = Perro()
mi_gato = Gato()
mi_pajaro = Pajaro()

imprimir_sonido(mi_perro)
imprimir_sonido(mi_gato)
imprimir_sonido(mi_pajaro)