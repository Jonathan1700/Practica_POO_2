class Pelicula:
    def __init__(self, nombre,director, año):
        self.nombre = nombre
        self.director = director
        self.año = año

    @classmethod
    def to_dict(cls, datos):
        return cls(datos["Nombre"],datos["director"],datos["años"])

    @classmethod
    def from_text(cls, datos):
        partes = datos.split(",")
        return cls(partes[0],partes[1],partes[2])

datos = {"Nombre": "Lalaland","director":"Jonathan Castro","años": "2010"}

Pelicula1 = Pelicula.to_dict(datos)
Pelicula2 = Pelicula.from_text("Lalaland, Jonathan Castro, 2010")
print (Pelicula1.nombre, Pelicula1.director, Pelicula1.año)
print(Pelicula2.nombre, Pelicula2.director, Pelicula2.año)