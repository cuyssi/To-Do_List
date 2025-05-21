from sqlalchemy import Column, Integer, String
from database.db import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    state = Column(String, default="pendiente")

    def __repr__(self):
        """
        Representación legible de una tarea, útil para imprimir por consola.
        """
        return (
            f"\033[95mTarea\033[0m {self.id}\n"
            f"\033[32mTítulo:\033[0m {self.title}\n"
            f"\033[32mDescripción:\033[0m {self.description}\n"
            f"\033[32mEstado:\033[0m {self.state}\n"
        )
