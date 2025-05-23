# 📝Proyecto TODO List - Python Vanilla + PostgreSQL

Este proyecto es un ejemplo funcional de una aplicación de consola que permite gestionar tareas (CRUD) utilizando Python, arquitectura MVC, SQLAlchemy y PostgreSQL, sin frameworks.

📦 Requisitos previos

* Python 3.10 o superior
* PostgreSQL instalado
* Acceso a psql desde consola
* Git (opcional)

⚙️ Configuración inicial

1. Clona el repositorio (si es necesario)

```bash
git clone <url-del-repo>
cd todo_list
```

2.Crea y activa entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Linux/MacOS
venv\Scripts\activate    # En Windows
```

3.Instala las dependencias

```bash
pip install -r requirements.txt
```

🛠️ Base de datos

1. Crea la base de datos en PostgreSQL
   Usa este comando (fuera del entorno virtual):

```bash
psql -U postgres -c "CREATE DATABASE todo_db;"
```

Asegúrate de tener acceso a psql y que tu contraseña sea 1234.
Puedes modificarla en `.env` si estás usando variables de entorno.

🔐 Configuración con script automático
Hemos preparado un script para que no tengas que crear la base de datos manualmente:

1. Copia el archivo `.env.example` como `.env`

```bash
cp .env.example .env
```

2.Rellena tus credenciales de PostgreSQL en el archivo `.env`:

```DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
DB_NAME=todo_db
```

3.Ejecuta los scripts de inicialización:

```bash
python setup_db.py   # Crea la base de datos si no existe
python seed.py       # Rellena la tabla de tareas con datos de prueba
```

🔗 Conexión a PostgreSQL
La URL de conexión es generada automáticamente desde las variables del archivo `.env`.

🔄 Migraciones (opcional si usas los scripts anteriores)

1. Inicializa Alembic (si no está hecho)

```bash
alembic init alembic
```

2.Configura Alembic:

* En `alembic.ini`:

```sqlalchemy.url = postgresql+pg8000://postgres:1234@localhost/todo_db
```

* En `alembic/env.py`:

```python
from database.db import Base
from models.task_model import Task
target_metadata = Base.metadata
```

3.Crea y aplica la migración:

```bash
alembic revision --autogenerate -m "crear tabla tasks"
alembic upgrade head
```

🚀 Ejecutar la aplicación
Lanza el menú desde la raíz del proyecto:

```bash
python views/task_view.py
```

Y verás:

```--- MENÚ TO-DO LIST ---
1. Crear tarea
2. Ver todas las tareas
3. Ver tarea por ID
4. Actualizar tarea
5. Eliminar tarea
6. Salir
```

🧪 Pruebas automáticas
El proyecto incluye tests automáticos usando `pytest`. Están ubicados en la carpeta `test/`.

* Los tests utilizan una base de datos temporal para evitar tocar tus datos reales.
* Se comprueba que se pueden crear, obtener y actualizar tareas correctamente.

Para ejecutarlos:

```bash
pytest
```

🧠 Estructura del proyecto
todo\_list/
│
├── alembic/              # Archivos de migración
├── controllers/          # Lógica de negocio (CRUD)
├── database/             # Conexión a la DB
├── models/               # Definición de modelos SQLAlchemy
├── views/                # Interfaz por consola
├── test/                 # Pruebas con pytest
│
├── alembic.ini
├── requirements.txt
├── README.md

🧹 Notas finales

* No necesitas frontend, puedes ver la salida por consola.
* El objetivo es entender cómo se estructura un proyecto con MVC y SQLAlchemy.
* Los scripts `setup_db.py` y `seed.py` automatizan la preparación de tu entorno.

¡Disfruta programando! 🐍✨
