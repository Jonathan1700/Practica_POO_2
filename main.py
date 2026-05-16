import os
import sys
import subprocess
import shutil

# ─────────────────────────────────────────────
#   UTILIDADES DE CONSOLA
# ─────────────────────────────────────────────

def gotoxy(x, y):
    print(f"\033[{y};{x}H", end="", flush=True)

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def ocultar_cursor():
    print("\033[?25l", end="", flush=True)

def mostrar_cursor():
    print("\033[?25h", end="", flush=True)

def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def get_cols():
    return shutil.get_terminal_size((80, 24)).columns

def get_filas():
    return shutil.get_terminal_size((80, 24)).lines

RESET = "\033[0m"
BOLD  = "\033[1m"

# ── Paleta ────────────────────────────────────────────────────────
C_BORDE_PRIN  = rgb(0, 200, 255)
C_TITULO_PRIN = rgb(255, 220, 0)
C_OPCION_PRIN = rgb(200, 255, 200)
C_RESALT_PRIN = rgb(255, 120, 0)
C_BORDE_SUB   = rgb(180, 0, 255)
C_TITULO_SUB  = rgb(0, 255, 180)
C_OPCION_SUB  = rgb(230, 230, 255)
C_RESALT_SUB  = rgb(255, 80, 80)
C_SEPARADOR   = rgb(80, 80, 120)
C_SALIR       = rgb(255, 80, 80)
C_DESC_EJ     = rgb(180, 220, 255)
# Visor de código
C_BORDE_COD   = rgb(255, 165, 0)
C_TITULO_COD  = rgb(255, 220, 0)
C_NUM_LINEA   = rgb(100, 100, 140)
C_CODIGO      = rgb(220, 255, 180)
C_SCROLL_INFO = rgb(160, 160, 160)
C_ACCION_1    = rgb(0, 255, 180)
C_ACCION_0    = rgb(255, 80, 80)
# Marco de ejecución
C_BORDE_RUN   = rgb(0, 220, 120)    # verde esmeralda — cabecera
C_TITULO_RUN  = rgb(255, 255, 255)
C_BORDE_FIN   = rgb(0, 180, 255)    # cian — pie
C_ENTER       = rgb(255, 220, 0)


def truncar(texto: str, max_len: int) -> str:
    if len(texto) <= max_len:
        return texto
    return texto[:max_len - 1] + "…"


# ─────────────────────────────────────────────
#   CLASE MENU
# ─────────────────────────────────────────────

class Menu:
    TL = "╔"; TR = "╗"; BL = "╚"; BR = "╝"
    H  = "═"; V  = "║"
    ML = "╠"; MR = "╣"

    def __init__(self, bloques: dict):
        self.bloques = bloques

    # ── Helpers genéricos ──────────────────────────────────────────

    def _borde_h(self, x, y, ancho, izq, der, color):
        gotoxy(x, y)
        print(f"{color}{izq}{self.H * (ancho - 2)}{der}{RESET}", end="", flush=True)

    def _paredes(self, x_ini, x_fin, y, color):
        gotoxy(x_ini, y);  print(f"{color}{self.V}{RESET}", end="", flush=True)
        gotoxy(x_fin, y);  print(f"{color}{self.V}{RESET}", end="", flush=True)

    def _limpiar_fila(self, x_ini, ancho, y):
        gotoxy(x_ini + 1, y)
        print(" " * (ancho - 2), end="", flush=True)

    def _centrar(self, x_ini, ancho, y, texto, color=""):
        interior = ancho - 2
        pad = max(0, (interior - len(texto)) // 2)
        self._limpiar_fila(x_ini, ancho, y)
        gotoxy(x_ini + 1 + pad, y)
        print(f"{color}{texto}{RESET}", end="", flush=True)

    # ── Menú principal ─────────────────────────────────────────────

    def mostrar_principal(self):
        while True:
            limpiar_pantalla()
            ocultar_cursor()

            c     = get_cols()
            f     = get_filas()
            ancho = max(56, min(72, c - 4))
            alto  = len(self.bloques) + 6
            x_ini = max(1, (c - ancho) // 2 + 1)
            x_fin = x_ini + ancho - 1
            y_ini = max(1, (f - alto) // 2)
            cb    = C_BORDE_PRIN
            et    = ancho - 2 - 22          # espacio para tema

            self._borde_h(x_ini, y_ini, ancho, self.TL, self.TR, cb)

            y = y_ini + 1
            self._paredes(x_ini, x_fin, y, cb)
            self._centrar(x_ini, ancho, y, "✦  MENÚ PRINCIPAL  ✦", BOLD + C_TITULO_PRIN)

            y += 1
            self._borde_h(x_ini, y, ancho, self.ML, self.MR, cb)

            for key, bloque in self.bloques.items():
                y += 1
                self._paredes(x_ini, x_fin, y, cb)
                self._limpiar_fila(x_ini, ancho, y)
                nombre = bloque['nombre'][:10]
                tema   = truncar(bloque['tema'], max(8, et))
                linea  = (f"  {C_RESALT_PRIN}[{RESET}{C_OPCION_PRIN}{key}{RESET}"
                          f"{C_RESALT_PRIN}]{RESET}  "
                          f"{C_OPCION_PRIN}{nombre:<10}{RESET}  "
                          f"{C_SEPARADOR}│{RESET}  "
                          f"{C_OPCION_PRIN}{tema}{RESET}")
                gotoxy(x_ini + 1, y)
                print(linea, end="", flush=True)

            y += 1
            self._borde_h(x_ini, y, ancho, self.ML, self.MR, cb)

            y += 1
            self._paredes(x_ini, x_fin, y, cb)
            self._limpiar_fila(x_ini, ancho, y)
            gotoxy(x_ini + 1, y)
            print(f"  {C_RESALT_PRIN}[{RESET}{C_SALIR}S{RESET}"
                  f"{C_RESALT_PRIN}]{RESET}  {C_SALIR}Salir del programa{RESET}",
                  end="", flush=True)

            y += 1
            self._borde_h(x_ini, y, ancho, self.BL, self.BR, cb)

            gotoxy(x_ini, y + 2)
            mostrar_cursor()
            print(f"{C_TITULO_PRIN}  ➤  Elige un bloque: {RESET}", end="", flush=True)
            opcion = input().strip().lower()

            if opcion == 's':
                limpiar_pantalla()
                print(f"\n{C_SALIR}{BOLD}  Saliendo del programa...{RESET}\n")
                break
            elif opcion in self.bloques:
                limpiar_pantalla()
                self.mostrar_submenu(self.bloques[opcion])
            else:
                gotoxy(x_ini, y + 4)
                print(f"{C_SALIR}  Opción no válida. Intenta de nuevo.{RESET}",
                      end="", flush=True)
                mostrar_cursor()
                input()

    # ── Submenú ────────────────────────────────────────────────────

    def mostrar_submenu(self, bloque: dict):
        nombre_bloque = bloque['nombre']
        tema          = bloque['tema']
        ejercicios    = bloque['ejercicios']

        while True:
            limpiar_pantalla()
            ocultar_cursor()

            c     = get_cols()
            ancho = max(60, min(88, c - 2))
            x_ini = max(1, (c - ancho) // 2 + 1)
            x_fin = x_ini + ancho - 1
            cb    = C_BORDE_SUB
            ed    = ancho - 2 - 26          # espacio para desc

            y = 2
            self._borde_h(x_ini, y, ancho, self.TL, self.TR, cb)

            y += 1
            self._paredes(x_ini, x_fin, y, cb)
            titulo = truncar(f"✦  {nombre_bloque.upper()}  —  {tema.upper()}  ✦", ancho - 4)
            self._centrar(x_ini, ancho, y, titulo, BOLD + C_TITULO_SUB)

            y += 1
            self._borde_h(x_ini, y, ancho, self.ML, self.MR, cb)

            opciones_validas = {}
            for i, (nombre_ej, datos) in enumerate(ejercicios.items(), start=1):
                y += 1
                self._paredes(x_ini, x_fin, y, cb)
                self._limpiar_fila(x_ini, ancho, y)
                desc  = truncar(datos['desc'], max(10, ed))
                linea = (f"  {C_RESALT_SUB}[{RESET}{C_OPCION_SUB}{i}{RESET}"
                         f"{C_RESALT_SUB}]{RESET}  "
                         f"{C_OPCION_SUB}{BOLD}{nombre_ej:<14}{RESET}  "
                         f"{C_SEPARADOR}│{RESET}  "
                         f"{C_OPCION_SUB}{desc}{RESET}")
                gotoxy(x_ini + 1, y)
                print(linea, end="", flush=True)
                opciones_validas[str(i)] = datos

            y += 1
            self._borde_h(x_ini, y, ancho, self.ML, self.MR, cb)

            y += 1
            self._paredes(x_ini, x_fin, y, cb)
            self._limpiar_fila(x_ini, ancho, y)
            gotoxy(x_ini + 1, y)
            print(f"  {C_RESALT_SUB}[{RESET}{C_SALIR}0{RESET}"
                  f"{C_RESALT_SUB}]{RESET}  {C_SALIR}Regresar al Menú Principal{RESET}",
                  end="", flush=True)

            y += 1
            self._borde_h(x_ini, y, ancho, self.BL, self.BR, cb)

            gotoxy(x_ini, y + 2)
            mostrar_cursor()
            print(f"{C_TITULO_SUB}  ➤  Elige un ejercicio: {RESET}", end="", flush=True)
            opcion = input().strip()

            if opcion == '0':
                break
            elif opcion in opciones_validas:
                datos = opciones_validas[opcion]
                if self._mostrar_codigo(datos):
                    self._ejecutar_script(datos['ruta'], datos['desc'])
            else:
                gotoxy(x_ini, y + 4)
                print(f"{C_SALIR}  Opción no válida. Intenta de nuevo.{RESET}",
                      end="", flush=True)
                mostrar_cursor()
                input()

    # ── Visor de código ────────────────────────────────────────────

    def _mostrar_codigo(self, datos: dict) -> bool:
        ruta = datos['ruta']
        desc = datos['desc']

        if not os.path.exists(ruta):
            limpiar_pantalla()
            print(f"\n{C_SALIR}  ¡Error! No se encontró: {ruta}{RESET}\n")
            mostrar_cursor()
            input("  Presiona Enter para continuar...")
            return False

        with open(ruta, "r", encoding="utf-8", errors="replace") as f:
            lineas = f.read().splitlines()

        c         = get_cols()
        f_        = get_filas()
        ancho     = max(60, min(90, c - 2))
        x_ini     = max(1, (c - ancho) // 2 + 1)
        x_fin     = x_ini + ancho - 1
        interior  = ancho - 2
        num_w     = 4
        cod_w     = interior - num_w - 2

        CABECERA   = 5
        PIE        = 4
        filas_cod  = max(5, f_ - CABECERA - PIE - 2)

        cb = C_BORDE_COD

        def borde_h(y, izq, der):
            gotoxy(x_ini, y)
            print(f"{cb}{izq}{self.H*(ancho-2)}{der}{RESET}", end="", flush=True)

        def pared(y):
            gotoxy(x_ini, y);  print(f"{cb}{self.V}{RESET}", end="", flush=True)
            gotoxy(x_fin, y);  print(f"{cb}{self.V}{RESET}", end="", flush=True)

        def limpiar_fila(y):
            gotoxy(x_ini+1, y); print(" "*interior, end="", flush=True)

        def centrar(y, texto, color=""):
            pad = max(0, (interior - len(texto)) // 2)
            limpiar_fila(y)
            gotoxy(x_ini+1+pad, y)
            print(f"{color}{texto}{RESET}", end="", flush=True)

        def dibujar_linea_cod(y, num_linea, texto):
            pared(y); limpiar_fila(y)
            num_str = f"{C_NUM_LINEA}{num_linea:>3} {RESET}"
            sep_str = f"{C_SEPARADOR}│{RESET} "
            cod_str = f"{C_CODIGO}{truncar(texto, cod_w)}{RESET}"
            gotoxy(x_ini+1, y)
            print(f"{num_str}{sep_str}{cod_str}", end="", flush=True)

        total  = len(lineas)
        offset = 0

        while True:
            limpiar_pantalla()
            ocultar_cursor()

            y = 1
            borde_h(y, self.TL, self.TR)

            y += 1; pared(y)
            centrar(y, f"◈  CÓDIGO  —  {os.path.basename(ruta)}  ◈", BOLD + C_TITULO_COD)

            y += 1; borde_h(y, self.ML, self.MR)

            y += 1; pared(y); limpiar_fila(y)
            gotoxy(x_ini+1, y)
            print(f"{C_DESC_EJ}{truncar('  ' + desc, interior)}{RESET}", end="", flush=True)

            y += 1; borde_h(y, self.ML, self.MR)

            y_cod_ini = y + 1
            for rel in range(filas_cod):
                ya  = y_cod_ini + rel
                idx = offset + rel
                if idx < total:
                    dibujar_linea_cod(ya, idx + 1, lineas[idx])
                else:
                    pared(ya); limpiar_fila(ya)

            y = y_cod_ini + filas_cod
            borde_h(y, self.ML, self.MR)

            y += 1; pared(y); limpiar_fila(y)
            pag_a = offset // filas_cod + 1
            pag_t = max(1, (total + filas_cod - 1) // filas_cod)
            nav   = "  W/↑ subir   S/↓ bajar  " if total > filas_cod else ""
            info  = truncar(f"  Líneas {offset+1}–{min(offset+filas_cod,total)} de {total}  [{pag_a}/{pag_t}]{nav}", interior)
            gotoxy(x_ini+1, y)
            print(f"{C_SCROLL_INFO}{info}{RESET}", end="", flush=True)

            y += 1; borde_h(y, self.ML, self.MR)

            y += 1; pared(y); limpiar_fila(y)
            gotoxy(x_ini+1, y)
            print(f"  {C_BORDE_COD}[{RESET}{C_ACCION_1}1{RESET}{C_BORDE_COD}]{RESET}"
                  f"  {C_ACCION_1}{BOLD}Ejecutar ejercicio{RESET}"
                  f"        "
                  f"{C_BORDE_COD}[{RESET}{C_ACCION_0}0{RESET}{C_BORDE_COD}]{RESET}"
                  f"  {C_ACCION_0}Volver{RESET}",
                  end="", flush=True)

            y += 1; borde_h(y, self.BL, self.BR)

            gotoxy(x_ini, y + 2)
            mostrar_cursor()
            print(f"{C_TITULO_COD}  ➤  Opción: {RESET}", end="", flush=True)
            tecla = input().strip().lower()

            if tecla in ('1', ''):
                return True
            elif tecla in ('0', 'q', 'b'):
                return False
            elif tecla in ('s', 'j'):
                if offset + filas_cod < total:
                    offset += filas_cod
            elif tecla in ('w', 'k'):
                offset = max(0, offset - filas_cod)

    # ── Ejecutar script con marco arriba y abajo ───────────────────

    @staticmethod
    def _ejecutar_script(ruta: str, descripcion: str = ""):
        limpiar_pantalla()

        c        = get_cols()
        ancho    = min(76, c - 2)
        x_ini    = max(1, (c - ancho) // 2 + 1)
        x_fin    = x_ini + ancho - 1
        interior = ancho - 2
        cb_top   = C_BORDE_RUN

        TL="╔"; TR="╗"; BL="╚"; BR="╝"; H="═"; V="║"; ML="╠"; MR="╣"

        def borde_h(y, izq, der, color):
            gotoxy(x_ini, y)
            print(f"{color}{izq}{H*(ancho-2)}{der}{RESET}", end="", flush=True)

        def pared_top(y):
            gotoxy(x_ini, y);  print(f"{cb_top}{V}{RESET}", end="", flush=True)
            gotoxy(x_fin, y);  print(f"{cb_top}{V}{RESET}", end="", flush=True)

        def limpiar_fila(y):
            gotoxy(x_ini+1, y); print(" "*interior, end="", flush=True)

        def centrar_top(y, texto, color=""):
            pad = max(0, (interior - len(texto)) // 2)
            limpiar_fila(y); gotoxy(x_ini+1+pad, y)
            print(f"{color}{texto}{RESET}", end="", flush=True)

        # ── CABECERA ──────────────────────────────────────────────
        y = 1
        borde_h(y, TL, TR, cb_top)

        y += 1; pared_top(y)
        centrar_top(y, "▶  EJECUTANDO EJERCICIO", BOLD + C_TITULO_RUN)

        y += 1; borde_h(y, ML, MR, cb_top)

        # Archivo
        y += 1; pared_top(y); limpiar_fila(y)
        gotoxy(x_ini+1, y)
        print(f"{C_OPCION_PRIN}{truncar('  Archivo : ' + ruta, interior)}{RESET}",
              end="", flush=True)

        # Descripción (1 o 2 líneas)
        label     = "  Desc.   : "
        max_body  = interior - len(label)
        if len(descripcion) <= max_body:
            y += 1; pared_top(y); limpiar_fila(y)
            gotoxy(x_ini+1, y)
            print(f"{C_DESC_EJ}{label}{descripcion}{RESET}", end="", flush=True)
        else:
            y += 1; pared_top(y); limpiar_fila(y)
            gotoxy(x_ini+1, y)
            print(f"{C_DESC_EJ}{label}{descripcion[:max_body]}{RESET}", end="", flush=True)
            indent = " " * len(label)
            y += 1; pared_top(y); limpiar_fila(y)
            gotoxy(x_ini+1, y)
            print(f"{C_DESC_EJ}{indent}{truncar(descripcion[max_body:], interior - len(indent))}{RESET}",
                  end="", flush=True)

        y += 1; borde_h(y, BL, BR, cb_top)

        # Línea en blanco antes del output del ejercicio
        gotoxy(1, y + 1)
        mostrar_cursor()
        print()          # margen superior del contenido

        # ── EJECUCIÓN (libre — inputs y outputs sin restricción) ──
        try:
            subprocess.run([sys.executable, ruta])
        except Exception as e:
            print(f"\n{C_SALIR}  Error al ejecutar el script: {e}{RESET}")

        # ── PIE ───────────────────────────────────────────────────
        print()          # margen inferior del contenido
        mostrar_cursor()
        input(f"  {C_ENTER}Presiona Enter para volver al menú...{RESET} ")


# ─────────────────────────────────────────────
#   DATOS — TODOS LOS BLOQUES
# ─────────────────────────────────────────────

def main():
    bloques = {
        "0": {
            "nombre": "Bloque 0",
            "tema": "Introducción a la POO",
            "ejercicios": {
                "Ejercicio 1": {
                    "ruta": "Bloque_0/ejercico1.py",
                    "desc": "Identifica 5 clases para modelar un sistema de biblioteca."
                },
                "Ejercicio 2": {
                    "ruta": "Bloque_0/ejercicio2.py",
                    "desc": "Crea la clase Persona (nombre, edad) e instancia 3 objetos."
                }
            }
        },
        "1": {
            "nombre": "Bloque 1",
            "tema": "El Constructor __init__",
            "ejercicios": {
                "Ejercicio 1": {
                    "ruta": "bloque_1/ejercicio1.py",
                    "desc": "Crea la clase Producto e instancia 2 productos."
                },
                "Ejercicio 2": {
                    "ruta": "bloque_1/ejercicio2.py",
                    "desc": "Agrega validación para que el precio no sea negativo."
                },
                "Ejercicio 3": {
                    "ruta": "bloque_1/ejercicip3.py",
                    "desc": "Crea clase Estudiante e inicia lista vacía si no hay notas."
                }
            }
        },
        "2": {
            "nombre": "Bloque 2",
            "tema": "Variables y Tipos de Datos",
            "ejercicios": {
                "Ejercicio 1": {
                    "ruta": "Bloque_2/ejercicio1.py",
                    "desc": "Declara variables de tipo simple y complejo e imprímelas."
                },
                "Ejercicio 2": {
                    "ruta": "Bloque_2/ejercicio2.py",
                    "desc": "Lista de 5 elementos: imprime el 1ro, último y slicing."
                },
                "Ejercicio 4": {
                    "ruta": "Bloque_2/ejercicio4.py",
                    "desc": "Clase con método que declara str, list y dict."
                },
                "Ejercicio 5": {
                    "ruta": "Bloque_2/ejercicio5.py",
                    "desc": "Práctica complementaria de tipos de datos."
                }
            }
        },
        "3": {
            "nombre": "Bloque 3",
            "tema": "Operadores",
            "ejercicios": {
                "Ejercicio 1": {
                    "ruta": "bloque_3/ejercicio1.py",
                    "desc": "Imprime operadores aritméticos con variables dadas."
                }
            }
        },
        "4": {
            "nombre": "Bloque 4",
            "tema": "Entrada y Salida (input/print)",
            "ejercicios": {
                "Ejercicio 1": {
                    "ruta": "bloque_4/ejercicio1.py",
                    "desc": "Pide nombre y edad, muestra mensaje con f-string."
                },
                "Ejercicio 2": {
                    "ruta": "bloque_4/ejercicio2.py",
                    "desc": "Lee dos números, calcula su suma y promedio."
                },
                "Ejercicio 3": {
                    "ruta": "bloque_4/ejercicio3.py",
                    "desc": "Concatenación de string con input sin convertir a entero."
                }
            }
        },
        "5": {
            "nombre": "Bloque 5",
            "tema": "Condicionales",
            "ejercicios": {
                "Ejercicio 1": {
                    "ruta": "bloque_5/ejercicio_1.py",
                    "desc": "Determina si un número es par/impar y asigna calificación."
                },
                "Ejercicio 2": {
                    "ruta": "bloque_5/ejercicio2.py",
                    "desc": "Sistema de login: registra usuario e inicia sesión."
                },
                "Ejercicio 3": {
                    "ruta": "bloque_5/ejercicio3.py",
                    "desc": "Sistema bancario: registro, login, saldo y tipo de cuenta."
                }
            }
        },
        "6": {
            "nombre": "Bloque 6",
            "tema": "Bucles y Colecciones",
            "ejercicios": {
                "Ejercicio 1": {
                    "ruta": "bloque_6/ejercicio1.py",
                    "desc": "While, for, range, enumerate, break, continue y comprensión."
                },
                "Ejercicio 2": {
                    "ruta": "bloque_6/ejercicio2.py",
                    "desc": "Contador, listas de frutas/PC y list comprehension."
                },
                "Ejercicio 3": {
                    "ruta": "bloque_6/ejercicio3.py",
                    "desc": "Clase Salón: agregar, mostrar, buscar y filtrar notas."
                },
                "Ejercicio 4": {
                    "ruta": "bloque_6/ejercicio4.py",
                    "desc": "Clase Inventario: agregar, mostrar y filtrar productos caros."
                }
            }
        },
        "7": {
            "nombre": "Bloque 7",
            "tema": "Funciones",
            "ejercicios": {
                "Ejercicio 1": {
                    "ruta": "bloque_7/ejercicio1.py",
                    "desc": "Funciones con *args, **kwargs, lambda y recursión factorial."
                },
                "Ejercicio 2": {
                    "ruta": "bloque_7/ejercicio2.py",
                    "desc": "Función calcular_doble y sumar_elementos con *args."
                }
            }
        }
    }

    menu = Menu(bloques)
    menu.mostrar_principal()


if __name__ == "__main__":
    main()