import os
import sys
import runpy
import shutil
import builtins

# ─────────────────────────────────────────────
#   UTILIDADES DE CONSOLA
# ─────────────────────────────────────────────

def gotoxy(x, y):
    # Usamos sys.stdout.write para nunca pasar por builtins.print
    sys.stdout.write(f"\033[{y};{x}H")
    sys.stdout.flush()

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def ocultar_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def mostrar_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def get_cols():
    return shutil.get_terminal_size((80, 24)).columns

def get_filas():
    return shutil.get_terminal_size((80, 24)).lines

def w(texto):
    """Escribe directo a stdout sin pasar por builtins.print."""
    sys.stdout.write(texto)
    sys.stdout.flush()

def wln(texto=""):
    sys.stdout.write(texto + "\n")
    sys.stdout.flush()

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
C_BORDE_COD   = rgb(255, 165, 0)
C_TITULO_COD  = rgb(255, 220, 0)
C_NUM_LINEA   = rgb(100, 100, 140)
C_CODIGO      = rgb(220, 255, 180)
C_SCROLL_INFO = rgb(160, 160, 160)
C_ACCION_1    = rgb(0, 255, 180)
C_ACCION_0    = rgb(255, 80, 80)
C_BORDE_RUN   = rgb(0, 220, 120)
C_TITULO_RUN  = rgb(255, 255, 255)
C_ENTER       = rgb(255, 220, 0)


def truncar(texto: str, max_len: int) -> str:
    if len(texto) <= max_len:
        return texto
    return texto[:max_len - 1] + "…"


# ─────────────────────────────────────────────
#   HELPERS DE DIBUJO  (todos usan w/wln/gotoxy,
#   nunca builtins.print — seguros durante monkey-patch)
# ─────────────────────────────────────────────

TL="╔"; TR="╗"; BL="╚"; BR="╝"; H="═"; V="║"; ML="╠"; MR="╣"

def _borde_h_raw(x, y, ancho, izq, der, color):
    gotoxy(x, y)
    w(f"{color}{izq}{H*(ancho-2)}{der}{RESET}")

def _pared_raw(x_ini, x_fin, y, color):
    gotoxy(x_ini, y); w(f"{color}{V}{RESET}")
    gotoxy(x_fin,  y); w(f"{color}{V}{RESET}")

def _limpiar_fila_raw(x_ini, interior, y):
    gotoxy(x_ini + 1, y)
    w(" " * interior)

def _fila_texto_raw(x_ini, x_fin, interior, y, texto, color_txt, color_borde, indent=1):
    _pared_raw(x_ini, x_fin, y, color_borde)
    _limpiar_fila_raw(x_ini, interior, y)
    trunc = truncar(texto, interior - indent - 1)
    gotoxy(x_ini + indent, y)
    w(f"{color_txt}{trunc}{RESET}")

def _fila_centrada_raw(x_ini, x_fin, interior, y, texto, color_txt, color_borde):
    _pared_raw(x_ini, x_fin, y, color_borde)
    _limpiar_fila_raw(x_ini, interior, y)
    texto_trunc = truncar(texto, interior - 2)
    pad = max(0, (interior - len(texto_trunc)) // 2)
    gotoxy(x_ini + 1 + pad, y)
    w(f"{color_txt}{texto_trunc}{RESET}")


# ─────────────────────────────────────────────
#   CLASE MENU
# ─────────────────────────────────────────────

class Menu:

    def __init__(self, bloques: dict):
        self.bloques = bloques

    # ── Helpers de menús (usan print normal — no hay monkey-patch) ─

    @staticmethod
    def _bh(x, y, ancho, izq, der, color):
        gotoxy(x, y)
        w(f"{color}{izq}{H*(ancho-2)}{der}{RESET}")

    @staticmethod
    def _pw(x_ini, x_fin, y, color):
        gotoxy(x_ini, y); w(f"{color}{V}{RESET}")
        gotoxy(x_fin,  y); w(f"{color}{V}{RESET}")

    @staticmethod
    def _lf(x_ini, interior, y):
        gotoxy(x_ini + 1, y); w(" " * interior)

    @staticmethod
    def _ct(x_ini, interior, y, texto, color=""):
        pad = max(0, (interior - len(texto)) // 2)
        gotoxy(x_ini + 1 + pad, y)
        w(f"{color}{texto}{RESET}")

    # ── Menú principal ─────────────────────────────────────────────

    def mostrar_principal(self):
        while True:
            limpiar_pantalla()
            ocultar_cursor()

            c     = get_cols()
            f     = get_filas()
            ancho = max(56, min(72, c - 4))
            inter = ancho - 2
            alto  = len(self.bloques) + 6
            x_ini = max(1, (c - ancho) // 2 + 1)
            x_fin = x_ini + ancho - 1
            y_ini = max(1, (f - alto) // 2)
            cb    = C_BORDE_PRIN
            et    = inter - 22

            self._bh(x_ini, y_ini, ancho, TL, TR, cb)

            y = y_ini + 1
            self._pw(x_ini, x_fin, y, cb)
            self._lf(x_ini, inter, y)
            self._ct(x_ini, inter, y, "✦  MENÚ PRINCIPAL  ✦", BOLD + C_TITULO_PRIN)

            y += 1
            self._bh(x_ini, y, ancho, ML, MR, cb)

            for key, bloque in self.bloques.items():
                y += 1
                self._pw(x_ini, x_fin, y, cb)
                self._lf(x_ini, inter, y)
                nombre = bloque['nombre'][:10]
                tema   = truncar(bloque['tema'], max(8, et))
                linea  = (f"  {C_RESALT_PRIN}[{RESET}{C_OPCION_PRIN}{key}{RESET}"
                          f"{C_RESALT_PRIN}]{RESET}  "
                          f"{C_OPCION_PRIN}{nombre:<10}{RESET}  "
                          f"{C_SEPARADOR}│{RESET}  "
                          f"{C_OPCION_PRIN}{tema}{RESET}")
                gotoxy(x_ini + 1, y); w(linea)

            y += 1; self._bh(x_ini, y, ancho, ML, MR, cb)
            y += 1
            self._pw(x_ini, x_fin, y, cb)
            self._lf(x_ini, inter, y)
            gotoxy(x_ini + 1, y)
            w(f"  {C_RESALT_PRIN}[{RESET}{C_SALIR}S{RESET}"
              f"{C_RESALT_PRIN}]{RESET}  {C_SALIR}Salir del programa{RESET}")

            y += 1; self._bh(x_ini, y, ancho, BL, BR, cb)

            gotoxy(x_ini, y + 2); mostrar_cursor()
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
                print(f"{C_SALIR}  Opción no válida.{RESET}", end="", flush=True)
                mostrar_cursor(); input()

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
            inter = ancho - 2
            x_ini = max(1, (c - ancho) // 2 + 1)
            x_fin = x_ini + ancho - 1
            cb    = C_BORDE_SUB
            ed    = inter - 26

            y = 2
            self._bh(x_ini, y, ancho, TL, TR, cb)
            y += 1
            self._pw(x_ini, x_fin, y, cb); self._lf(x_ini, inter, y)
            titulo = truncar(f"✦  {nombre_bloque.upper()}  —  {tema.upper()}  ✦", inter - 4)
            self._ct(x_ini, inter, y, titulo, BOLD + C_TITULO_SUB)
            y += 1; self._bh(x_ini, y, ancho, ML, MR, cb)

            opciones_validas = {}
            for i, (nombre_ej, datos) in enumerate(ejercicios.items(), start=1):
                y += 1
                self._pw(x_ini, x_fin, y, cb); self._lf(x_ini, inter, y)
                desc  = truncar(datos['desc'], max(10, ed))
                linea = (f"  {C_RESALT_SUB}[{RESET}{C_OPCION_SUB}{i}{RESET}"
                         f"{C_RESALT_SUB}]{RESET}  "
                         f"{C_OPCION_SUB}{BOLD}{nombre_ej:<14}{RESET}  "
                         f"{C_SEPARADOR}│{RESET}  "
                         f"{C_OPCION_SUB}{desc}{RESET}")
                gotoxy(x_ini + 1, y); w(linea)
                opciones_validas[str(i)] = datos

            y += 1; self._bh(x_ini, y, ancho, ML, MR, cb)
            y += 1
            self._pw(x_ini, x_fin, y, cb); self._lf(x_ini, inter, y)
            gotoxy(x_ini + 1, y)
            w(f"  {C_RESALT_SUB}[{RESET}{C_SALIR}0{RESET}"
              f"{C_RESALT_SUB}]{RESET}  {C_SALIR}Regresar al Menú Principal{RESET}")
            y += 1; self._bh(x_ini, y, ancho, BL, BR, cb)

            gotoxy(x_ini, y + 2); mostrar_cursor()
            print(f"{C_TITULO_SUB}  ➤  Elige un ejercicio: {RESET}", end="", flush=True)
            opcion = input().strip()

            if opcion == '0':
                break
            elif opcion in opciones_validas:
                datos = opciones_validas[opcion]
                if self._mostrar_codigo(datos):
                    self._ejecutar_en_marco(datos['ruta'], datos['desc'])
            else:
                gotoxy(x_ini, y + 4)
                print(f"{C_SALIR}  Opción no válida.{RESET}", end="", flush=True)
                mostrar_cursor(); input()

    # ── Visor de código ────────────────────────────────────────────

    def _mostrar_codigo(self, datos: dict) -> bool:
        ruta = datos['ruta']
        desc = datos['desc']

        if not os.path.exists(ruta):
            limpiar_pantalla()
            print(f"\n{C_SALIR}  ¡Error! No se encontró: {ruta}{RESET}\n")
            mostrar_cursor(); input("  Presiona Enter para continuar...")
            return False

        with open(ruta, "r", encoding="utf-8", errors="replace") as f:
            lineas = f.read().splitlines()

        c         = get_cols()
        f_        = get_filas()
        ancho     = max(60, min(90, c - 2))
        inter     = ancho - 2
        x_ini     = max(1, (c - ancho) // 2 + 1)
        x_fin     = x_ini + ancho - 1
        cod_w     = inter - 6

        CABECERA  = 5
        PIE       = 4
        filas_cod = max(5, f_ - CABECERA - PIE - 2)
        cb        = C_BORDE_COD

        def bh(y, izq, der):
            gotoxy(x_ini, y); w(f"{cb}{izq}{H*(ancho-2)}{der}{RESET}")

        def pared(y):
            gotoxy(x_ini, y); w(f"{cb}{V}{RESET}")
            gotoxy(x_fin,  y); w(f"{cb}{V}{RESET}")

        def lf(y):
            gotoxy(x_ini+1, y); w(" "*inter)

        def ct(y, texto, color=""):
            pad = max(0, (inter - len(texto)) // 2)
            lf(y); gotoxy(x_ini+1+pad, y); w(f"{color}{texto}{RESET}")

        def linea_cod(y, num, texto):
            pared(y); lf(y)
            gotoxy(x_ini+1, y)
            w(f"{C_NUM_LINEA}{num:>3} {RESET}{C_SEPARADOR}│{RESET} "
              f"{C_CODIGO}{truncar(texto, cod_w)}{RESET}")

        total  = len(lineas)
        offset = 0

        while True:
            limpiar_pantalla(); ocultar_cursor()

            y = 1; bh(y, TL, TR)
            y += 1; pared(y)
            ct(y, f"◈  CÓDIGO  —  {os.path.basename(ruta)}  ◈", BOLD + C_TITULO_COD)
            y += 1; bh(y, ML, MR)
            y += 1; pared(y); lf(y)
            gotoxy(x_ini+1, y)
            w(f"{C_DESC_EJ}{truncar('  ' + desc, inter)}{RESET}")
            y += 1; bh(y, ML, MR)

            y_c = y + 1
            for rel in range(filas_cod):
                ya = y_c + rel; idx = offset + rel
                if idx < total:
                    linea_cod(ya, idx+1, lineas[idx])
                else:
                    pared(ya); lf(ya)

            y = y_c + filas_cod; bh(y, ML, MR)
            y += 1; pared(y); lf(y)
            pag_a = offset // filas_cod + 1
            pag_t = max(1, (total + filas_cod - 1) // filas_cod)
            nav   = "  W↑ subir  S↓ bajar  " if total > filas_cod else ""
            gotoxy(x_ini+1, y)
            w(f"{C_SCROLL_INFO}{truncar(f'  Líneas {offset+1}–{min(offset+filas_cod,total)} de {total}  [{pag_a}/{pag_t}]{nav}', inter)}{RESET}")

            y += 1; bh(y, ML, MR)
            y += 1; pared(y); lf(y)
            gotoxy(x_ini+1, y)
            w(f"  {C_BORDE_COD}[{RESET}{C_ACCION_1}1{RESET}{C_BORDE_COD}]{RESET}"
              f"  {C_ACCION_1}{BOLD}Ejecutar{RESET}"
              f"          "
              f"{C_BORDE_COD}[{RESET}{C_ACCION_0}0{RESET}{C_BORDE_COD}]{RESET}"
              f"  {C_ACCION_0}Volver{RESET}")
            y += 1; bh(y, BL, BR)

            gotoxy(x_ini, y+2); mostrar_cursor()
            print(f"{C_TITULO_COD}  ➤  Opción: {RESET}", end="", flush=True)
            tecla = input().strip().lower()

            if tecla in ('1', ''):   return True
            elif tecla in ('0', 'q'): return False
            elif tecla in ('s', 'j'):
                if offset + filas_cod < total: offset += filas_cod
            elif tecla in ('w', 'k'):
                offset = max(0, offset - filas_cod)

    # ── Ejecutar dentro de marco ────────────────────────────────────

    @staticmethod
    def _ejecutar_en_marco(ruta: str, descripcion: str = ""):
        """
        Todo el dibujo usa sys.stdout.write (función w/wln/gotoxy).
        El monkey-patch reemplaza builtins.print y builtins.input,
        pero NUNCA llama a esas funciones internamente — usa w() y
        sys.stdin.readline() directamente, eliminando toda recursión.
        """
        limpiar_pantalla()

        c     = get_cols()
        ancho = min(78, c - 2)
        inter = ancho - 2
        x_ini = max(1, (c - ancho) // 2 + 1)
        x_fin = x_ini + ancho - 1
        cb    = C_BORDE_RUN

        # ── Helpers internos (w, nunca print) ─────────────────────

        def bh(y, izq, der, color=None):
            clr = color or cb
            gotoxy(x_ini, y)
            w(f"{clr}{izq}{H*(ancho-2)}{der}{RESET}")

        def pared(y, color=None):
            clr = color or cb
            gotoxy(x_ini, y); w(f"{clr}{V}{RESET}")
            gotoxy(x_fin,  y); w(f"{clr}{V}{RESET}")

        def lf(y):
            gotoxy(x_ini+1, y); w(" "*inter)

        def fila_ct(y, texto, color_txt, color_borde=None):
            pared(y, color_borde)
            lf(y)
            pad = max(0, (inter - len(texto)) // 2)
            gotoxy(x_ini+1+pad, y)
            w(f"{color_txt}{texto}{RESET}")

        def fila_tx(y, texto, color_txt, indent=1):
            pared(y)
            lf(y)
            trunc = truncar(texto, inter - indent - 1)
            gotoxy(x_ini + indent, y)
            w(f"{color_txt}{trunc}{RESET}")

        def fila_v(y):
            pared(y); lf(y)

        # ── CABECERA ──────────────────────────────────────────────
        y = 2
        bh(y, TL, TR)
        y += 1; fila_ct(y, "▶  EJECUTANDO EJERCICIO", BOLD + C_TITULO_RUN)
        y += 1; bh(y, ML, MR)
        y += 1; fila_tx(y, f"Archivo : {ruta}", C_OPCION_PRIN)

        label    = "Desc.   : "
        max_body = inter - len(label) - 2
        if len(descripcion) <= max_body:
            y += 1; fila_tx(y, f"{label}{descripcion}", C_DESC_EJ)
        else:
            y += 1; fila_tx(y, f"{label}{descripcion[:max_body]}", C_DESC_EJ)
            y += 1; fila_tx(y, " "*len(label) + truncar(descripcion[max_body:], max_body), C_DESC_EJ)

        y += 1; bh(y, ML, MR)
        y += 1; fila_v(y)   # margen antes del output

        # fila donde empieza el output del ejercicio
        y_out = y + 1

        mostrar_cursor()

        # ── MONKEY-PATCH (sin recursión) ──────────────────────────
        _orig_print = builtins.print
        _orig_input = builtins.input

        # Estado compartido entre pared_print y pared_input
        estado = {"fila": y_out, "prompt_pendiente": ""}

        def _dibujar_fila(texto: str, color_txt: str = C_OPCION_PRIN):
            """Dibuja una línea de output dentro del marco usando w()."""
            yf = estado["fila"]
            # Pared izquierda
            gotoxy(x_ini, yf); w(f"{cb}{V}{RESET}")
            # Contenido
            trunc = truncar(texto, inter - 2)
            gotoxy(x_ini + 2, yf); w(f"{color_txt}{trunc}{RESET}")
            # Limpiar resto de la fila
            relleno = inter - 2 - len(trunc)
            if relleno > 0:
                w(" " * relleno)
            # Pared derecha
            gotoxy(x_fin, yf); w(f"{cb}{V}{RESET}")
            # Bajar fila
            estado["fila"] += 1

        def pared_print(*args, **kwargs):
            sep  = kwargs.get("sep", " ")
            end  = kwargs.get("end", "\n")
            file = kwargs.get("file", None)
            # Stderr u otro destino → stderr real, sin marco
            if file is sys.stderr:
                sys.stderr.write(sep.join(str(a) for a in args) + (end if end else ""))
                return
            if file not in (None, sys.stdout):
                return
            texto  = sep.join(str(a) for a in args)
            partes = texto.split("\n")
            # print con end="" (prompt inline) → guardar y mostrar en input
            if end == "" and len(partes) == 1:
                estado["prompt_pendiente"] += partes[0]
                return
            # Primera parte puede llevar prompt pendiente pegado
            if estado["prompt_pendiente"]:
                partes[0] = estado["prompt_pendiente"] + partes[0]
                estado["prompt_pendiente"] = ""
            for parte in partes:
                _dibujar_fila(parte)

        def pared_input(prompt=""):
            prompt_str = estado["prompt_pendiente"] + str(prompt)
            estado["prompt_pendiente"] = ""
            yf = estado["fila"]
            # Dibujar la fila del prompt
            gotoxy(x_ini, yf); w(f"{cb}{V}{RESET}")
            trunc = truncar(prompt_str, inter - 4)
            gotoxy(x_ini + 2, yf); w(f"{C_DESC_EJ}{trunc}{RESET}")
            col_input = x_ini + 2 + len(trunc)
            # Limpiar resto
            relleno = inter - 2 - len(trunc)
            if relleno > 0: w(" " * relleno)
            gotoxy(x_fin, yf); w(f"{cb}{V}{RESET}")
            # Posicionar cursor para que el usuario escriba dentro del marco
            gotoxy(col_input, yf)
            val = sys.stdin.readline().rstrip("\n")
            # Redibujar pared derecha (el texto del usuario la pudo pisar)
            gotoxy(x_fin, yf); w(f"{cb}{V}{RESET}")
            estado["fila"] += 1
            return val

        builtins.print = pared_print
        builtins.input = pared_input

        # ── EJECUCIÓN ─────────────────────────────────────────────
        try:
            runpy.run_path(os.path.abspath(ruta), run_name="__main__")
        except SystemExit:
            pass
        except Exception as e:
            _dibujar_fila(f"⚠  Error: {e}", C_SALIR)
        finally:
            builtins.print = _orig_print
            builtins.input = _orig_input

        # ── PIE ───────────────────────────────────────────────────
        yp = estado["fila"]
        fila_v(yp);       yp += 1
        bh(yp, ML, MR);   yp += 1
        fila_ct(yp, "✔  Ejercicio finalizado", BOLD + C_TITULO_RUN)
        yp += 1; bh(yp, ML, MR); yp += 1
        ocultar_cursor()
        fila_ct(yp, "Presiona Enter para volver al menú...", C_ENTER)
        yp += 1; bh(yp, BL, BR)

        gotoxy(x_ini + 1, yp + 1); mostrar_cursor()
        sys.stdin.readline()


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
