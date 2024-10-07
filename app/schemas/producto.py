from pydantic import BaseModel
from typing import Optional

class Producto(BaseModel):
    id: Optional[str]
    nombre: str
    monto_minimo: int
    categoria: str
