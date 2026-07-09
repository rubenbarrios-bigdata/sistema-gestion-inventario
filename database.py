"""
Módulo: database.py
Gestiona la conexión con la base de datos SQLite y la creación de la tabla productos.
"""

import sqlite3


def conectar():
    """
    Establece y devuelve una conexión con la base de datos 'inventario.db'.
    La base de datos se crea automáticamente si no existe.
    """
    conexion = sqlite3.connect("inventario.db")
    return conexion


def crear_tabla():
    """
    Crea la tabla 'productos' en la base de datos si aún no existe.
    Define las columnas: id, nombre, descripcion, cantidad, precio, categoria.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
        """
    )
    conexion.commit()
    conexion.close()
