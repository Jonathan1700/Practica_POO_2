class Compra:
    def __init__(self):
        self.productos = []

    def registrar_producto(self):
        nombre: str = input("Ingrese el nombre del producto: ")
        precio: float = float(input("Ingrese el precio del producto: "))
        self.productos.append((nombre, precio))
        print(f"Producto registrado: {nombre} | Precio: ${precio:.2f}")

    def calcular_descuento(self):
        if not self.productos:
            print("No hay productos registrados.")
            return
        precio_original: float = float(input("Ingrese el precio original del producto: "))
        descuento: float = precio_original * 0.2
        precio_final: float = precio_original - descuento
        print(f"Descuento: ${descuento:.2f}")
        print(f"Precio final: ${precio_final:.2f}")

    def concatenar_sin_castear(self):
        num = input("Ingrese un número: ")
        print(num + "00")


compra = Compra()
compra.registrar_producto()
compra.calcular_descuento()
compra.concatenar_sin_castear()
