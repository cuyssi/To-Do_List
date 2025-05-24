import sys
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'To-do_list')))

from views.task_view import menu # type: ignore 

if __name__ == "__main__" :   
    # Llamamos a la función menu() desde el módulo task_view
    # para iniciar la aplicación de To-Do List.
    # Esto permite que el usuario interactúe con el menú y realice acciones.    

    menu()  
