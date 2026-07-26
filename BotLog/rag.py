from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from google import genai

from config import GOOGLE_API_KEY


embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=GOOGLE_API_KEY
)


db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)


client = genai.Client(api_key=GOOGLE_API_KEY)


def preguntar(pregunta):

    resultados = db.similarity_search(
        pregunta,
        k=3
    )

    if not resultados:
        return "No tengo información disponible sobre ese tema en la documentación."


    contexto = "\n\n".join(
        [doc.page_content for doc in resultados]
    )


    prompt = f"""
Eres un asistente de una empresa de logística.

Reglas importantes:
- Responde únicamente usando la información proporcionada.
- No inventes datos.
- Si la información no aparece, responde:
"No tengo información disponible sobre ese tema en la documentación."

Documento:
{contexto}

Pregunta:
{pregunta}
"""


    respuesta = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )


    return respuesta.text