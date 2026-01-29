import pymongo
import os
from pprint import pprint

# Carregar variáveis do .env (opcional, se rodar no mesmo diretório)
from dotenv import load_dotenv
load_dotenv()

MONGO_URL = os.getenv("MONGO_URL") or "mongodb+srv://jesielamarojunior_db_user:admin123@cluster0.vuho6l7.mongodb.net/IOS-SISTEMA-CHAMADA?retryWrites=true&w=majority"
DB_NAME = os.getenv("DB_NAME") or "IOS-SISTEMA-CHAMADA"

client = pymongo.MongoClient(MONGO_URL)
db = client[DB_NAME]

print(f"Conectado ao banco: {DB_NAME}")
print("Coleções disponíveis:")
print(db.list_collection_names())

for collection_name in db.list_collection_names():
    print(f"\n--- Primeiros documentos da coleção: {collection_name} ---")
    for doc in db[collection_name].find().limit(3):
        pprint(doc)
