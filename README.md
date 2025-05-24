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

Asegúrate de tener acceso a psql.

🔐 Configuración con script automático
Hemos preparado un script para que no tengas que crear la base de datos manualmente:

1. Copia el archivo `.env.example` como `.env`

```bash
cp .env.example .env
```

2.Rellena tus credenciales de PostgreSQL en el archivo `.env` que creara al tirar ese comando:

```DB_USER=tu_usuario (suele ser postgres)
DB_PASSWORD=tu_contraseña (la contraseña de postgres)
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

🔄 Migraciones (opcional si no usas los scripts anteriores)

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
python main.py
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
To-Do_List/
├── controllers/             # Lógica de control (create, read, update, delete)
│   ├── init.py
│   └── task_controller.py
│
├── database/                # Configuración de la base de datos
│   ├── init.py
│   └── db.py
│
├── models/                  # Definición de modelos (clases de datos)
│   ├── init.py
│   └── task_model.py
│
├── test/                    # Pruebas unitarias (con pytest)
│   └── test_tasks.py
│
├── views/                   # Interfaz por consola (menú, inputs)
│   ├── init.py
│   └── task_view.py
│
├── .env                     # Variables de entorno (NO se sube al repo)
├── .env.example             # Plantilla para crear el .env
├── .gitignore               # Archivos/carpetas que Git debe ignorar
├── main.py                  # Punto de entrada del programa
├── requirements.txt         # Dependencias del proyecto
└── README.md

🧹 Notas finales

* No necesitas frontend, puedes ver la salida por consola.
* El objetivo es entender cómo se estructura un proyecto con MVC y SQLAlchemy.
* Los scripts `setup_db.py` y `seed.py` automatizan la preparación de tu entorno.

¡Disfruta programando! 🐍✨
