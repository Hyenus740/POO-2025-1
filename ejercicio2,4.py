import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base + self.altura + self.hipotenusa()

    def hipotenusa(self):
        return math.sqrt(self.base**2 + self.altura**2)

    def tipo_triangulo(self):
        a = self.base
        b = self.altura
        c = self.hipotenusa()

        if a == b == c:
            return "Equilátero"
        elif a == b or a == c or b == c:
            return "Isósceles"
        else:
            return "Escaleno"

class Rombo:
    def __init__(self, diagonal_mayor, diagonal_menor, lado):
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor
        self.lado = lado

    def area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def perimetro(self):
        return 4 * self.lado

class Trapecio:
    def __init__(self, base_mayor, base_menor, altura, lado1, lado2):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def perimetro(self):
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2

# Clase de prueba
def main():
    # Crear figuras geométricas y probar metodos
    radio = float(input('Radio del circulo en cm:'))
    circulo = Circulo(radio)
    print("Círculo:")
    print(f"Área: {circulo.area():.2f} cm²")
    print(f"Perímetro: {circulo.perimetro():.2f} cm\n")

    base = float(input('Base del rectangulo en cm:'))
    altura = float(input('Altura del rectangulo en cm:'))
    rectangulo = Rectangulo(base, altura)
    print("Rectángulo:")
    print(f"Área: {rectangulo.area()} cm²")
    print(f"Perímetro: {rectangulo.perimetro()} cm\n")

    lado = float(input('Lado del cuadrado en cm:'))
    cuadrado = Cuadrado(lado)
    print("Cuadrado:")
    print(f"Área: {cuadrado.area()} cm²")
    print(f"Perímetro: {cuadrado.perimetro()} cm\n")

    base = float(input('Base del triangulo en cm:'))
    altura = float(input('Altura del triangulo en cm:'))
    triangulo = TrianguloRectangulo(base, altura)
    print("Triángulo Rectángulo:")
    print(f"Área: {triangulo.area()} cm²")
    print(f"Perímetro: {triangulo.perimetro():.2f} cm")
    print(f"Hipotenusa: {triangulo.hipotenusa():.2f} cm")
    print(f"Tipo de triángulo: {triangulo.tipo_triangulo()}\n")

    diagonal_mayor = float(input('Diagonal mayor del rombo en cm:'))
    diagonal_menor = float(input('Diagonal menor del rombo en cm:'))
    lado = float(input('Lado del rombo en cm:'))
    rombo = Rombo(diagonal_mayor, diagonal_menor, lado)
    print("Rombo:")
    print(f"Área: {rombo.area()} cm²")
    print(f"Perímetro: {rombo.perimetro()} cm\n")

    base_mayor = float(input('Base mayor del trapecio en cm:'))
    base_menor = float(input('Base menor del trapecio en cm:'))
    altura = float(input('Altura del trapecio en cm:'))
    lado1 = float(input('Lado1 del trapecio en cm:'))
    lado2 = float(input('Lado2 del trapecio en cm:'))
    trapecio = Trapecio(base_mayor, base_menor, altura, lado1, lado2)
    print("Trapecio:")
    print(f"Área: {trapecio.area()} cm²")
    print(f"Perímetro: {trapecio.perimetro()} cm")

if __name__ == "__main__":
    main()