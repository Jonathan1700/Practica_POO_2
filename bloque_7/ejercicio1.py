def saludar(nombre):
    return f"Hola {nombre}"

print(saludar("Juan")) 


def presentarse(nombre, edad=25):
    return f"{nombre} tiene {edad} años"

presentarse("Ana")       
presentarse("Ana", 30) 


def dividir(a, b):
    return a // b, a % b  

cociente, resto = dividir(10, 3)



def sumar(*numeros):      
    return sum(numeros)

def mostrar(**datos):      
    for clave, valor in datos.items():
        print(clave, valor)

sumar(1, 2, 3, 4)
mostrar(nombre="Ana", edad=25)


def factorial(n):
    if n == 0: return 1      
    return n * factorial(n-1) 

cuadrado = lambda x: x**2 
print(cuadrado(4))  



def factorial(n):
    if n == 0: return 1
    return n * factorial(n - 1)

print(factorial(5))   

 