class Entrada_Salida:
    def nombre_edad(self):
        nombre: str = input ("Ingrese su nombre: ")
        edad: int = int (input ("Ingrese su edad: "))
        print (f"Su nombre es {nombre} y tiene {edad} años.")

    def promedios(self):
        numero1: int = int(input("Ingrese el primer número: "))
        numero2: int = int(input("Ingrese el segundo número: "))
        promedio: float = (numero1 + numero2)/2 
        print(f"El promedioes: {promedio}")

    def sin_conversion(self):
        numero = input("Ingrese un número: ")
        print(numero + "5")
        print("Explicación: no se sumaron, se concatenaron como texto")

resultados = Entrada_Salida()
resultados.nombre_edad()
resultados.promedios()
resultados.sin_conversion()
