import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

cliente = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def perguntar_ao_gemini(prompt):
    resposta = cliente.models.generate_content(
        model=os.getenv("GEMINI_MODEL_NAME", "gemini-2.0-flash"),
        contents=prompt
    )
    return resposta.text


def main():
    print("Chat com Gemini — digite 'sair' para encerrar\n")
    while True:
        pergunta = input("Você: ")
        if pergunta.lower() == "sair":
            print("Encerrando...")
            break
        resposta = perguntar_ao_gemini(pergunta)
        print(f"\nGemini: {resposta}\n")


if __name__ == "__main__":
    main()
