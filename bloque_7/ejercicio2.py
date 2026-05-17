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

    @staticmethod
    def potencia_recursiva(base, exponente):  
        if exponente == 0:
            return 1
        return base * ejercicio2.potencia_recursiva(base, exponente -1)

    @staticmethod
    def registar_pedidos(*productos, **detalles):
        print ("=== Productos ===")
        for indice, cantidad in enumerate (productos,1):
            print (indice, cantidad)
        print ("=== Detalles ===")
        for clave, valor in (detalles).items():
            print (clave, valor)

    @staticmethod
    def eje4():
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        triples = list(map(lambda p: p *3, numeros))
        mayores = list(filter(lambda j: j > 5, numeros))
        pares_cuadrados = list(map(lambda p: p** 2, filter(lambda p: p % 2 == 0, numeros)))
        print (triples)
        print(mayores)
        print (pares_cuadrados)
         



ejercicio2.calcular_interes(1000, 2000, 500, tasa = 0.05)
print("=" *40)
ejercicio2.filtrar_transacciones(500, 1500, 200, 3000, 800, 2000)
print("=" *40)
print(ejercicio2.potencia_recursiva(3,4))
print("=" *40)
ejercicio2.registar_pedidos("laptop", "mouse", "teclado", cliente="Elian", ciudad="Guayaquil")
ejercicio2.eje4()