class Salon:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiantes(self):
        nombre = ""
        while nombre != "listo":
            nombre = input("Ingrese estudiante (o 'listo' para terminar): ")
            if nombre != "listo":
                self.estudiantes.append(nombre)
    
    def mostrar_lista(self):
        for indice, est in enumerate(self.estudiantes,1 ):
            print(indice, est)

    def buscar_estudiantes(self):
        nombre = input("Ingrese el nombre que desea buscar :")
        for est in self.estudiantes:
            if est == nombre:
                print ("Usted a sido encontrado")
                break
        else:
            print("No te encontre bro")

    def mejores_notas(self):
        notas = [5, 8, 3, 9, 6, 10, 4, 7]
        notas1 = [x for x in (notas) if x > 6]
        print(f"Las mejores notas son estas : {notas1}")



salon = Salon()
salon.agregar_estudiantes()
salon.mostrar_lista()
salon.buscar_estudiantes()
salon.mejores_notas()