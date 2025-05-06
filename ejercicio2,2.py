#EJERCICIO #2.2

class Planeta:
    def __init__(self, nombre=None, cantidadsatelites=0, masa=0.0, volumen=0.0, diametro=0.0, distanciasol=0, tipoplaneta=None, observable=False):
        self.nombre = nombre
        self.cantidadsatelites = cantidadsatelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distanciasol = distanciasol
        self.tipoplaneta = tipoplaneta
        self.observable = observable

    def datos(self):
      print("Nombre del planeta =", self.nombre)
      print("Cantidad de satélites =", self.cantidadsatelites)
      print("Masa del planeta =", self.masa)
      print("Volumen del planeta =", self.volumen)
      print("Diámetro del planeta =", self.diametro)
      print("Distancia al sol =", self.distanciasol)
      print("Tipo de planeta =", self.tipoplaneta)
      print("Es observable =", self.observable)

    def densidad(self):
        if self.volumen != 0:
            return self.masa / self.volumen
        return 0

    def es_planeta_exterior(self):
        distancia_en_ua = self.distanciasol / 149.6
        limite_exterior_ua = 3.4
        if distancia_en_ua > limite_exterior_ua:
            return True
        else:
            return False

def especificartipoplaneta():
    while True:
        tipoplaneta = input("Tipo de planeta: ").upper()
        if tipoplaneta in ['GASEOSO', 'TERRESTRE', 'ENANO']:
            return tipoplaneta
        else:
            print("ingrese solo: 'GASEOSO', 'TERRESTRE', 'ENANO'")

def esobservable():
    while True:
        observable = input("¿Es observable a simple vista? (True/False): ").upper()
        if observable == 'TRUE':
            return True
        elif observable == 'FALSE':
            return False
        else:
            print("Ingrese solo: 'True', 'False'")


def main():
    print("Ingrese datos del planeta #1: ")
    nombre1 = input("Nombre del planeta: ")
    cantidadsatelites1 = int(input("Cantidad de satélites del planeta: "))
    masa1 = float(input("Masa del planeta (kg): "))
    volumen1 = float(input("Volumen del planeta (km³): "))
    diametro1 = float(input("Diámetro del planeta (km)"))
    distanciasol1 = int(input("Distancia al Sol (millones de km): "))
    tipoplaneta1 = especificartipoplaneta()
    observable1 = esobservable()

    print("\nIngrese datos del planeta #2: ")
    nombre2 = input("Nombre del planeta: ")
    cantidadsatelites2 = int(input("Cantidad de satélites del planeta: "))
    masa2 = float(input("Masa del planeta (kg): "))
    volumen2 = float(input("Volumen del planeta (km³): "))
    diametro2 = float(input("Diámetro del planeta (km)"))
    distanciasol2 = int(input("Distancia al Sol (millones de km): "))
    tipoplaneta2 = especificartipoplaneta()
    observable2 = esobservable()


    planeta1 = Planeta(nombre1, cantidadsatelites1, masa1, volumen1, diametro1, distanciasol1,
                        tipoplaneta1, observable1)

    planeta2 = Planeta(nombre2, cantidadsatelites2, masa2, volumen2, diametro2, distanciasol2,
                        tipoplaneta2, observable2)

    print("Datos del planeta #1: ")
    planeta1.datos()
    print("Densidad del planeta:", planeta1.densidad())
    print("¿Es un planeta exterior del sistema solar?: ", planeta1.es_planeta_exterior())
    print("\nDatos del planeta #2:")
    planeta2.datos()
    print("Densidad del planeta:", planeta2.densidad())
    print("¿Es un planeta exterior del sistema solar?: ", planeta2.es_planeta_exterior())

if __name__ == "__main__":
    main()