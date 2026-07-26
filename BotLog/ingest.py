from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config import GOOGLE_API_KEY


PDF_PATH = "documentos/Manual.pdf"


print("Leyendo PDF...")

loader = PyPDFLoader(PDF_PATH)
documents = loader.load()


print("Cantidad de páginas:", len(documents))


print("Dividiendo texto...")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)


print("Fragmentos creados:", len(chunks))


print("Creando embeddings...")


embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=GOOGLE_API_KEY
)


print("Guardando en ChromaDB...")


db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)


print("Proceso terminado correctamente")