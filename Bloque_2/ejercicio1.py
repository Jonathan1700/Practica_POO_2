entero:int = 19
Tipo_float: float = 19.20
Tipo_cadena: str = "Hola, software A2"
Booleano: bool = False
Valor_Nulo: None = None


Una_lista:list[any] = [67, "six seven", True, 3.19]
Una_tupla:tuple = (67, "six seven", True, 3.19)
Un_diccionario: dict[str, any] = {"Nombre": "Juan", "Edad": 67}
Un_conjunto: set[int] = {67, 19, 3.19}


print("----- Tipos de datos -----")
print("Entero:", entero)
print("Float:", Tipo_float)
print("Cadena:", Tipo_cadena)
print("Booleano:", Booleano)
print("Valor Nulo:", Valor_Nulo)


print ("\n -- Datos complejos --")
print("Lista:", Una_lista)
print("Tupla:", Una_tupla)
print("Diccionario:", Un_diccionario)
print("Conjunto:", Un_conjunto)

