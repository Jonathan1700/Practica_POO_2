class ejercicio2:
    @staticmethod
    def calcular_interes (*monto, tasa):
        for indice, cantidad in enumerate (monto,1):
            c = cantidad * tasa
            print(f"{indice} Monto: {cantidad} - Interes: {c}")


    @staticmethod
    def filtrar_transacciones(*montos):
        grandes = list(filter(lambda x: x > 1000, montos))
        con_comision = list(map(lambda p: p* 0.02, grandes))
        print (grandes, con_comision)


ejercicio2.calcular_interes(1000, 2000, 500, tasa = 0.05)
ejercicio2.filtrar_transacciones(500, 1500, 200, 3000, 800, 2000)