# 🤖 Test API Gemini

Projeto didático em Python para aprender a consumir a API do Google Gemini (LLM).
Você faz uma pergunta e a inteligência artificial responde.

---

## Pré-requisitos

Antes de começar, você precisa ter instalado no seu computador:

- [Python 3.9 ou superior](https://www.python.org/downloads/)
  - Durante a instalação, marque a opção **"Add Python to PATH"**
- [Git](https://git-scm.com/downloads)
- Uma conta Google para criar a chave de API (gratuita)

---

## Passo 1 — Clonar o projeto

Abra o terminal (Prompt de Comando, PowerShell ou Git Bash) e rode:

```bash
git clone https://github.com/SEU_USUARIO/test-api-gemini.git
cd test-api-gemini
```

> Substitua `SEU_USUARIO` pelo seu usuário do GitHub.

---

## Passo 2 — Criar o ambiente virtual

O ambiente virtual isola as dependências deste projeto para não conflitar com outros projetos do seu computador.

```bash
py -m venv .venv
```

Depois, ative o ambiente:

- **Windows (Git Bash):**
  ```bash
  source .venv/Scripts/activate
  ```
- **Windows (PowerShell ou CMD):**
  ```bash
  .venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source .venv/bin/activate
  ```

Quando ativado, você verá `(.venv)` no início da linha do terminal.

---

## Passo 3 — Instalar as dependências

Com o ambiente virtual ativado, rode:

```bash
pip install -r requirements.txt
```

---

## Passo 4 — Criar sua chave de API do Gemini

1. Acesse [aistudio.google.com](https://aistudio.google.com) e faça login com sua conta Google
2. No menu lateral, clique em **"Get API key"**
3. Clique em **"Create API key"**
4. Copie a chave gerada

> **Importante:** nunca compartilhe sua chave de API publicamente.

---

## Passo 5 — Configurar o arquivo `.env`

Na raiz do projeto, copie o arquivo de exemplo:

```bash
cp .env.example .env
```

Abra o arquivo `.env` em qualquer editor de texto e preencha com sua chave:

```
GEMINI_API_KEY=cole_sua_chave_aqui
GEMINI_MODEL_NAME=gemini-3.5-flash
```

---

## Passo 6 — Rodar o projeto

```bash
py src/01_hello_gemini.py
```

Você verá a resposta do Gemini no terminal. 🎉

---

## Estrutura do projeto

```
test-api-gemini/
├── src/
│   └── 01_hello_gemini.py   # Script principal
├── .env                     # Suas credenciais (não versionar)
├── .env.example             # Modelo do arquivo .env
├── .gitignore               # Arquivos ignorados pelo Git
├── requirements.txt         # Dependências do projeto
└── README.md                # Este arquivo
```

---

## Solução de problemas comuns

| Erro | Solução |
|---|---|
| `pip: command not found` | Use `py -m pip install -r requirements.txt` |
| `ModuleNotFoundError` | Verifique se o ambiente virtual está ativado (`(.venv)` no terminal) |
| `RESOURCE_EXHAUSTED (429)` | Troque o modelo no `.env` por outro da lista disponível |
| `API key not valid` | Verifique se a chave no `.env` foi colada corretamente |

---

## Modelos disponíveis

Se o modelo padrão não funcionar, troque o valor de `GEMINI_MODEL_NAME` no `.env` por um dos modelos abaixo:

- `gemini-3.5-flash` ← recomendado
- `gemini-2.0-flash`
- `gemini-2.0-flash-lite`

---

## Licença

Projeto para fins educacionais.
