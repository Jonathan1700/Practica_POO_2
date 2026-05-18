lista = [3, 1, 4, 1, 5]

lista.append(9)      # agrega al final        → [3,1,4,1,5,9]
lista.extend([7,8])  # agrega varios          → [3,1,4,1,5,9,7,8]
lista.insert(0, 99)  # inserta en posición 0  → [99,3,1,4,1,5,9,7,8]
lista.pop()          # elimina y retorna último
lista.remove(1)      # elimina primera ocurrencia de 1
lista.sort()         # ordena in-place
lista.reverse()      # invierte in-place
lista.count(1)       # cuántas veces aparece 1
lista.index(4)       # posición de 4
lista.clear()        # vacía la lista
lista.copy()         # copia superficial


nums = [10, 5, 8, 1, 9]
len(nums)     # 5
sum(nums)     # 33
max(nums)     # 10
min(nums)     # 1
sorted(nums)  # [1,5,8,9,10] ← NO modifica original
nums.sort()   # [1,5,8,9,10] ← SÍ modifica original



lista = [1, 2, 3]
copia_ref  = lista        # misma referencia
copia_real = lista.copy() # objeto nuevo

copia_ref.append(4)
print(lista)      # [1,2,3,4] ← también cambió
print(copia_real) # [1,2,3]   ← no cambió