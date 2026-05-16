def calcular_doble(numero):
    return numero *2

def sumar_elementos(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(sumar_elementos(10, 20, 30, 40)) 