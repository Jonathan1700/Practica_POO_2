class ejercicio_3:
    @staticmethod
    def eje4():
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        triples = list(map(lambda p: p *3, numeros))
        mayores = list(filter(lambda j: j > 5, numeros))
        pares_cuadrados = list(map(lambda p: p** 2, filter(lambda p: p % 2 == 0, numeros)))
        print (triples)
        print(mayores)
        print (pares_cuadrados)
         
ejercicio_3.eje4()
