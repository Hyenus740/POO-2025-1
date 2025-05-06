class CuentaBancaria:
    def __init__(self, nombres_titular, apellidos_titular, numero_cuenta, tipo_cuenta, interes_mensual=0.0):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta.upper()
        self.saldo = 0.0
        self.interes_mensual = interes_mensual

    def imprimir_datos(self):
        print("\nDatos de la cuenta bancaria:")
        print(f"Nombres del titular: {self.nombres_titular}")
        print(f"Apellidos del titular: {self.apellidos_titular}")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Tipo de cuenta: {self.tipo_cuenta}")
        print(f"Saldo actual: ${self.saldo:,.2f}")
        print(f"Interés mensual: {self.interes_mensual}%")

    def consultar_saldo(self):
        return self.saldo

    def consignar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Se ha consignado ${monto:,.2f} en la cuenta. El nuevo saldo es ${self.saldo:,.2f}")
            return True
        else:
            print("Error: El monto a consignar debe ser positivo")
            return False

    def retirar(self, monto):
        if monto <= 0:
            print("Error: El monto a retirar debe ser positivo")
            return False
        elif monto > self.saldo:
            print("Error: Fondos insuficientes para realizar el retiro")
            return False
        else:
            self.saldo -= monto
            print(f"Se ha retirado ${monto:,.2f} de la cuenta. El nuevo saldo es ${self.saldo:,.2f}")
            return True

    def aplicar_interes_mensual(self):
        if self.interes_mensual > 0:
            interes = self.saldo * (self.interes_mensual / 100)
            self.saldo += interes
            print(f"Se ha aplicado un interés de {self.interes_mensual}% (${interes:,.2f}). Nuevo saldo: ${self.saldo:,.2f}")
            return True
        return False


def main():
    nombres = input('Nombres del titular:')
    apellidos = input('Apellidos del titular:')
    no_cuenta = input('Numero de cuenta:')
    tipo_cuenta = input('Tipo de la cuenta(Ahorros/Corriente):')
    cuenta = CuentaBancaria(
        nombres_titular=nombres,
        apellidos_titular=apellidos,
        numero_cuenta=no_cuenta,
        tipo_cuenta=tipo_cuenta,
        interes_mensual=1.5
    )

    # Imprimir datos iniciales
    cuenta.imprimir_datos()

    # Realizar operaciones
    print('Consignar dinero a la cuenta')
    monto = float(input('Cantidad de dinero a consignar:'))
    cuenta.consignar(monto)
    monto = float(input('Cantidad de dinero a consignar:'))
    cuenta.consignar(monto)
    monto = float(input('Cantidad de dinero a retirar:'))
    cuenta.retirar(monto)

    # Aplicar interés mensual
    cuenta.aplicar_interes_mensual()

    # Consultar saldo final
    print(f"\nSaldo final: ${cuenta.consultar_saldo():,.2f}")

if __name__ == "__main__":
    main()