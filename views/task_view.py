import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.task_controller import create_task
from controllers.task_controller import get_all_tasks
from controllers.task_controller import update_task
from controllers.task_controller import get_one
from controllers.task_controller import delete
from models.task_model import Task


def show_menu():
    return """
    --- \033[35mMENÚ TO-DO LIST\033[0m ---
\033[94m1. Crear tarea
2. Ver todas las tareas
3. Ver tarea por ID
4. Actualizar tarea
5. Eliminar tarea
6. Salir\033[0m
\033[32mElige una opción:\033[0m """

# Validamos que el ID ingresado sea un número entero válido

def input_task_id():
    """
    Pide al usuario que ingrese un ID y valida que sea un entero.
    Retorna el ID como entero o None si la entrada no es válida.
    """
    try:
        return int(input("\033[92mIntroduce el ID de la tarea:\033[0m "))
    except ValueError:
        print("\033[91m🚩 Atención!\033[0mDebes introducir un número válido.")
        return None

# Verificamos que una tarea exista antes de modificarla o eliminarla
def validate_task_exists(task_id):
    """
    Verifica que exista una tarea con el ID dado.
    Retorna la tarea si existe, o None si no.
    """
    task = get_one(task_id)
    if not task:
        print("\033[91m🚩 Atención!\033[0mNo existe una tarea con ese ID.")
        return None
    return task

def get_task_for_id():
    """
    Función reutilizable para pedir el ID de una tarea y validar que exista.
    Retorna una tupla (task_id, task) si es válido, o (None, None) si no.
    """
    task_id = input_task_id()
    if task_id is None:
        return None, None
    task = validate_task_exists(task_id)
    if not task:
        return None, None
    return task_id, task


def create_view():
    title = input("\033[35mNombre de la tarea que quieres agregar?:\033[0m ")
    description = input("\033[35mDescribela:\033[0m ")
    if not title:
        print("\033[91m🚩 Atención!\033[0mEl nombre no puede estar vacío.")
        return
    create_task(title, description)
    print("\033[45m✅ Tarea creada correctamente!\033[0m")

def show_tasks():
    tasks = get_all_tasks()
    if not tasks:
        print("\033[91m🚩 Atención!\033[0mNo hay tareas registradas.")
    for task in tasks:
        print(task)

def show_one_task():
    _, task = get_task_for_id()
    if task:
        print(task)

def menu_update():
    return """
---\033[35mQué quieres modificar?\033[0m---
\033[94m1.Modificar titulo de tarea
2.Modificar descripcion de tarea
3.Modificar estado de la tarea\033[0m
\033[32mElige una opción:\033[0m """

def options_update():
    """Gestiona la actualización de campos de una tarea existente."""
    task_id, task = get_task_for_id()
    if not task:
        return
    option = input(menu_update())
    if option not in ["1", "2", "3"]:
        print("\033[91m🚩 Atención!\033[0mOpcion invalida.")
        return
    campos = {
        "1": ("titulo", "title"),
        "2": ("descripción", "description"),
        "3": ("estado", "state")
    }
    etiqueta, campo = campos[option]
    nuevo_valor = input(f"\033[92mNuevo {etiqueta}:\033[0m ").strip()
    if not nuevo_valor:
        print(f"\033[91m🚩 Atención!\033[0mEl {etiqueta} no puede estar vacío.")
        return

    update_task(task_id, **{campo: nuevo_valor})
    print("\033[45m✅ Tarea actualizada correctamente.\033[0m")
    return
def delete_view():
    task_id, task = get_task_for_id()
    if task:
        delete(task_id)
        print("\033[45m✅ Tarea eliminada correctamente.\033[0m")


def menu():
    while True:
        option = input(show_menu())
        if option == "1":
            create_view()
        elif option == "2":
            show_tasks()
        elif option == "3":
            show_one_task()
        elif option == "4":
            options_update()
        elif option == "5":
            delete_view()
        elif option == "6":
            print("\033[35mHasta luego!\033[0m")
            break

menu()
