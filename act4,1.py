import tkinter as tk
from tkinter import ttk
import math

class Notas:
    def __init__(self):
        self.lista_notas = [0.0 for _ in range(5)]

    def calcular_promedio(self):
        suma = 0.0
        for nota in self.lista_notas:
            suma = suma + nota
        return suma / len(self.lista_notas)

    def calcular_desviacion(self):
        prom = self.calcular_promedio()
        suma_cuadrados_diferencias = 0.0
        for nota in self.lista_notas:
            suma_cuadrados_diferencias += math.pow(nota - prom, 2)
        return math.sqrt(suma_cuadrados_diferencias / len(self.lista_notas))

    def calcular_menor(self):
        menor = self.lista_notas[0]
        for nota in self.lista_notas:
            if nota < menor:
                menor = nota
        return menor

    def calcular_mayor(self):
        mayor = self.lista_notas[0]
        for nota in self.lista_notas:
            if nota > mayor:
                mayor = nota
        return mayor

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notas") 
        self.geometry("280x380") 
        self.resizable(False, False) 
        self.init_componentes() 

    def init_componentes(self):
        self.campos = [] 
        for i in range(5):
            etiqueta = ttk.Label(self, text=f"Nota {i+1}:")
            etiqueta.place(x=20, y=20 + i*30)
            campo = ttk.Entry(self)
            campo.place(x=105, y=20 + i*30, width=135)
            self.campos.append(campo)

        self.boton_calcular = ttk.Button(self, text="Calcular", command=self.calcular)
        self.boton_calcular.place(x=20, y=170, width=100)

        self.boton_limpiar = ttk.Button(self, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.place(x=125, y=170, width=100)

        self.etiqueta_promedio = ttk.Label(self, text="Promedio = ")
        self.etiqueta_promedio.place(x=20, y=210)

        self.etiqueta_desviacion = ttk.Label(self, text="Desviación = ")
        self.etiqueta_desviacion.place(x=20, y=240)

        self.etiqueta_mayor = ttk.Label(self, text="Nota mayor = ")
        self.etiqueta_mayor.place(x=20, y=270)

        self.etiqueta_menor = ttk.Label(self, text="Nota menor = ")
        self.etiqueta_menor.place(x=20, y=300)

    def calcular(self):
        try:
            notas = Notas()
            for i in range(5):
                notas.lista_notas[i] = float(self.campos[i].get())
            promedio = notas.calcular_promedio()
            desviacion = notas.calcular_desviacion()
            mayor = notas.calcular_mayor()
            menor = notas.calcular_menor()
            self.etiqueta_promedio.config(text=f"Promedio = {promedio:.2f}")
            self.etiqueta_desviacion.config(text=f"Desviación = {desviacion:.2f}")
            self.etiqueta_mayor.config(text=f"Nota mayor = {mayor}")
            self.etiqueta_menor.config(text=f"Nota menor = {menor}")
        except ValueError:
            self.etiqueta_promedio.config(text="Error: notas inválidas")
            self.etiqueta_desviacion.config(text="")
            self.etiqueta_mayor.config(text="")
            self.etiqueta_menor.config(text="")

    def limpiar(self):
        for campo in self.campos:
            campo.delete(0, tk.END)
        self.etiqueta_promedio.config(text="Promedio = ")
        self.etiqueta_desviacion.config(text="Desviación = ")
        self.etiqueta_mayor.config(text="Nota mayor = ")
        self.etiqueta_menor.config(text="Nota menor = ")

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
