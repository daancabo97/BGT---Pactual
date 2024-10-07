from pydantic import BaseModel

class Sucursal(BaseModel):
    nombre: str
    ciudad: str
