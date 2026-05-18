class Tienda:
    @staticmethod
    def gestionar_inventario():
        productos = ["arroz", "leche", "pan", "huevos", "aceite"]
        productos.insert(2, "azucar")
        e = productos.pop()
        productos.index("pan")
        l = len(productos)
        print (f" El producto eliminado fue: {e}, y quedan {l} productos")

    @staticmethod
    def precios_ordenados():
        precios = [5.50, 2.30, 8.90, 1.20, 6.75, 3.40]
        copia = precios.copy()
        precios.sort()
        print(f"La copia: {copia}, original recortado: {precios}")
        print(f" El valor maximo es {max(precios)}, el valor minimo es {min(precios)}")

    @staticmethod
    def resumen_ventas():
        lunes = [150, 200, 80, 320]
        martes = [90, 175, 410, 60]
        miercoles = [200,150,300,175]
        ventas = []
        ventas.extend(lunes)
        ventas.extend(martes)
        ventas.extend(miercoles)
        v = list(filter(lambda j: j > 200, ventas))
        promedio = sum(ventas) / len(ventas)
        print(f"las ventas semanales fueron:{sum(ventas)}")
        print (f" La venta mas alta fue: {max(ventas)} y la mas baja fue de: {min(ventas)}")
        print (f"las ventas que superaron las 200: {v}")
        print (f"el promedio de las ventas fueron: {promedio}")
        
        



Tienda.gestionar_inventario()
Tienda.precios_ordenados()
Tienda.resumen_ventas()

    