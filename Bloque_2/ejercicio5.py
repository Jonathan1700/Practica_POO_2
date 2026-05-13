class Tienda:
    def mostrar_inventario(self):
        nombre: str = "Oxxo"
        lista: list[str] = ["Laptops","Cargadores", "parlantes", "mouse"]
        inventario:dict[str, int] = {"nombre": "Laptop", "precio": 900, "stock": 5}

        print("primeras 3 letras del nombre:", nombre[0:3])
        print("el segundo y el cuarto elemento", lista[1:4:2])
        print ("el precio de la laptop es:", inventario["precio"])



tienda = Tienda()
tienda.mostrar_inventario()

