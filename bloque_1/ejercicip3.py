class Membresia:
    def __init__(self, codigo, tipo, precio_mensual):
        if precio_mensual <= 0:
            raise ValueError ("El precio mensual debe ser un valor positivo")
        self.codigo = codigo
        self.tipo = tipo
        self.precio_mensual = precio_mensual


class Miembro:
    def __init__(self, nombre, rutinas):
        if rutinas is None:
            self.rutinas = []
        self.nombre = nombre
        self.rutinas = rutinas


    @classmethod
    def to_dict (cls, datos):
        return cls(nombre=datos["nombre"], rutinas=datos["rutinas"])
    

datos = {"nombre": "Juan", "rutinas": ["Pecho", "espalda"]}

Juan = Miembro.to_dict(datos)
Pedo = Miembro.to_dict({"nombre": "Pedo", "rutinas": ["piernas", "hombros"]})

print (Juan.nombre, Juan.rutinas)
print (Pedo.nombre, Pedo.rutinas)