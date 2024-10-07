from fastapi import APIRouter, HTTPException
from app.database import inscripciones_collection
from app.schemas.inscripcion import Inscripcion

router = APIRouter()


@router.post("/inscripciones/")
async def crear_inscripcion(inscripcion: Inscripcion):
    inscripcion_id = inscripciones_collection.insert_one(inscripcion.dict()).inserted_id
    return {"id": str(inscripcion_id)}
