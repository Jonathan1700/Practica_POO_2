class login:
    def __init__(self):
        self.usuarios = {}

    def registrar(self):
        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = int(input("Ingrese su contraseña: "))
        self.usuarios[usuario] = contraseña
        print(f"El usuario {usuario} ha sido registrado.")

    def inicio(self):
        if self.usuarios is None:
            print("No hay usuarios registrados.")
        else:
            usuario = input("Ingrese su nombre de usuario: ")
            contraseña: int = int(input("Ingrese su contraseña: "))
            if usuario in self.usuarios and self.usuarios[usuario] == contraseña:
                print(f"¡Bienvenido, {usuario}!")
            else:
                print("Nombre de usuario o contraseña incorrectos.")
                


a = login()
a.registrar()
a.inicio()
