from models.task_model import Task
from database.db import SessionLocal

def create_task(title, description, state="pendiente"):
    db = SessionLocal()
    try:
        new_task = Task(title=title, description=description, state=state)
        db.add(new_task)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"\033[91m🚩 Atención!\033[0m Error al crear la tarea: {e}")
    finally:
        db.close()


def get_all_tasks():
    db = SessionLocal()
    try:
        return db.query(Task).order_by(Task.id).all()
    except Exception as e:
        print(f"\033[91m🚩 Atención!\033[0m Error al obtener las tareas: {e}")
        return []
    finally:
        db.close()


def get_one(task_id):
    db = SessionLocal()
    try:
        return db.query(Task).get(task_id)
    except Exception as e:
        print(f"\033[91m🚩 Atención!\033[0m Error al obtener la tarea: {e}")
        return None
    finally:
        db.close()

def update_task(task_id, title=None, description=None, state=None):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise ValueError("\033[91m🚩 Atención!\033[0mTask not found")
    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    if state is not None:
        task.state = state
    db.commit()
    db.close()

def delete(id):
    db = SessionLocal()
    task = db.query(Task).get(id)
    if task is None:
        print("\033[91m🚩 Atención!\033[0mNo se encontró la tarea con ese ID.")
        db.close()
        return
    db.delete(task)
    db.commit()
    db.close()
