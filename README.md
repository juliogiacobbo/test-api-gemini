# Test API Gemini

Projeto didático em Python para aprender a consumir a API do Google Gemini (LLM).
Você faz uma pergunta e a inteligência artificial responde.

---

## Objetivo

Aprender a integrar e consumir uma API de LLM (Large Language Model) em Python,
começando do zero de forma didática para uso no trabalho.

**API escolhida:** Google Gemini — modelo `gemini-2.0-flash`

**Por que Gemini?**
- Plano gratuito generoso
- Fácil de configurar
- Boa documentação oficial

---

## Roadmap

### Etapa 1 — Setup + primeiro script ✅
- [x] Escolher a API (Gemini)
- [x] Criar API key no Google AI Studio
- [x] Configurar projeto Python (estrutura, dependências, .env)
- [x] Primeiro script: prompt fixo → resposta da LLM
- [x] Subir projeto no GitHub

### Etapa 2 — Input pelo terminal 🔄
- [ ] Usuário digita a pergunta no terminal em vez de estar fixa no código
- [ ] Loop para continuar conversando sem precisar rodar o script de novo
- [ ] Comando para sair (ex: digitar "sair")

### Etapa 3 — Memória (histórico de conversa) ⏳
- [ ] Modelo se lembra do que foi dito antes na mesma sessão
- [ ] Entender o conceito de multi-turn (conversa com contexto)
- [ ] Implementar histórico de mensagens

### Etapa 4 — Interface Web ⏳
- [ ] Backend com Flask (Python) servindo uma rota `/chat`
- [ ] Frontend com HTML/CSS/JS
- [ ] JavaScript com `fetch()` para chamar o backend
- [ ] Chat visual no navegador em `http://localhost:5000`

### Etapa 5 — Multi-agentes ⏳
- [ ] Entender o conceito de agentes especializados
- [ ] Agente 1: recebe o prompt do usuário e gera uma resposta especializada
- [ ] Agente 2: pega a resposta do Agente 1 e a processa/melhora
- [ ] Orquestrador: coordena o fluxo entre os agentes

---

## Metodologia: Test-Driven Development (TDD)

O projeto segue o ciclo TDD em toda nova funcionalidade:

1. **Red** — escrever um teste que falha (a feature ainda não existe)
2. **Green** — implementar o mínimo de código para o teste passar
3. **Refactor** — melhorar o código sem quebrar os testes

Os testes ficam na pasta `tests/` e são executados com `pytest`.
A cada push no GitHub, o GA roda os testes automaticamente.

**Rodando os testes localmente:**

```bash
# rodar todos os testes
pytest

# rodar com detalhes (ver nome de cada teste)
pytest -v

# rodar apenas um arquivo de teste
pytest tests/test_terminal.py -v
```

> Os testes usam mocks — não chamam a API real e não precisam do `.env`.

---

## Conceitos que Serão Aprendidos

- O que é uma API key e como usá-la com segurança
- Como instalar e usar o SDK do Gemini em Python
- O que é um `prompt` e como estruturá-lo
- Input do usuário e loops no terminal
- Como manter contexto de conversa (multi-turn)
- Backend com Flask e rotas HTTP
- Frontend se comunicando com backend via `fetch()` e JSON
- Arquitetura de multi-agentes com LLMs

---

## Estrutura do Projeto

```
test-api-gemini/
├── .github/
│   └── workflows/
│       └── tests.yml       ← GitHub Actions (roda os testes automaticamente)
├── src/
│   ├── 01_hello_gemini.py  ← prompt fixo (Etapa 1 ✅)
│   ├── 02_terminal.py      ← input pelo terminal (Etapa 2)
│   ├── 03_memoria.py       ← histórico de conversa (Etapa 3)
│   └── 04_agentes.py       ← multi-agentes (Etapa 5)
├── tests/                  ← testes automatizados (pytest)
├── app.py                  ← servidor Flask (Etapa 4)
├── templates/
│   └── index.html          ← interface web (Etapa 4)
├── static/
│   ├── style.css
│   └── script.js
├── CLAUDE.md               ← instruções para o Claude Code
├── README.md               ← este arquivo
├── .env                    ← suas credenciais (não versionar)
├── .env.example            ← modelo do arquivo .env
├── .gitignore
└── requirements.txt
```

---

## Pré-requisitos

- [Python 3.9 ou superior](https://www.python.org/downloads/)
  - Durante a instalação, marque a opção **"Add Python to PATH"**
- [Git](https://git-scm.com/downloads)
- Uma conta Google para criar a chave de API (gratuita)

---

## Instalação

**1. Clonar o projeto**

```bash
git clone https://github.com/SEU_USUARIO/test-api-gemini.git
cd test-api-gemini
```

**2. Criar o ambiente virtual**

```bash
py -m venv .venv
```

Ativar o ambiente:

- Windows (PowerShell): `.venv\Scripts\activate`
- Windows (Git Bash): `source .venv/Scripts/activate`
- Mac/Linux: `source .venv/bin/activate`

Quando ativado, você verá `(.venv)` no início da linha do terminal.

**3. Instalar as dependências**

```bash
pip install -r requirements.txt
```

**4. Criar sua chave de API do Gemini**

1. Acesse [aistudio.google.com](https://aistudio.google.com) e faça login com sua conta Google
2. No menu lateral, clique em **"Get API key"**
3. Clique em **"Create API key"**
4. Copie a chave gerada

> **Importante:** nunca compartilhe sua chave de API publicamente.

**5. Configurar o arquivo `.env`**

```bash
cp .env.example .env
```

Abra o `.env` e preencha com sua chave:

```
GEMINI_API_KEY=cole_sua_chave_aqui
GEMINI_MODEL_NAME=gemini-2.0-flash
```

**6. Rodar o primeiro script**

```bash
py src/01_hello_gemini.py
```

---

## Solução de Problemas

| Erro | Solução |
|---|---|
| `pip: command not found` | Use `py -m pip install -r requirements.txt` |
| `ModuleNotFoundError` | Verifique se o ambiente virtual está ativado (`(.venv)` no terminal) |
| `RESOURCE_EXHAUSTED (429)` | Troque o modelo no `.env` por outro da lista abaixo |
| `API key not valid` | Verifique se a chave no `.env` foi colada corretamente |

**Modelos disponíveis** (para trocar no `.env`):
- `gemini-2.0-flash` ← recomendado
- `gemini-2.0-flash-lite`
- `gemini-1.5-flash`

---

## Notas de Aula

_(serão adicionadas conforme o projeto avança)_

---

## Licença

Projeto para fins educacionais.
