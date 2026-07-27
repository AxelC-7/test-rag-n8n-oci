# BotLog - Chatbot RAG para Empresa de Logística

## Descripción

BotLog es un chatbot para Telegram desarrollado en Python que responde consultas sobre una empresa de logística utilizando información contenida en un documento PDF.

El proyecto utiliza la técnica **RAG (Retrieval-Augmented Generation)** para recuperar la información más relevante del documento antes de generar una respuesta con Google Gemini.

---

## Características

* Chatbot para Telegram.
* Integración con Google Gemini.
* Búsqueda semántica mediante ChromaDB.
* Indexación automática de documentos PDF.
* Despliegue mediante Docker.
* Configuración mediante variables de entorno.

---

## Tecnologías utilizadas

* Python 3.13
* Google Gemini API
* LangChain
* ChromaDB
* python-telegram-bot
* Docker
* Docker Compose

---

## Estructura del proyecto

```text
BotLog/
│
├── bot_telegram.py        # Bot de Telegram
├── rag.py                 # Lógica RAG
├── ingest.py              # Indexación del PDF
├── config.py              # Variables de entorno
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
│
├── documentos/
│   └── empresa.pdf
│
└── chroma_db/
```

---

## Configuración

Crear un archivo `.env`:

```env
GOOGLE_API_KEY=TU_API_KEY
TELEGRAM_TOKEN=TU_TOKEN
```

---

## Instalación

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual:

### Windows

```bash
.venv\Scripts\activate
```

### Linux

```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Indexar el documento

Después de colocar el PDF dentro de la carpeta `documentos`, ejecutar:

```bash
python ingest.py
```

Este proceso:

* Lee el PDF.
* Divide el texto en fragmentos.
* Genera embeddings.
* Guarda la base vectorial en ChromaDB.

---

## Ejecutar el bot

```bash
python bot_telegram.py
```

---

## Despliegue con Docker

Construir la imagen:

```bash
docker compose build
```

Iniciar el contenedor:

```bash
docker compose up -d
```

Ver los logs:

```bash
docker logs -f botlog
```

Detener el servicio:

```bash
docker compose down
```

---

## Funcionamiento

1. El usuario envía un mensaje al bot de Telegram.
2. El bot busca los fragmentos más relevantes en ChromaDB.
3. Se envía el contexto recuperado a Google Gemini.
4. Gemini genera una respuesta basada exclusivamente en la información del documento.
5. El bot devuelve la respuesta al usuario.

---

## Variables de entorno

| Variable       | Descripción               |
| -------------- | ------------------------- |
| GOOGLE_API_KEY | API Key de Google Gemini  |
| TELEGRAM_TOKEN | Token del Bot de Telegram |

---

## Notas

* El archivo `.env` no debe subirse al repositorio.
* La carpeta `chroma_db` puede regenerarse ejecutando `ingest.py`.
* El PDF utilizado puede sustituirse por otro para actualizar la base de conocimiento.

---

## Autor

Axel C.
