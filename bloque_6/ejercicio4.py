class Inventario:
    def __init__(self):
        self.producto = []
    
    def agregar_productos(self):
        producto = ""
        while producto != "listo":
            producto = input("Ingrese el nombre del producto: ")
            if producto != "listo":
                self.producto.append(producto)
    
    def mostrar_productos(self):
        for indice, prd in enumerate(self.producto,1):
            print(indice, prd)
    
    def buscar_producto(self):
        nombre = input("Ingrese el producto: ")
        for est in self.producto:
            if nombre == nombre:
                print ("producto encontrado")
                break
        else:
            print ("Producto no encontrado")
    
    def productos_caros(self):
        caros = [150, 800, 50, 1200, 300, 900, 25, 600]
        carosx = [x for x in (caros) if x >500]
        print(carosx) 
 
inventario = Inventario()
inventario.agregar_productos()
inventario.mostrar_productos()
inventario.buscar_producto()
inventario.productos_caros()

