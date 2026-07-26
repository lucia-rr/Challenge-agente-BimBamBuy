import os
from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

# Configuración centralizada de Embeddings
embeddings = CohereEmbeddings(model="embed-multilingual-v3.0")

def cargar_vector_store(ruta="db/faiss_index"):
    """Carga la base de datos existente para ser usada por consulta.py"""
    return FAISS.load_local(
        ruta,
        embeddings,
        allow_dangerous_deserialization=True
    )

def guardar_vector_store(documentos, ruta="db/faiss_index"):
    """Función para usar SOLAMENTE cuando ingestion.py prepare nuevos documentos."""
    db = FAISS.from_documents(documentos, embeddings)
    db.save_local(ruta)
    print(f"Base de datos actualizada en: {ruta}")