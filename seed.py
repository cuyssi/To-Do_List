import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Cargar .env
load_dotenv()

# Datos de conexión
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Usamos pg8000 como driver
DATABASE_URL = f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Configuración de SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Modelo real según vuestra base
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    state = Column(String, default="pendiente")

    def __repr__(self):
        return f"<Task(title='{self.title}', state='{self.state}')>"

# Crear tablas si no existen (no borra nada)
Base.metadata.create_all(bind=engine)

# Insertar datos si aún no hay tareas
db = SessionLocal()

if db.query(Task).count() == 0:
    tareas = [
        Task(title="Preparar la entrega", description="Subir repo a Simplon", state="pendiente"),
        Task(title="Hacer presentación", description="Explicar MTV clarito", state="en progreso"),
        Task(title="Revisar README", description="Meter todo lo del script", state="hecho")
    ]
    db.add_all(tareas)
    db.commit()
    print("✅ Tareas de ejemplo insertadas correctamente.")
else:
    print("⚠️ Ya hay tareas en la base de datos. No se insertaron duplicados.")

db.close()