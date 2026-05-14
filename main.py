import os
import sys
import subprocess

def limpiar_pantalla():
    """Limpia la pantalla de la consola dependiendo del sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def ejecutar_script(ruta):
    """Ejecuta un script de Python usando el mismo intérprete y pausa al terminar."""
    limpiar_pantalla()
    print(f"--- Ejecutando: {ruta} ---\n")
    try:
        subprocess.run([sys.executable, ruta])
    except Exception as e:
        print(f"Ocurrió un error al intentar ejecutar el script: {e}")
    
    print("\n" + "="*60)
    input("Presiona Enter para volver al menú...")

def menu_bloque(nombre_bloque, tema, ejercicios):
    """Muestra el submenú con los ejercicios y sus descripciones."""
    while True:
        limpiar_pantalla()
        print("="*80)
        print(f"          {nombre_bloque.upper()} - {tema.upper()}")
        print("="*80)
        
        opciones_validas = {}
        for i, (nombre_ej, datos) in enumerate(ejercicios.items(), start=1):
            # Formateamos para que el título y la descripción se vean alineados y limpios
            print(f"  [{i}] {nombre_ej:<12} | {datos['desc']}")
            opciones_validas[str(i)] = datos['ruta']
            
        print("-" * 80)
        print("  [0] Regresar al Menú Principal")
        print("="*80)
        
        opcion = input("\nElige un ejercicio: ")
        
        if opcion == '0':
            break 
        elif opcion in opciones_validas:
            ruta = opciones_validas[opcion]
            if os.path.exists(ruta):
                ejecutar_script(ruta)
            else:
                print(f"\n¡Error! No se encontró el archivo en la ruta: {ruta}")
                print("Asegúrate de que 'main.py' esté en la raíz de la carpeta contenedora.")
                input("Presiona Enter para continuar...")
        else:
            print("\nOpción no válida. Intenta de nuevo.")
            input("Presiona Enter para continuar...")

def main():
    # Diccionario estructurado con Bloques, Temas, Rutas y Descripciones
    bloques = {
        "0": {
            "nombre": "Bloque 0",
            "tema": "Introducción a la POO",
            "ejercicios": {
                "Ejercicio 1": {"ruta": "Bloque_0/ejercico1.py", "desc": "Identifica 5 clases para modelar un sistema de biblioteca."},
                "Ejercicio 2": {"ruta": "Bloque_0/ejercicio2.py", "desc": "Crea la clase Persona (nombre, edad) e instancia 3 objetos."}
            }
        },
        "1": {
            "nombre": "Bloque 1",
            "tema": "El Constructor __init__",
            "ejercicios": {
                "Ejercicio 1": {"ruta": "bloque_1/ejercicio1.py", "desc": "Crea la clase Producto e instancia 2 productos."},
                "Ejercicio 2": {"ruta": "bloque_1/ejercicio2.py", "desc": "Agrega validación para que el precio no sea negativo."},
                "Ejercicio 3": {"ruta": "bloque_1/ejercicip3.py", "desc": "Crea clase Estudiante e inicia lista vacía si no hay notas."}
            }
        },
        "2": {
            "nombre": "Bloque 2",
            "tema": "Variables y Tipos de Datos",
            "ejercicios": {
                "Ejercicio 1": {"ruta": "Bloque_2/ejercicio1.py", "desc": "Declara variables de tipo simple y complejo e imprímelas."},
                "Ejercicio 2": {"ruta": "Bloque_2/ejercicio2.py", "desc": "Lista de 5 elementos: imprime el 1ro, último y slicing."},
                "Ejercicio 4": {"ruta": "Bloque_2/ejercicio4.py", "desc": "Clase con método que declara str, list y dict."},
                "Ejercicio 5": {"ruta": "Bloque_2/ejercicio5.py", "desc": "Práctica complementaria de tipos de datos."}
            }
        },
        "3": {
            "nombre": "Bloque 3",
            "tema": "Operadores",
            "ejercicios": {
                "Ejercicio 1": {"ruta": "bloque_3/ejercicio1.py", "desc": "Imprime operadores aritméticos con variables dadas."}
            }
        },
        "4": {
            "nombre": "Bloque 4",
            "tema": "Entrada y Salida (input/print)",
            "ejercicios": {
                "Ejercicio 1": {"ruta": "bloque_4/ejercicio1.py", "desc": "Pide nombre/edad y muestra mensaje con f-string."},
                "Ejercicio 2": {"ruta": "bloque_4/ejercicio2.py", "desc": "Lee dos números, calcula su suma, promedio y los imprime."},
                "Ejercicio 3": {"ruta": "bloque_4/ejercicio3.py", "desc": "Concatenación de string con input sin convertir a entero."}
            }
        },
    }

    while True:
        limpiar_pantalla()
        print("="*60)
        print("                 MENÚ PRINCIPAL                 ")
        print("="*60)
        for key, bloque in bloques.items():
            # Formato bonito para el menú principal
            print(f"  [{key}] {bloque['nombre']:<10} | {bloque['tema']}")
        print("-" * 60)
        print("  [S] Salir del programa")
        print("="*60)

        opcion = input("\nElige un bloque: ").strip().lower()

        if opcion == 's':
            limpiar_pantalla()
            print("Saliendo del programa...")
            break
        elif opcion in bloques:
            menu_bloque(bloques[opcion]['nombre'], bloques[opcion]['tema'], bloques[opcion]['ejercicios'])
        else:
            print("\nOpción no válida. Intenta de nuevo.")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()