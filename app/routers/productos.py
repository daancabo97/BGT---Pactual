from fastapi import APIRouter, HTTPException
from app.database import productos_collection
from app.schemas.producto import Producto

router = APIRouter()


@router.get("/productos/")
async def obtener_productos():
    productos = list(productos_collection.find())
    return productos


@router.post("/productos/")
async def crear_producto(producto: Producto):
    producto_id = productos_collection.insert_one(producto.dict()).inserted_id
    return {"id": str(producto_id)}
