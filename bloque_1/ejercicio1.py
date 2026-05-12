class Producto:
    def __init__(self, codigo, nombre, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo


p1 = Producto("001", "Refrigeradora", 400)
p2 = Producto("002", "Lavadora", 400)
print(f"Producto: {p1.codigo} | {p1.nombre} | ${p1.precio}")
print(f"Producto: {p2.codigo} | {p2.nombre} | ${p2.precio}")

print("=="*40)


class Estudiante:
    def __init__(self, nombre, notas = None):
        if notas is None:
            self.notas =[]
        else:
            self.notas = notas
        self.nombre = nombre


    @classmethod
    def desde_diccionario(cls,datos):
        return cls (nombre=datos["nombre"], notas=datos["notas"])
    

datos = {"nombre": "Cristina", "notas": [8, 9, 10]}
Estudiante1 = Estudiante.desde_diccionario(datos)
print(f"Estudiante: {Estudiante1.nombre} | Notas: {Estudiante1.notas}")


Estudiante2 = Estudiante("Jose")
print(f"Estudiante: {Estudiante2.nombre} | Notas: {Estudiante2.notas}")
