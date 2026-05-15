# ========== WHILE ==========
print("--- While ---")
contador = 1
while contador <= 3:
    print(f"Contador: {contador}")
    contador += 1

# ========== FOR CON RANGE ==========
print("\n--- For con range ---")
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4

print()
for i in range(1, 6):
    print(i, end=" ")  # 1 2 3 4 5

print()
for i in range(0, 10, 2):
    print(i, end=" ")  # 0 2 4 6 8

# ========== FOR SOBRE COLECCIONES ==========
print("\n\n--- Enumerate ---")
frutas = ["manzana", "pera", "uva"]
for indice, fruta in enumerate(frutas):
    print(f"{indice} → {fruta}")

print("\n--- Diccionario ---")
persona = {"nombre": "Juan", "edad": 25}
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# ========== BREAK Y CONTINUE ==========
print("\n--- Break ---")
for i in range(5):
    if i == 3: break
    print(i, end=" ")  # 0 1 2

print("\n--- Continue ---")
for i in range(5):
    if i == 2: continue
    print(i, end=" ")  # 0 1 3 4

# ========== LIST COMPREHENSION ==========
print("\n\n--- List Comprehension ---")
cuadrados = [x**2 for x in range(5)]
print("Cuadrados:", cuadrados)

pares = [x for x in range(10) if x % 2 == 0]
print("Pares:", pares)

cubos = {x: x**3 for x in range(4)}
print("Cubos:", cubos)