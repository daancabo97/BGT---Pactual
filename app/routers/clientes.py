from fastapi import APIRouter, HTTPException
from app.database import clientes_collection
from app.schemas.cliente import Cliente
from bson import ObjectId

router = APIRouter()


def cliente_serializer(cliente) -> dict:
    """Convierte los ObjectId y limpia el campo _id."""
    cliente["id"] = str(cliente["_id"])
    cliente["_id"] = str(cliente["_id"])
    del cliente["_id"]
    return cliente


@router.get("/clientes/")
async def obtener_clientes():
    clientes = list(clientes_collection.find())
    clientes_serializados = [cliente_serializer(cliente) for cliente in clientes]
    return clientes_serializados


@router.post("/clientes/")
async def crear_cliente(cliente: Cliente):
    cliente_dict = cliente.dict()
    resultado = clientes_collection.insert_one(cliente_dict)
    cliente_dict["_id"] = str(resultado.inserted_id)
    cliente_dict["id"] = str(resultado.inserted_id) 
    return {"id": cliente_dict["id"]}


@router.get("/clientes/{id}")
async def obtener_cliente(id: str):
    cliente = clientes_collection.find_one({"_id": ObjectId(id)})
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente_serializer(cliente)


@router.put("/clientes/{id}")
async def actualizar_saldo(id: str, nuevo_saldo: int):
    resultado = clientes_collection.update_one({"_id": ObjectId(id)}, {"$set": {"saldo": nuevo_saldo}})
    if resultado.modified_count == 0:
        raise HTTPException(status_code=404, detail="Cliente no encontrado o saldo no actualizado")
    return {"mensaje": "Saldo actualizado correctamente"}
