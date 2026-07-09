# 📦 Sistema de Gestión de Inventario

Proyecto desarrollado en **Python y SQLite** como trabajo final integrador del curso **Iniciación a la Programación con Python**.

El objetivo de la aplicación es administrar un inventario de productos mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar), utilizando una base de datos **SQLite** y una interfaz de usuario manejada a traves de Python, en este caso VSC.

## 🚀 Tecnologías utilizadas

* 🐍 Python 3
* 🗄️ SQLite

## 📋 Funcionalidades

La aplicación permite:

* ➕ Registrar nuevos productos.
* 📄 Visualizar todos los productos registrados.
* 🔍 Buscar productos por ID.
* ✏️ Actualizar la información de un producto.
* ❌ Eliminar productos por ID.
* 📉 Generar un reporte de productos con bajo stock según un límite definido por el usuario.

## 🗃️ Base de datos

La aplicación utiliza una base de datos SQLite denominada **inventario.db**, que almacena la información de los productos en una tabla llamada **productos** con los siguientes campos:

| Campo       | Descripción                           |
| ----------- | ------------------------------------- |
| id          | Identificador único (autoincremental) |
| nombre      | Nombre del producto                   |
| descripcion | Descripción del producto              |
| cantidad    | Cantidad disponible                   |
| precio      | Precio del producto                   |
| categoria   | Categoría del producto                |

---

## 📂 Estructura del Proyecto

```



sistema-gestion-inventario/

│

├── database.py

├── main.py

├── productos.py

├── ui.py

├── README.md

│

└── images/

\&#x20;   ├── python\\\_vsc.png

\&#x20;   └── sqlite\\\_inventario.png



```
---

🎯 Objetivo del proyecto

Este proyecto tuvo como finalidad aplicar los conocimientos adquiridos durante el curso, integrando conceptos fundamentales como:

- Variables y tipos de datos.
- Funciones.
- Estructuras condicionales.
- Bucles.
- Manejo de archivos.
- Bases de datos SQLite.
- Programación modular.

---

▶️ Ejecución
- Clonar el repositorio.
- Ejecutar el archivo principal del proyecto:
python main.py

La aplicación creará automáticamente la base de datos inventario.db si no existe y mostrará el menú principal para gestionar el inventario.

---

📌 Autor

Rubén Barrios

Proyecto práctico desarrollado como parte de portafolio profesional en análisis y gestión de base de datos.

Academia: Talento Tech.

---

## ⭐ Si este proyecto te parece interesante

No olvides darle una estrella al repositorio y conectar en LinkedIn.

https://www.linkedin.com/in/ruben-barrios-1430712ab/

#Python #SQLite #DataAnalyst #DataAnalytics #Programación #Portfolio #GitHub #SQL #AprendizajeContinuo #TalentoTech