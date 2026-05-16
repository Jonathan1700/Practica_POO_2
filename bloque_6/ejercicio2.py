class BuclesYColecciones:
    def __init__(self):
        self.frutas = ["Pera", "Mandarina", "UVA"]
        self.pc = ["Procesador", "ram", "disco"]

    def contar_hasta_diez(self):
        print("--- Contador ---")
        contador = 1
        while contador <= 10:
            print(contador)
            contador += 1

    def listar_frutas(self):
        print("\n--- Lista de Frutas ---")
        for indice, fruta in enumerate(self.frutas):
            print(indice, fruta)

    def listar_pc(self):
        print("\n--- Componentes de PC ---")
        for indice, componente in enumerate(self.pc):
            print(indice, componente)

    def mostrar_cuadrados_pares(self):
        print("\n--- Cuadrados Pares ---")
        cuadrados = [x**2 for x in range(1, 11) if x % 2 == 0]
        print(cuadrados)


mis_bucles = BuclesYColecciones()


mis_bucles.contar_hasta_diez()
mis_bucles.listar_frutas()
mis_bucles.listar_pc()
mis_bucles.mostrar_cuadrados_pares()