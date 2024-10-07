from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv(dotenv_path=".env")


MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "BTG") 


client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]


print(f"Conectando a MongoDB en: {MONGO_URI}")
print(f"Usando la base de datos: {DATABASE_NAME}")
