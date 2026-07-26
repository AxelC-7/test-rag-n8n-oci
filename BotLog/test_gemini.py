from google import genai
from config import GOOGLE_API_KEY

try:
    print("Probando Gemini...")

    client = genai.Client(api_key=GOOGLE_API_KEY)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Explica en una frase qué hace una empresa de logística."
    )


    print(response.text)

except Exception as e:
    print("ERROR:")
    print(e)