import pymongo
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL") or "mongodb+srv://jesielamarojunior_db_user:admin123@cluster0.vuho6l7.mongodb.net/IOS-SISTEMA-CHAMADA?retryWrites=true&w=majority"
DB_NAME = os.getenv("DB_NAME") or "IOS-SISTEMA-CHAMADA"

client = pymongo.MongoClient(MONGO_URL)
db = client[DB_NAME]

colecoes = db.list_collection_names()

for colecao in colecoes:
    if colecao in ["usuarios", "users"]:
        continue
    print(f"Apagando todos os documentos da coleção: {colecao}")
    db[colecao].delete_many({})

print("Limpeza concluída. Apenas usuários mantidos.")
