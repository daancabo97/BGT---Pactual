from pymongo import MongoClient
from app.config import MONGO_URI


client = MongoClient(MONGO_URI)
db = client.BTG  

# Colecciones de la base de datos
clientes_collection = db["clientes"]
productos_collection = db["productos"]
inscripciones_collection = db["inscripciones"]
sucursales_collection = db["sucursales"]
disponibilidad_collection = db["disponibilidad"]
visitan_collection = db["visitan"]
transacciones_collection = db["transacciones"]
