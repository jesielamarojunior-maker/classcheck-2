import pymongo
import os
import csv
from bson import json_util
from dotenv import load_dotenv

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL") or "mongodb+srv://jesielamarojunior_db_user:admin123@cluster0.vuho6l7.mongodb.net/IOS-SISTEMA-CHAMADA?retryWrites=true&w=majority"
DB_NAME = os.getenv("DB_NAME") or "IOS-SISTEMA-CHAMADA"

client = pymongo.MongoClient(MONGO_URL)
db = client[DB_NAME]

# Buscar alunos
alunos = list(db["alunos"].find())
# Indexar alunos por id para facilitar merge
alunos_dict = {a["id"]: a for a in alunos}

# Buscar frequências (attendances)
frequencias = list(db["attendances"].find())

# Montar linhas para o CSV
linhas = []
for freq in frequencias:
    turma_id = freq.get("turma_id")
    data = freq.get("data")
    for rec in freq.get("records", []):
        aluno_id = rec.get("aluno_id")
        aluno = alunos_dict.get(aluno_id, {})
        linha = {
            "data": data,
            "turma_id": turma_id,
            "aluno_id": aluno_id,
            "nome_aluno": aluno.get("nome", ""),
            "cpf": aluno.get("cpf", ""),
            "data_nascimento": aluno.get("data_nascimento", ""),
            "presente": rec.get("presente"),
            "nota": rec.get("nota"),
        }
        linhas.append(linha)

# Escrever CSV
with open("frequencias_com_alunos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=linhas[0].keys())
    writer.writeheader()
    writer.writerows(linhas)

print("Arquivo frequencias_com_alunos.csv gerado com sucesso!")
