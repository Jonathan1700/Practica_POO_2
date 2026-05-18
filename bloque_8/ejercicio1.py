class ejercicio1:
    @staticmethod
    def eje1():
        lista = []
        lista.append(2)
        lista.append(4)
        lista.append(5)
        lista.sort()
        print(f"Lista ordenada: {lista}")
    @staticmethod
    def eje2():
        lista = [5, 3, 8, 1, 9, 3]
        print (f"Maximo y minimo:{sum(lista)},{min(lista)}, {max(lista)}")
        
    @staticmethod
    def eje3():
        lista = [5, 3, 8, 1, 9, 3]
        copion = lista.copy()
        referencia = lista
        referencia.append(4)
        print(f"copion: {copion}, referencia: {referencia}, original: {lista}")

        #la diferencia es que la lista copia sigue igual, por que copio la lista que estaba en ese momento
        #La referencia y la lista original ocupan espacio en la memoria por eso al ser modificada, se modifican los dos

ejercicio1.eje1()  
ejercicio1.eje2()
ejercicio1.eje3()