class banco:
    def __init__(self):
        self.cuentas = {}

    def registrar_cuenta(self):
        nombre = input("Ingrese el nombre de Usuario")
        contraseña = input("Ingrese su contraseña")
        self.cuentas[nombre] = contraseña
        print(f"Cuenta creada para: {nombre}")
    

    def verificar_saldo(self):
            