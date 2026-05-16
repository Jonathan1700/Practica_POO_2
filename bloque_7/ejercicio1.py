class ejercicio1:


    def calcular_doble(self, numero):
        return numero *2

    def sumar_elementos(self, *args):
        total = 0
        for numero in args:
            total += numero
        return total

herramientas = ejercicio1()
print(herramientas.calcular_doble(5))
print(herramientas.sumar_elementos(10, 20, 30, 40)) 

