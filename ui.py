"""
Módulo: ui.py
Gestiona la interfaz de usuario por terminal: menú principal, entrada de datos
y visualización de resultados.
"""

import productos

# Intenta importar colorama para dar color a la terminal.
# Si no está instalado, se usan mensajes sin color.
try:
    from colorama import init, Fore, Style

    init()
    COLOR_OK = Fore.GREEN
    COLOR_ERROR = Fore.RED
    COLOR_MENU = Fore.CYAN
    COLOR_RESET = Style.RESET_ALL
except ImportError:
    # Si colorama no está disponible, se definen valores vacíos.
    COLOR_OK = ""
    COLOR_ERROR = ""
    COLOR_MENU = ""
    COLOR_RESET = ""


def mostrar_bienvenida():
    """Muestra el encabezado del proyecto al iniciar la aplicación."""
    print(COLOR_MENU + "=" * 64 + COLOR_RESET)
    print(COLOR_MENU + "   PROYECTO FINAL: BASE DE DATOS inventario.db" + COLOR_RESET)
    print(
        COLOR_MENU
        + "   Herramientas utilizadas: Visual Studio Code (Python) - SQLite"
        + COLOR_RESET
    )
    print(
        COLOR_MENU
        + "   Talento Tech: Iniciación a la Programación con Python"
        + COLOR_RESET
    )
    print(COLOR_MENU + "   Alumno: Ruben Barrios" + COLOR_RESET)
    print(COLOR_MENU + "   Tutor: Tomás Torchinsky Landau" + COLOR_RESET)
    print(COLOR_MENU + "   Instructor: Lihuel Landoni Ledesma" + COLOR_RESET)
    print(COLOR_MENU + "   Comisión 26107" + COLOR_RESET)
    print(COLOR_MENU + "=" * 64 + COLOR_RESET)


def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print(COLOR_MENU + "\n--- MENÚ PRINCIPAL ---" + COLOR_RESET)
    print("1. Registrar nuevo producto")
    print("2. Visualizar todos los productos")
    print("3. Actualizar producto por ID")
    print("4. Eliminar producto por ID")
    print("5. Buscar producto")
    print("6. Reporte de bajo stock")
    print("7. Salir")
    print(COLOR_MENU + "-" * 25 + COLOR_RESET)


def mostrar_producto(producto):
    """
    Muestra los datos de un producto en pantalla de forma ordenada.
    'producto' es una tupla con (id, nombre, descripcion, cantidad, precio, categoria).
    """
    if producto is None:
        print(COLOR_ERROR + "Producto no encontrado." + COLOR_RESET)
        return
    print(COLOR_MENU + "-" * 40 + COLOR_RESET)
    print(f"ID:          {producto[0]}")
    print(f"Nombre:      {producto[1]}")
    print(f"Descripción: {producto[2] if producto[2] else '(sin descripción)'}")
    print(f"Cantidad:    {producto[3]}")
    print(f"Precio:      ${producto[4]:.2f}")
    print(f"Categoría:   {producto[5] if producto[5] else '(sin categoría)'}")
    print(COLOR_MENU + "-" * 40 + COLOR_RESET)


def mostrar_productos(lista_productos):
    """
    Muestra una lista completa de productos.
    Si la lista está vacía, informa al usuario.
    """
    if not lista_productos:
        print(COLOR_ERROR + "No hay productos registrados." + COLOR_RESET)
        return
    for producto in lista_productos:
        mostrar_producto(producto)


def pedir_datos_producto():
    """
    Solicita al usuario los datos de un producto por teclado.
    Retorna una tupla (nombre, descripcion, cantidad, precio, categoria).
    Valida que cantidad y precio sean números válidos.
    """
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción: ")

    while True:
        try:
            cantidad = int(input("Cantidad: "))
            break
        except ValueError:
            print(
                COLOR_ERROR
                + "Error: la cantidad debe ser un número entero."
                + COLOR_RESET
            )

    while True:
        try:
            precio = float(input("Precio: "))
            break
        except ValueError:
            print(COLOR_ERROR + "Error: el precio debe ser un número." + COLOR_RESET)

    categoria = input("Categoría: ")
    return nombre, descripcion, cantidad, precio, categoria


def opcion_registrar():
    """Flujo para registrar un nuevo producto."""
    print(COLOR_OK + "\n--- REGISTRAR PRODUCTO ---" + COLOR_RESET)
    nombre, descripcion, cantidad, precio, categoria = pedir_datos_producto()
    productos.registrar_producto(nombre, descripcion, cantidad, precio, categoria)


def opcion_visualizar():
    """Flujo para visualizar todos los productos."""
    print(COLOR_OK + "\n--- LISTA DE PRODUCTOS ---" + COLOR_RESET)
    lista = productos.obtener_todos()
    mostrar_productos(lista)


def opcion_actualizar():
    """Flujo para actualizar un producto existente por su ID."""
    print(COLOR_OK + "\n--- ACTUALIZAR PRODUCTO ---" + COLOR_RESET)
    try:
        id_producto = int(input("ID del producto a actualizar: "))
    except ValueError:
        print(COLOR_ERROR + "Error: el ID debe ser un número entero." + COLOR_RESET)
        return

    # Muestra los datos actuales antes de modificarlos
    producto = productos.buscar_por_id(id_producto)
    if producto is None:
        print(COLOR_ERROR + "No se encontró un producto con ese ID." + COLOR_RESET)
        return

    print("Datos actuales del producto:")
    mostrar_producto(producto)
    print("Ingrese los nuevos datos (deje en blanco para mantener el valor actual):")

    nuevo_nombre = input(f"Nombre [{producto[1]}]: ") or producto[1]
    nueva_descripcion = input(f"Descripción [{producto[2]}]: ") or producto[2]

    while True:
        try:
            entrada_cantidad = input(f"Cantidad [{producto[3]}]: ")
            if entrada_cantidad == "":
                nueva_cantidad = producto[3]
            else:
                nueva_cantidad = int(entrada_cantidad)
            break
        except ValueError:
            print(COLOR_ERROR + "Error: debe ingresar un número entero." + COLOR_RESET)

    while True:
        try:
            entrada_precio = input(f"Precio [{producto[4]:.2f}]: ")
            if entrada_precio == "":
                nuevo_precio = producto[4]
            else:
                nuevo_precio = float(entrada_precio)
            break
        except ValueError:
            print(COLOR_ERROR + "Error: debe ingresar un número." + COLOR_RESET)

    nueva_categoria = input(f"Categoría [{producto[5]}]: ") or producto[5]

    productos.actualizar_producto(
        id_producto,
        nuevo_nombre,
        nueva_descripcion,
        nueva_cantidad,
        nuevo_precio,
        nueva_categoria,
    )


def opcion_eliminar():
    """Flujo para eliminar un producto por su ID."""
    print(COLOR_OK + "\n--- ELIMINAR PRODUCTO ---" + COLOR_RESET)
    try:
        id_producto = int(input("ID del producto a eliminar: "))
    except ValueError:
        print(COLOR_ERROR + "Error: el ID debe ser un número entero." + COLOR_RESET)
        return
    productos.eliminar_producto(id_producto)


def opcion_buscar():
    """Flujo para buscar productos por ID, nombre o categoría."""
    print(COLOR_OK + "\n--- BUSCAR PRODUCTO ---" + COLOR_RESET)
    print("1. Buscar por ID")
    print("2. Buscar por nombre")
    print("3. Buscar por categoría")
    print("4. Volver al menú principal")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        try:
            id_producto = int(input("ID del producto: "))
        except ValueError:
            print(COLOR_ERROR + "Error: el ID debe ser un número entero." + COLOR_RESET)
            return
        producto = productos.buscar_por_id(id_producto)
        mostrar_producto(producto)

    elif opcion == "2":
        nombre = input("Nombre (o parte del nombre): ")
        resultados = productos.buscar_por_nombre(nombre)
        if resultados:
            print(f"Se encontraron {len(resultados)} resultado(s):")
            mostrar_productos(resultados)
        else:
            print(
                COLOR_ERROR
                + "No se encontraron productos con ese nombre."
                + COLOR_RESET
            )

    elif opcion == "3":
        categoria = input("Categoría (o parte de la categoría): ")
        resultados = productos.buscar_por_categoria(categoria)
        if resultados:
            print(f"Se encontraron {len(resultados)} resultado(s):")
            mostrar_productos(resultados)
        else:
            print(
                COLOR_ERROR
                + "No se encontraron productos en esa categoría."
                + COLOR_RESET
            )

    elif opcion == "4":
        return

    else:
        print(COLOR_ERROR + "Opción inválida." + COLOR_RESET)


def opcion_reporte_bajo_stock():
    """Flujo para generar un reporte de productos con stock bajo."""
    print(COLOR_OK + "\n--- REPORTE DE BAJO STOCK ---" + COLOR_RESET)
    try:
        limite = int(input("Ingrese el límite de cantidad para el reporte: "))
    except ValueError:
        print(COLOR_ERROR + "Error: debe ingresar un número entero." + COLOR_RESET)
        return

    resultados = productos.reporte_bajo_stock(limite)
    if resultados:
        print(f"Productos con cantidad igual o inferior a {limite}:")
        mostrar_productos(resultados)
    else:
        print(
            COLOR_OK
            + "No hay productos con stock por debajo del límite indicado."
            + COLOR_RESET
        )


def menu_principal():
    """Bucle principal que muestra el menú y procesa las opciones del usuario."""
    mostrar_bienvenida()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            opcion_registrar()
        elif opcion == "2":
            opcion_visualizar()
        elif opcion == "3":
            opcion_actualizar()
        elif opcion == "4":
            opcion_eliminar()
        elif opcion == "5":
            opcion_buscar()
        elif opcion == "6":
            opcion_reporte_bajo_stock()
        elif opcion == "7":
            print(
                COLOR_OK + "\n¡Gracias por usar el sistema de inventario!" + COLOR_RESET
            )
            break
        else:
            print(COLOR_ERROR + "Opción inválida. Intente nuevamente." + COLOR_RESET)
