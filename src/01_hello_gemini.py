import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

cliente = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def perguntar_ao_gemini(prompt):
    try:
        resposta = cliente.models.generate_content(
            model=os.getenv("GEMINI_MODEL_NAME", "gemini-3.5-flash"),
            contents=prompt
        )
        return resposta.text
    except Exception as e:
        return f"Erro ao consultar a API: {e}"

meu_prompt = "Qual é a capital da França?"
resultado = perguntar_ao_gemini(meu_prompt)

print("--- Resposta do Gemini ---")
print(resultado)
