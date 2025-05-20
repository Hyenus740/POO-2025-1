class Inmueble:
    def __init__(self, id_inmobiliario, area, direccion):
        self.id_inmobiliario = id_inmobiliario
        self.area = area
        self.direccion = direccion
        self.valor_compra = 0

    def calcular_valor_compra(self, valor_m2):
        self.valor_compra = self.area * valor_m2

    def imprimir(self):
        print(f"ID Inmobiliario: {self.id_inmobiliario}")
        print(f"Área: {self.area} m²")
        print(f"Dirección: {self.direccion}")
        print(f"Valor de compra: ${self.valor_compra:,.0f}")


# --------- Vivienda ---------
class InmuebleVivienda(Inmueble):
    def __init__(self, id_inmobiliario, area, direccion, habitaciones, banos):
        super().__init__(id_inmobiliario, area, direccion)
        self.habitaciones = habitaciones
        self.banos = banos

    def imprimir(self):
        super().imprimir()
        print(f"Habitaciones: {self.habitaciones}")
        print(f"Baños: {self.banos}")


# --- Casas ---
class Casa(InmuebleVivienda):
    def __init__(self, id_inmobiliario, area, direccion, habitaciones, banos, pisos):
        super().__init__(id_inmobiliario, area, direccion, habitaciones, banos)
        self.pisos = pisos

    def imprimir(self):
        super().imprimir()
        print(f"Pisos: {self.pisos}")


class CasaRural(Casa):
    def __init__(self, id_inmobiliario, area, direccion, habitaciones, banos, pisos, distancia_cabecera, altitud):
        super().__init__(id_inmobiliario, area, direccion, habitaciones, banos, pisos)
        self.distancia_cabecera = distancia_cabecera
        self.altitud = altitud

    def imprimir(self):
        super().imprimir()
        print(f"Distancia a cabecera municipal: {self.distancia_cabecera} km")
        print(f"Altitud: {self.altitud} msnm")


class CasaUrbana(Casa):
    def __init__(self, id_inmobiliario, area, direccion, habitaciones, banos, pisos):
        super().__init__(id_inmobiliario, area, direccion, habitaciones, banos, pisos)


class CasaConjuntoCerrado(CasaUrbana):
    def __init__(self, id_inmobiliario, area, direccion, habitaciones, banos, pisos, valor_admin, zonas_comunes):
        super().__init__(id_inmobiliario, area, direccion, habitaciones, banos, pisos)
        self.valor_admin = valor_admin
        self.zonas_comunes = zonas_comunes

    def imprimir(self):
        super().imprimir()
        print(f"Valor administración: ${self.valor_admin}")
        print(f"Zonas comunes: {'Sí' if self.zonas_comunes else 'No'}")


class CasaIndependiente(CasaUrbana):
    def __init__(self, id_inmobiliario, area, direccion, habitaciones, banos, pisos):
        super().__init__(id_inmobiliario, area, direccion, habitaciones, banos, pisos)


# --- Apartamentos ---
class Apartamento(InmuebleVivienda):
    def __init__(self, id_inmobiliario, area, direccion, habitaciones, banos, valor_admin):
        super().__init__(id_inmobiliario, area, direccion, habitaciones, banos)
        self.valor_admin = valor_admin

    def imprimir(self):
        super().imprimir()
        print(f"Valor administración: ${self.valor_admin}")


class ApartamentoFamiliar(Apartamento):
    def __init__(self, id_inmobiliario, area, direccion, habitaciones, banos, valor_admin):
        super().__init__(id_inmobiliario, area, direccion, habitaciones, banos, valor_admin)


class Apartaestudio(Apartamento):
    def __init__(self, id_inmobiliario, area, direccion, valor_admin):
        super().__init__(id_inmobiliario, area, direccion, 1, 1, valor_admin)


# --------- Locales ---------
class Local(Inmueble):
    def __init__(self, id_inmobiliario, area, direccion, localizacion):
        super().__init__(id_inmobiliario, area, direccion)
        self.localizacion = localizacion  # "interno" o "calle"

    def imprimir(self):
        super().imprimir()
        print(f"Localización: {self.localizacion}")


class LocalComercial(Local):
    def __init__(self, id_inmobiliario, area, direccion, localizacion, centro_comercial):
        super().__init__(id_inmobiliario, area, direccion, localizacion)
        self.centro_comercial = centro_comercial

    def imprimir(self):
        super().imprimir()
        print(f"Centro Comercial: {self.centro_comercial}")


class Oficina(Local):
    def __init__(self, id_inmobiliario, area, direccion, localizacion, es_gobierno):
        super().__init__(id_inmobiliario, area, direccion, localizacion)
        self.es_gobierno = es_gobierno

    def imprimir(self):
        super().imprimir()
        print(f"Oficina del gobierno: {'Sí' if self.es_gobierno else 'No'}")
if __name__ == "__main__":
    print("=== Datos Apartamento Familiar ===")
    id_apto = int(input("Ingrese ID del inmueble: "))
    area_apto = int(input("Ingrese el área en m²: "))
    direccion_apto = input("Ingrese la dirección: ")
    habitaciones_apto = int(input("Ingrese número de habitaciones: "))
    banos_apto = int(input("Ingrese número de baños: "))
    valor_admin_apto = int(input("Ingrese valor de administración: $"))

    apto1 = ApartamentoFamiliar(
        id_inmobiliario=id_apto,
        area=area_apto,
        direccion=direccion_apto,
        habitaciones=habitaciones_apto,
        banos=banos_apto,
        valor_admin=valor_admin_apto
    )
    apto1.calcular_valor_compra(2000000)  
    apto1.imprimir()

    print("\n=== Datos Apartaestudio ===")
    id_estudio = int(input("Ingrese ID del inmueble: "))
    area_estudio = int(input("Ingrese el área en m²: "))
    direccion_estudio = input("Ingrese la dirección: ")
    valor_admin_estudio = int(input("Ingrese valor de administración: $"))

    aptestudio1 = Apartaestudio(
        id_inmobiliario=id_estudio,
        area=area_estudio,
        direccion=direccion_estudio,
        valor_admin=valor_admin_estudio
    )
    aptestudio1.calcular_valor_compra(1500000)  
    aptestudio1.imprimir()
