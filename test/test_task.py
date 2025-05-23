from models.task_model import Task  # importa tu clase Task real
from database.db import Base


def test_create_task(session):
    nueva = Task(title="Estudiar Django", description="Repasar arquitectura MTV", state="pendiente")
    session.add(nueva)
    session.commit()

    resultado = session.query(Task).filter_by(title="Estudiar Django").first()
    
    assert resultado is not None
    assert resultado.description == "Repasar arquitectura MTV"
    assert resultado.state == "pendiente"

def test_get_task_por_id(session):
    nueva = Task(title="Aprender testing", description="Hacer test con pytest", state="pendiente")
    session.add(nueva)
    session.commit()

    resultado = session.get(Task, nueva.id)

    assert resultado is not None
    assert resultado.title == "Aprender testing"

def test_update_task(session):
    nueva = Task(title="Aprender SQL", description="Repasar consultas SQL", state="pendiente")
    session.add(nueva)
    session.commit()

    # Actualizar la tarea
    nueva.title = "Aprender SQL Avanzado"
    session.commit()

    resultado = session.get(Task, nueva.id)

    assert resultado is not None
    assert resultado.title == "Aprender SQL Avanzado"

def test_delete_task(session):
    nueva = Task(title="Aprender SQL", description="Repasar consultas SQL", state="pendiente")
    session.add(nueva)
    session.commit()

    # Eliminar la tarea
    session.delete(nueva)
    session.commit()

    resultado = session.get(Task, nueva.id)

    assert resultado is None

# Test para listar tareas

def test_list_tasks(session):
    tarea1 = Task(title="Tarea 1", description="Descripción 1", state="pendiente")
    tarea2 = Task(title="Tarea 2", description="Descripción 2", state="completada")
    session.add(tarea1)
    session.add(tarea2)
    session.commit()

    resultado = session.query(Task).all()

    assert len(resultado) == 2
    assert resultado[0].title == "Tarea 1"
    assert resultado[1].title == "Tarea 2"


def test_list_tasks_vacia(session):
    resultado = session.query(Task).all()

    assert len(resultado) == 0


    


