class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

class Categoria:
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


Cristina = Persona("Cristina", 20)
print(f"Persona: {Cristina.nombre}, Edad: {Cristina.edad}")

Elian = Autor("Elian", ["El temor de un Hombre Sabio", "El ensayo de la segera"])
print(f"Autor: {Elian.nombre}, Libros Publicados: {Elian.libros_publicados}")

Jose = Usuario("Jose", "987654321")
print(f"Usuario: {Jose.nombre}, Cédula: {Jose.cedula}")

print ("Clases Identificadas:")
print ("- Libro")
print ("- Categoría")
print ("- Usuario")
print ("- Préstamo")
print ("- Autor")



