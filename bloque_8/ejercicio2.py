class Sistema_Notas:
    @staticmethod
    def registrar_notas():
        notas = []
        notas.append(3)
        notas.append(10)
        notas.append(15)
        notas.append(18)
        notas.append(10)
        notas.sort()
        print(f"Lista de notas: {notas}")
    
    @staticmethod
    def estadisticas():
        lista = [8, 5, 9, 3, 7, 6, 10, 4]
        total = sum(lista)
        maximo  = max(lista)
        minimo  = min(lista)
        promedio = sum(lista) / len(lista)
        print (f"La suma de las notas es: {total}, y el promedio es {promedio}, el maximo es {maximo}, y el minimo es {minimo}")


    @staticmethod
    def referencia():
        notas = [10,15,10,10,8,2]
        copia = notas.copy()
        referencia = notas
        referencia.append(2)
        print (f"Notas: {notas} || Copia: {copia} || Referencia: {referencia}")
        #lo que pasa es que la lista copia sigue igual, por que copio la lista que estaba en ese momento
        #La referencia y la lista original ocupan espacio en la memoria por eso al ser modificada, se modifican los dos
    
    @staticmethod
    def metodos_extra():
        numeros = [4, 7, 2, 9, 7, 1, 7]
        e = numeros.pop()
        n = numeros.insert(0,99)
        print(f"El numero 7 se repite unas {numeros.count(7)} veces, El nueve esta en la posicion {numeros.index(9)}, numero insetado {numeros}")
        print (f"El numero que fue elminado fue el: {e}")


        
print("== Registro de Notas == ")
Sistema_Notas.registrar_notas()
print ("== Estadisticas ==")
Sistema_Notas.estadisticas()
print (" == Referencia === ")
Sistema_Notas.referencia()
print ("== Metodos extra ==")
Sistema_Notas.metodos_extra() 