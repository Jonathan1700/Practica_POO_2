class EJERCICIO1:
    
    def saludar(self, nombre):
        return f"Hola {nombre}"

    def presentarse(self, nombre, edad=25):
        return f"{nombre} tiene {edad} años"

    def dividir(self, a, b):
        return a // b, a % b  

    def sumar(self, *numeros):      
        return sum(numeros)

    def mostrar(self, **datos):      
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")

    def factorial(self, n):
        if n == 0: return 1      
        return n * self.factorial(n-1) 
    cuadrado = lambda self, x: x**2 



herramientas = EJERCICIO1()


print(herramientas.saludar("Juan")) 

print(herramientas.presentarse("Ana"))       
cociente, resto = herramientas.dividir(10, 3)
print(f"División de 10/3 -> Cociente: {cociente}, Resto: {resto}")

print(f"Suma: {herramientas.sumar(1, 2, 3, 4)}")

print("Mostrando datos:")
herramientas.mostrar(nombre="Ana", edad=25)

print(f"Cuadrado de 4: {herramientas.cuadrado(4)}")  
print(f"Factorial de 5: {herramientas.factorial(5)}")