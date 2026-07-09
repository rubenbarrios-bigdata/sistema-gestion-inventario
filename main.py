"""
Módulo: main.py
Punto de entrada del programa. Inicia la base de datos y el menú principal.
"""

from database import crear_tabla
from ui import menu_principal


def main():
    """
    Función principal del programa.
    1. Crea la tabla 'productos' si no existe.
    2. Inicia el menú interactivo para el usuario.
    """
    crear_tabla()
    menu_principal()


if __name__ == "__main__":
    main()
