class Banco:
    def __init__(self):
        self.cuentas = {}
        self.usuario_actual = None

    def registrar_cuenta(self):
        nombre = input("Ingrese el nombre de Usuario: ")
        contraseña = input("Ingrese su contraseña")
        pin = input("Ingrese su pin :")
        self.cuentas[nombre] = {
            "contraseña": contraseña,
             "pin": pin
        }
        print(f"Cuenta creada para: {nombre}")
    
    def iniciar_sesion(self):
       nombre = input("Ingrese su nombre de usuario: ")
       pin = input("Ingrese su pin :")
       if nombre in self.cuentas:
            if self.cuentas[nombre]["pin"] == pin:
               self.usuario_actual = nombre
               print (f"Bienvenido, {nombre}")
            else:
               print ("Pin incorrecto")
       else:
           print ("Usuario no encontrado")
        

    def verificar_saldo(self):
        if self.usuario_actual is None:
            print ("No hay cuentas regiistradas")
        else:
            saldo = float(input("Ingrese su saldo: "))
            print(f"su saldo es de: {saldo:.2f}")

    
    def tipo_cuenta(self):
        if self.usuario_actual is None:
            print ("Inicia secion primero")
        else:
            saldo = float(input("Ingrese su saldo"))
            if saldo >= 10000:
                print("Cuenta Premium")
            elif saldo >= 5000:
                print("Cuenta Estándar")
            elif saldo >= 1000:
                print("Cuenta Básica")
            else:
                print( "Saldo insuficiente para abrir cuenta")

    

banco = Banco()
banco.registrar_cuenta()
banco.iniciar_sesion()
banco.verificar_saldo()
banco.tipo_cuenta()