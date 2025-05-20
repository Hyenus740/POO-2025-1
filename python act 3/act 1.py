class Cuenta:
    def __init__(self, saldo: float, tasa_anual: float):
        self._saldo = saldo
        self._num_consignaciones = 0
        self._num_retiros = 0
        self._tasa_anual = tasa_anual
        self._comision_mensual = 0.0

    def consignar(self, cantidad: float):
        self._saldo += cantidad
        self._num_consignaciones += 1

    def retirar(self, cantidad: float):
        if cantidad <= self._saldo:
            self._saldo -= cantidad
            self._num_retiros += 1
        else:
            print("Fondos insuficientes.")

    def calcular_interes_mensual(self):
        interes_mensual = (self._tasa_anual / 12) * self._saldo
        self._saldo += interes_mensual

    def extracto_mensual(self):
        self._saldo -= self._comision_mensual
        self.calcular_interes_mensual()

    def imprimir(self):
        print(f"Saldo: ${self._saldo:.2f}")
        print(f"Número de consignaciones: {self._num_consignaciones}")
        print(f"Número de retiros: {self._num_retiros}")
        print(f"Tasa anual: {self._tasa_anual}")
        print(f"Comisión mensual: ${self._comision_mensual:.2f}")


class CuentaAhorros(Cuenta):
    def __init__(self, saldo: float, tasa_anual: float):
        super().__init__(saldo, tasa_anual)
        self._activa = saldo >= 10000

    def consignar(self, cantidad: float):
        if self._activa:
            super().consignar(cantidad)
        else:
            print("Cuenta inactiva. No se puede consignar.")
        self._actualizar_estado()

    def retirar(self, cantidad: float):
        if self._activa:
            super().retirar(cantidad)
        else:
            print("Cuenta inactiva. No se puede retirar.")
        self._actualizar_estado()

    def extracto_mensual(self):
        if self._num_retiros > 4:
            self._comision_mensual += (self._num_retiros - 4) * 1000
        super().extracto_mensual()
        self._actualizar_estado()

    def _actualizar_estado(self):
        self._activa = self._saldo >= 10000

    def imprimir(self):
        super().imprimir()
        print(f"Estado de la cuenta: {'Activa' if self._activa else 'Inactiva'}")



if __name__ == "__main__":
    print("Cuenta de ahorros")
    saldo_inicial = float(input("Ingrese saldo inicial= $ "))
    tasa_interes = float(input("Ingrese tasa de interés (por ejemplo 0.1 para 10%)= "))

    cuenta = CuentaAhorros(saldo_inicial, tasa_interes)

    valor_consignar = float(input("Ingresar cantidad a consignar= $"))
    cuenta.consignar(valor_consignar)

    valor_retirar = float(input("Ingresar cantidad a retirar= $"))
    cuenta.retirar(valor_retirar)

    cuenta.extracto_mensual()
    cuenta.imprimir()
