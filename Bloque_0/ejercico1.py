class libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

class categoria:
    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero

class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula


class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo


class Autor:
    def __init__(self, nombre, libros_publicados):
        self.nombre = nombre
        self.libros_publicados = libros_publicados