from typing import Optional
from sqlmodel import Field, SQLModel

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    email: str
    rol: str = "operario"  # Valores: operario, admin, gerente