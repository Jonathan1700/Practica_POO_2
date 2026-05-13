class Operacion:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def sumar(self):
        return self.a + self.b
    
    def restar(self):
        return self.a - self.b
    
    def multiplicar(self):
        return self.a * self.b
    
    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: División por cero"
    
    def division_entera(self):
        if self.b != 0:
            return self.a // self.b
        else:
            print ("No se puede dividir por cero")

    def potencia(self):
        return self.a ** self.b
    
    def modulo(self):
        if self.b != 0:
            return self.a % self.b
        else:
            print("No se puede calcular el módulo por cero")


a = 20
b = 4

operaciones = Operacion(a,b)
print(operaciones.sumar()) 
print(operaciones.restar())
print(operaciones.multiplicar())
print(operaciones.division())
print(operaciones.division_entera())
print(operaciones.potencia())
print(operaciones.modulo())


print("="*50)
lista1: list = [3, 4, 5]
lista2: list = [3,4,5]
lista3 = lista1
print (lista1 == lista2)
print (lista1 is lista2)
print (lista1 is lista3)

