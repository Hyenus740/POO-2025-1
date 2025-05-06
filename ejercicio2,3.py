#ejercicio 2.3
class Automovil:
    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil, numero_puertas, cantidad_asientos, velocidad_maxima, color):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = 0

    # Métodos get
    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_motor(self):
        return self.motor

    def get_tipo_combustible(self):
        return self.tipo_combustible

    def get_tipo_automovil(self):
        return self.tipo_automovil

    def get_numero_puertas(self):
        return self.numero_puertas

    def get_cantidad_asientos(self):
        return self.cantidad_asientos

    def get_velocidad_maxima(self):
        return self.velocidad_maxima

    def get_color(self):
        return self.color

    def get_velocidad_actual(self):
        return self.velocidad_actual

    # Métodos set
    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_motor(self, motor):
        self.motor = motor

    def set_tipo_combustible(self, tipo_combustible):
        self.tipo_combustible = tipo_combustible

    def set_tipo_automovil(self, tipo_automovil):
        self.tipo_automovil = tipo_automovil

    def set_numero_puertas(self, numero_puertas):
        self.numero_puertas = numero_puertas

    def set_cantidad_asientos(self, cantidad_asientos):
        self.cantidad_asientos = cantidad_asientos

    def set_velocidad_maxima(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima

    def set_color(self, color):
        self.color = color

    def set_velocidad_actual(self, velocidad_actual):
        if velocidad_actual < 0:
            print("¡Advertencia! No es posible establecer una velocidad negativa.")
            self.velocidad_actual = 0
        else:
            self.velocidad_actual = velocidad_actual

    def acelerar(self, incremento_velocidad):
        nueva_velocidad = self.velocidad_actual + incremento_velocidad
        if nueva_velocidad <= self.velocidad_maxima:
            self.velocidad_actual = nueva_velocidad
        else:
            print(f"¡Advertencia! No se puede acelerar más allá de la velocidad máxima ({self.velocidad_maxima} km/h).")

    def desacelerar(self, decremento_velocidad):
        nueva_velocidad = self.velocidad_actual - decremento_velocidad
        if nueva_velocidad >= 0:
            self.velocidad_actual = nueva_velocidad
        else:
            print("¡Advertencia! No es posible desacelerar a una velocidad negativa.")
            self.velocidad_actual = 0

    def frenar(self):
        self.velocidad_actual = 0
        print("El automóvil ha frenado.")

    def calcular_tiempo_estimado(self, distancia):
        if self.velocidad_actual > 0:
            tiempo_estimado = distancia / self.velocidad_actual
            return tiempo_estimado
        else:
            return "El automóvil está detenido, no se puede calcular el tiempo de llegada."

    def mostrar_atributos(self):
        print("--- Atributos del Automóvil ---")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Motor: {self.motor} L")
        print(f"Tipo de Combustible: {self.tipo_combustible}")
        print(f"Tipo de Automóvil: {self.tipo_automovil}")
        print(f"Número de Puertas: {self.numero_puertas}")
        print(f"Cantidad de Asientos: {self.cantidad_asientos}")
        print(f"Velocidad Máxima: {self.velocidad_maxima} km/h")
        print(f"Color: {self.color}")
        print(f"Velocidad Actual: {self.velocidad_actual} km/h")
        print("-----------------------------")

def main():
    print("Por favor, ingrese los datos del automóvil:")
    marca = input("Marca: ")
    modelo = int(input("Modelo (año): "))
    motor = float(input("Motor (volumen en litros): "))
    tipo_combustible = input("Tipo de combustible (gasolina, bioetanol, diésel, biodiésel, gas natural): ")
    tipo_automovil = input("Tipo de automóvil (carro de ciudad, subcompacto, compacto, familiar, ejecutivo, SUV): ")
    numero_puertas = int(input("Número de puertas: "))
    cantidad_asientos = int(input("Cantidad de asientos: "))
    velocidad_maxima = int(input("Velocidad máxima (km/h): "))
    color = input("Color (blanco, negro, rojo, naranja, amarillo, verde, azul, violeta): ")

    mi_auto = Automovil(
        marca=marca,
        modelo=modelo,
        motor=motor,
        tipo_combustible=tipo_combustible,
        tipo_automovil=tipo_automovil,
        numero_puertas=numero_puertas,
        cantidad_asientos=cantidad_asientos,
        velocidad_maxima=velocidad_maxima,
        color=color
    )

    print("\nEstado inicial del automóvil:")
    mi_auto.mostrar_atributos()

    velocidad_inicial = int(input("\nIngrese la velocidad actual inicial (km/h): "))
    mi_auto.set_velocidad_actual(velocidad_inicial)
    print(f"Velocidad actual después de establecer: {mi_auto.get_velocidad_actual()} km/h")

    incremento = int(input("Ingrese la cantidad a acelerar (km/h): "))
    mi_auto.acelerar(incremento)
    print(f"Velocidad actual después de acelerar: {mi_auto.get_velocidad_actual()} km/h")

    decremento = int(input("Ingrese la cantidad a desacelerar (km/h): "))
    mi_auto.desacelerar(decremento)
    print(f"Velocidad actual después de desacelerar: {mi_auto.get_velocidad_actual()} km/h")

    input("\nPresione Enter para frenar el automóvil.")
    mi_auto.frenar()
    print(f"Velocidad actual después de frenar: {mi_auto.get_velocidad_actual()} km/h")

if __name__ == "__main__":
    main()