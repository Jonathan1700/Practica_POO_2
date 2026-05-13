class Dato:
    def Mostrar(self):
        texto:str="Este es un dato"
        Mi_lista:list[str] = [1, 2, 3]
        Mi_diccionario:dict[str, int] = {"Nombre": "jonathan", "Apellido": "Castro"}


        print("Primer caracter:",texto[0])
        print("ultimo elemento:",Mi_lista[-1])
        print ("valor del dict:", Mi_diccionario["Nombre"])


dato = Dato()
dato.Mostrar()