class Animales:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza


class Personal:
    def __init__(self, nombre, cedula, cargo):
        self.nombre = nombre
        self.cedula = cedula
        self.cargo = cargo


class Citas:
    def __init__(self, fecha, hora):
        self.fecha = fecha
        self.hora = hora


class Medicamentos:
    def __init__(self, nombre, dosis):
        self.nombre = nombre
        self.dosis = dosis

class Registros:
    def __init__(self, fecha_de_cita, hora_de_cita, diagnostico):
        self.fecha = fecha_de_cita
        self.hora = hora_de_cita
        self.diagnostico = diagnostico  

    def Pedir_cita(self, cita):
        return f"La cita está programada para el {cita.fecha} a las {cita.hora}"

perro = Animales ("Kaisa", "Labrador")
medicamento = Medicamentos ("Paracetamol", "500mg")
cita = Citas ("2023-10-15", "10:00")
registros = Registros("2023-10-15", "10:00", "Infección urinaria")
print(registros.Pedir_cita(cita))


