
class Persona:
    def __init__(self, nombre, direccion):
        self._nombre = nombre
        self._direccion = direccion

    def getNombre(self):
        return self._nombre

    def getDireccion(self):
        return self._direccion

    def setNombre(self, nombre):
        self._nombre = nombre

    def setDireccion(self, direccion):
        self._direccion = direccion


class Estudiante(Persona):
    def __init__(self, nombre, direccion, carrera, semestre):
        super().__init__(nombre, direccion)
        self._carrera = carrera
        self._semestre = semestre

    def getCarrera(self):
        return self._carrera

    def getSemestre(self):
        return self._semestre

    def setCarrera(self, carrera):
        self._carrera = carrera

    def setSemestre(self, semestre):
        self._semestre = semestre


class Profesor(Persona):
    def __init__(self, nombre, direccion, departamento, categoria):
        super().__init__(nombre, direccion)
        self._departamento = departamento
        self._categoria = categoria

    def getDepartamento(self):
        return self._departamento

    def getCategoria(self):
        return self._categoria

    def setDepartamento(self, departamento):
        self._departamento = departamento

    def setCategoria(self, categoria):
        self._categoria = categoria


# Ejemplo de uso interactivo
def main():
    tipo = input("¿Desea crear un estudiante o un profesor? (e/p): ").lower()
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")

    if tipo == 'e':
        carrera = input("Carrera: ")
        semestre = int(input("Semestre: "))
        persona = Estudiante(nombre, direccion, carrera, semestre)
        print("\n--- Estudiante ---")
        print("Nombre:", persona.getNombre())
        print("Dirección:", persona.getDireccion())
        print("Carrera:", persona.getCarrera())
        print("Semestre:", persona.getSemestre())

    elif tipo == 'p':
        departamento = input("Departamento: ")
        categoria = input("Categoría: ")
        persona = Profesor(nombre, direccion, departamento, categoria)
        print("\n--- Profesor ---")
        print("Nombre:", persona.getNombre())
        print("Dirección:", persona.getDireccion())
        print("Departamento:", persona.getDepartamento())
        print("Categoría:", persona.getCategoria())
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()
