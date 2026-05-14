class Condicionales:
    def pedir_numero(self):
        num1: int = int(input("Ingrese un número: "))
        if num1 % 2 == 0:
            print("El número es par.")
        else:
            print("El número es impar.")
    
    def calificaciones(self):
        calificaciones: int = int(input("Ingrese la calificación: "))
        if calificaciones >= 90:
            print("A")
        elif calificaciones >= 80:
            print("B")
        elif calificaciones >= 70:
            print("C")
        else:
            print("D") 

condicionales = Condicionales()
condicionales.pedir_numero()
condicionales.calificaciones()
