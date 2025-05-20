class Mascota:
    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Color: {self.color}")



class Perro(Mascota):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color)
        self.peso = peso
        self.muerde = muerde

    @staticmethod
    def sonido():
        print("Los perros ladran")

    def imprimir(self):
        super().imprimir()
        print(f"Peso: {self.peso} kg")
        print(f"Muerde: {'Sí' if self.muerde else 'No'}")
        Perro.sonido()


class PerroPequenio(Perro):
    pass

class Caniche(PerroPequenio):
    pass

class YorkshireTerrier(PerroPequenio):
    pass

class Schnauzer(PerroPequenio):
    pass

class Chihuahua(PerroPequenio):
    pass


class PerroMediano(Perro):
    pass

class Collie(PerroMediano):
    pass

class Dalmata(PerroMediano):
    pass

class Bulldog(PerroMediano):
    pass

class Galgo(PerroMediano):
    pass

class Sabueso(PerroMediano):
    pass


class PerroGrande(Perro):
    pass

class PastorAleman(PerroGrande):
    pass

class Doberman(PerroGrande):
    pass

class Rottweiler(PerroGrande):
    pass



class Gato(Mascota):
    def __init__(self, nombre, edad, color, altura_salto, longitud_salto):
        super().__init__(nombre, edad, color)
        self.altura_salto = altura_salto
        self.longitud_salto = longitud_salto

    @staticmethod
    def sonido():
        print("Los gatos maúllan y ronronean")

    def imprimir(self):
        super().imprimir()
        print(f"Altura de salto: {self.altura_salto} cm")
        print(f"Longitud de salto: {self.longitud_salto} cm")
        Gato.sonido()


class GatoPeloCorto(Gato):
    pass

class AzulRuso(GatoPeloCorto):
    pass

class Britanico(GatoPeloCorto):
    pass

class Manx(GatoPeloCorto):
    pass

class DevonRex(GatoPeloCorto):
    pass


class GatoPeloLargo(Gato):
    pass

class Angora(GatoPeloLargo):
    pass

class Himalayo(GatoPeloLargo):
    pass

class Balines(GatoPeloLargo):
    pass

class Somali(GatoPeloLargo):
    pass


class GatoSinPelo(Gato):
    pass

class Esfinge(GatoSinPelo):
    pass

class Elfo(GatoSinPelo):
    pass

class Donskoy(GatoSinPelo):
    pass



def crear_mascota():
    tipo = input("Ingrese tipo de mascota (perro/gato): ").strip().lower()
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    color = input("Color: ")

    if tipo == "perro":
        peso = float(input("Peso en kg: "))
        muerde = input("¿Muerde? (s/n): ").strip().lower() == 's'
        raza = input("Ingrese raza (ej. caniche, bulldog, etc.): ").strip().lower()

        categoria = None
        if raza in ["caniche", "yorkshire terrier", "schnauzer", "chihuahua"]:
            categoria = "pequeño"
        elif raza in ["collie", "dalmata", "bulldog", "galgo", "sabueso"]:
            categoria = "mediano"
        elif raza in ["pastor aleman", "doberman", "rottweiler"]:
            categoria = "grande"

        if categoria:
            print(f"Categoría: Perro {categoria}")

        if raza == "caniche":
            mascota = Caniche(nombre, edad, color, peso, muerde)
        elif raza == "yorkshire terrier":
            mascota = YorkshireTerrier(nombre, edad, color, peso, muerde)
        elif raza == "schnauzer":
            mascota = Schnauzer(nombre, edad, color, peso, muerde)
        elif raza == "chihuahua":
            mascota = Chihuahua(nombre, edad, color, peso, muerde)
        elif raza == "collie":
            mascota = Collie(nombre, edad, color, peso, muerde)
        elif raza == "dalmata":
            mascota = Dalmata(nombre, edad, color, peso, muerde)
        elif raza == "bulldog":
            mascota = Bulldog(nombre, edad, color, peso, muerde)
        elif raza == "galgo":
            mascota = Galgo(nombre, edad, color, peso, muerde)
        elif raza == "sabueso":
            mascota = Sabueso(nombre, edad, color, peso, muerde)
        elif raza == "pastor aleman":
            mascota = PastorAleman(nombre, edad, color, peso, muerde)
        elif raza == "doberman":
            mascota = Doberman(nombre, edad, color, peso, muerde)
        elif raza == "rottweiler":
            mascota = Rottweiler(nombre, edad, color, peso, muerde)
        else:
            mascota = Perro(nombre, edad, color, peso, muerde)

    elif tipo == "gato":
        altura = float(input("Altura de salto (cm): "))
        longitud = float(input("Longitud de salto (cm): "))
        raza = input("Ingrese raza (ej. angora, esfinge, etc.): ").strip().lower()

        if raza == "angora":
            mascota = Angora(nombre, edad, color, altura, longitud)
        elif raza == "esfinge":
            mascota = Esfinge(nombre, edad, color, altura, longitud)
        else:
            mascota = Gato(nombre, edad, color, altura, longitud)

    else:
        print("Tipo no reconocido")
        return

    print("\n--- DATOS DE LA MASCOTA ---")
    mascota.imprimir()



if __name__ == "__main__":
    crear_mascota()
