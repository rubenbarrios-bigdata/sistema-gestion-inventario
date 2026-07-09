"""
Módulo: productos.py
Contiene las funciones CRUD para la gestión de productos en la base de datos.
"""

from database import conectar


def registrar_producto(nombre, descripcion, cantidad, precio, categoria):
    """
    Inserta un nuevo producto en la tabla productos.
    Recibe nombre, descripcion, cantidad, precio y categoria como parámetros.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        """
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
        """,
        (nombre, descripcion, cantidad, precio, categoria),
    )
    conexion.commit()
    conexion.close()
    print("Producto registrado con éxito.")


def obtener_todos():
    """
    Devuelve una lista con todos los productos registrados.
    Cada producto es una tupla con (id, nombre, descripcion, cantidad, precio, categoria).
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()
    return productos


def actualizar_producto(id, nombre, descripcion, cantidad, precio, categoria):
    """
    Actualiza los datos de un producto existente identificado por su ID.
    Si no existe un producto con ese ID, informa al usuario.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        """
        UPDATE productos
        SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
        WHERE id = ?
        """,
        (nombre, descripcion, cantidad, precio, categoria, id),
    )
    if cursor.rowcount == 0:
        print("No se encontró un producto con ese ID.")
    else:
        print("Producto actualizado con éxito.")
    conexion.commit()
    conexion.close()


def eliminar_producto(id):
    """
    Elimina un producto de la base de datos usando su ID.
    Informa si el producto no existe.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    if cursor.rowcount == 0:
        print("No se encontró un producto con ese ID.")
    else:
        print("Producto eliminado con éxito.")
    conexion.commit()
    conexion.close()


def buscar_por_id(id):
    """
    Busca y devuelve un producto por su ID.
    Retorna None si no existe.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
    producto = cursor.fetchone()
    conexion.close()
    return producto


def buscar_por_nombre(nombre):
    """
    Busca productos cuyo nombre contenga el texto ingresado (búsqueda parcial).
    Devuelve una lista con los resultados.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT * FROM productos WHERE nombre LIKE ?", ("%" + nombre + "%",)
    )
    productos = cursor.fetchall()
    conexion.close()
    return productos


def buscar_por_categoria(categoria):
    """
    Busca productos cuya categoría contenga el texto ingresado (búsqueda parcial).
    Devuelve una lista con los resultados.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT * FROM productos WHERE categoria LIKE ?", ("%" + categoria + "%",)
    )
    productos = cursor.fetchall()
    conexion.close()
    return productos


def reporte_bajo_stock(limite):
    """
    Devuelve una lista de productos cuya cantidad sea igual o inferior al límite indicado.
    Útil para generar alertas de stock mínimo.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT * FROM productos WHERE cantidad <= ? ORDER BY cantidad ASC", (limite,)
    )
    productos = cursor.fetchall()
    conexion.close()
    return productos
