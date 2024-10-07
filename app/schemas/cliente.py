from pydantic import BaseModel
from typing import Optional

class Cliente(BaseModel):
    id: Optional[int] = 1
    nombre: str
    apellidos: str
    ciudad: str
    saldo: Optional[int] = 500000  
    email: Optional[str] = None  