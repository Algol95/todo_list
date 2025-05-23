# 📝 Proyecto TODO List - Python Vanilla + PostgreSQL

Este proyecto es un ejemplo funcional de una aplicación de consola que permite gestionar tareas (CRUD) utilizando **Python**, **arquitectura MVC**, **SQLAlchemy** y **PostgreSQL**, sin frameworks.

---

## 📦 Requisitos previos

- Python 3.10 o superior
- PostgreSQL instalado
- Acceso a `psql` desde consola
- Git (opcional)

---

## 📄 Documentación

Aplicación documentada con Pdoc 🐍

Para acceder a ella acceder a la carpeta `docs_html > index.html`

![Pdoc](https://i.imgur.com/ApyrQvQ.png)

---

## ⚙️ Configuración inicial

### 1. Clona el repositorio (si es necesario)

```bash
git clone <url-del-repo>
cd todo_list
```

### 2. Crea y activa entorno virtual

```bash
python -m venv venv
.env\Scriptsctivate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

---

## 🛠️ Base de datos

### 1. Crea la base de datos en PostgreSQL

Usa este comando (fuera del entorno virtual):

```bash
psql -U postgres -c "CREATE DATABASE todo_db;"
```

> Asegúrate de tener acceso a `psql`  
> Puedes modificarla en `database/db.py`.

---

## 🔗 Conexión a PostgreSQL

Edita `database/db.py` y asegúrate de que esta línea esté así:

```python
DATABASE_URL = "postgresql+pg8000://user:password@localhost/todo_db"
```

> Recuerda poner tu usuario y contraseña de postgre
> Usamos el driver `pg8000` en lugar de `psycopg2`.

---

## 🔄 Migraciones

### 1. Inicializa Alembic (si no está hecho)

```bash
alembic init alembic
```

### 2. Configura Alembic

- En `alembic.ini` revisa:

  ```ini
  sqlalchemy.url = postgresql+pg8000://user:password@localhost/todo_db
  ```

  ► Si tienes un usuario distino a postgres y root recuerda cambiarlo

- En `alembic/env.py`, importa el modelo y apunta a los metadatos:

  ```python
  from database.db import Base
  from models.task_model import Task
  target_metadata = Base.metadata
  ```

### 3. Crea y aplica la migración

```bash
alembic revision --autogenerate -m "crear tabla tasks"
alembic upgrade head
```

---

## 🚀 Ejecutar la aplicación

Lanza el menú desde la raíz del proyecto:

```bash
python main.py
```

Y verás:

```
--- MENÚ TO-DO LIST ---
1. Crear tarea
2. Ver todas las tareas
3. Ver tarea por ID
4. Actualizar tarea
5. Eliminar tarea
6. Salir
```

---

## 🧠 Estructura del proyecto

```
todo_list/
│
├── alembic/              # Archivos de migración
├── controllers/          # Lógica de negocio (CRUD)
├── database/             # Conexión a la DB
├── models/               # Definición de modelos
├── seed/                 # Población inicial de BBDD
SQLAlchemy
├── views/                # Interfaz por consola
│
├── main.py
├── alembic.ini
├── requirements.txt
├── README.md
```

---

## 🧹 Notas finales

- No necesitas frontend, puedes ver la salida por consola.
- El objetivo es entender cómo se estructura un proyecto con MVC y SQLAlchemy.

¡Disfruta programando! 🐍✨
