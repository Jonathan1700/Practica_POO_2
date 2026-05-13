class Restaurante:
    def __init__(self):
        self.platos = []
    def registrar_cliente(self):
        nombre: str = input ("Ingrese el nombre del cliente: ")
        plato:str = input("Ingrese el plato deseado: ")
        self.platos.append((nombre,plato))

    def calcular_cuenta(self):
        precio_plato:float = float(input("Ingrese el precio del plato: "))
        cantidad:int = int(input("Ingrese la cantidad de platos: "))
        subtotal = precio_plato * cantidad
        iva = subtotal * 0.12
        total = subtotal + iva

        print(f"Subtotal: {subtotal:.2f}")
        print(f"IVA: {iva:.2f}")
        print(f"Total: {total:.2f}")

    def sin_castear(self):
        numero = input("Ingrese un número de mesa: ")
        print(numero + "-vip")

restaurante = Restaurante()
restaurante.registrar_cliente()
restaurante.calcular_cuenta()
restaurante.sin_castear()
