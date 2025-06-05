import tkinter as tk
from tkinter import ttk
import math

class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0
        self.superficie = 0

    def get_volumen(self):
        return self.volumen

    def get_superficie(self):
        return self.superficie

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.calcular()

    def calcular(self):
        self.volumen = math.pi * self.radio ** 2 * self.altura
        self.superficie = 2 * math.pi * self.radio * self.altura + 2 * math.pi * self.radio ** 2

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.calcular()

    def calcular(self):
        self.volumen = (4/3) * math.pi * self.radio ** 3
        self.superficie = 4 * math.pi * self.radio ** 2

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.calcular()

    def calcular(self):
        self.volumen = (self.base ** 2 * self.altura) / 3
        self.superficie = self.base ** 2 + 2 * self.base * self.apotema


def ventana_cilindro():
    win = tk.Toplevel()
    win.title("Cilindro")

    tk.Label(win, text="Radio (cm):").grid(row=0, column=0)
    tk.Label(win, text="Altura (cm):").grid(row=1, column=0)

    entrada_radio = ttk.Entry(win)
    entrada_altura = ttk.Entry(win)
    entrada_radio.grid(row=0, column=1)
    entrada_altura.grid(row=1, column=1)

    resultado = tk.Label(win, text="")
    resultado.grid(row=3, columnspan=2)

    def calcular():
        radio = float(entrada_radio.get())
        altura = float(entrada_altura.get())
        figura = Cilindro(radio, altura)
        resultado.config(text=f"Volumen (cm³): {figura.get_volumen():.2f}\nSuperficie (cm²): {figura.get_superficie():.2f}")

    ttk.Button(win, text="Calcular", command=calcular).grid(row=2, columnspan=2)

def ventana_esfera():
    win = tk.Toplevel()
    win.title("Esfera")

    tk.Label(win, text="Radio (cm):").grid(row=0, column=0)
    entrada_radio = ttk.Entry(win)
    entrada_radio.grid(row=0, column=1)

    resultado = tk.Label(win, text="")
    resultado.grid(row=2, columnspan=2)

    def calcular():
        radio = float(entrada_radio.get())
        figura = Esfera(radio)
        resultado.config(text=f"Volumen (cm³): {figura.get_volumen():.2f}\nSuperficie (cm²): {figura.get_superficie():.2f}")

    ttk.Button(win, text="Calcular", command=calcular).grid(row=1, columnspan=2)

def ventana_piramide():
    win = tk.Toplevel()
    win.title("Pirámide")

    tk.Label(win, text="Base (cm):").grid(row=0, column=0)
    tk.Label(win, text="Altura (cm):").grid(row=1, column=0)
    tk.Label(win, text="Apotema (cm):").grid(row=2, column=0)

    entrada_base = ttk.Entry(win)
    entrada_altura = ttk.Entry(win)
    entrada_apotema = ttk.Entry(win)

    entrada_base.grid(row=0, column=1)
    entrada_altura.grid(row=1, column=1)
    entrada_apotema.grid(row=2, column=1)

    resultado = tk.Label(win, text="")
    resultado.grid(row=4, columnspan=2)

    def calcular():
        base = float(entrada_base.get())
        altura = float(entrada_altura.get())
        apotema = float(entrada_apotema.get())
        figura = Piramide(base, altura, apotema)
        resultado.config(text=f"Volumen (cm³): {figura.get_volumen():.2f}\nSuperficie (cm²): {figura.get_superficie():.2f}")

    ttk.Button(win, text="Calcular", command=calcular).grid(row=3, columnspan=2)

# Ventana principal
def main():
    root = tk.Tk()
    root.title("Figuras")

    ttk.Button(root, text="Cilindro", command=ventana_cilindro).grid(row=0, column=0, padx=10, pady=10)
    ttk.Button(root, text="Esfera", command=ventana_esfera).grid(row=0, column=1, padx=10, pady=10)
    ttk.Button(root, text="Pirámide", command=ventana_piramide).grid(row=0, column=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()