class Pelicula:
    def __init__(self, nombre,director, año):
        self.nombre = nombre
        self.director = director
        self.año = año




    @classmethod
    def to_dict(cls, datos):
        return cls(datos["Nombre"],datos["director"],datos["años"])


datos = {"Nombre": "Lalaland","director":"Jonathan Castro","años": "2010"}

Pelicula1 = Pelicula.to_dict(datos)
print (Pelicula1.nombre, Pelicula1.director, Pelicula1.año)