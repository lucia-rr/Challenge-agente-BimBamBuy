import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import FAISS

# Cargamos variables de entorno para la API KEY
load_dotenv()

# 1. Definimos las rutas
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "..", "data")
db_path = os.path.join(base_dir, "..", "db", "faiss_index")

# Archivos PDF de BimBam Buy
pdfs = [
    "pf_metodo_pago.pdf",
    "manual_garantia.pdf"
]

# 2. Cargamos todos los PDFs
print("📄 Cargando documentos de BimBam Buy...")
documentos = []
for pdf in pdfs:
    ruta_pdf = os.path.join(data_dir, pdf)
    print(f"  → Leyendo: {pdf}")
    loader = PyPDFLoader(ruta_pdf)
    documentos.extend(loader.load())

print(f"✅ Total de páginas cargadas: {len(documentos)}")

# 3. Dividimos el texto en fragmentos
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
documentos_divididos = text_splitter.split_documents(documentos)
print(f"📦 Documento dividido en {len(documentos_divididos)} fragmentos.")

# 4. CONFIGURACIÓN COHERE
print("🧠 Generando embeddings con Cohere...")
embeddings = CohereEmbeddings(model="embed-multilingual-v3.0")

# 5. Guardado en FAISS
db = FAISS.from_documents(documentos_divididos, embeddings)
db.save_local(db_path)
print(f"💾 Base de datos vectorial creada en: {db_path}")