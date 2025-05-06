#EJERCICIO 2.1

class Persona:
    def __init__(self, nombre, apellidos, identificacion, ano_nacimiento):
        self.nombre = nombre
        self.apellidos = apellidos
        self.identificacion = identificacion
        self.ano_nacimiento = ano_nacimiento

    def datos(self):
      print("Nombre:", self.nombre)
      print("Apellidos:", self.apellidos)
      print("Identificación:", self.identificacion)
      print("Año de nacimiento:", self.ano_nacimiento)


def main():
    print("ingrese datos de la persona 1")
    nombre1 = input("Nombre: ")
    apellidos1 = input("Apellidos: ")
    identificacion1 = input("Identificación: ")
    ano_nacimiento1 = input("Año de nacimiento: ")

    print("ingrese datos de la persona 2")
    nombre2 = input("Nombre: ")
    apellidos2 = input("Apellidos: ")
    identificacion2 = input("Identificación: ")
    ano_nacimiento2 = input("Año de nacimiento: ")

    persona1 = Persona(nombre1, apellidos1, identificacion1, ano_nacimiento1)
    persona2 = Persona(nombre2, apellidos2, identificacion2, ano_nacimiento2)

    print("Datos de la Persona 1:")
    persona1.datos()
    print("\nDatos de la Persona 2:")
    persona2.datos()

main()