# Projeto: Aprendendo a Consumir APIs de LLM

## Objetivo
Aprender a integrar e consumir uma API de LLM (Large Language Model) em Python,
começando do zero de forma didática para uso no trabalho.

## API Escolhida
**Google Gemini** — modelo `gemini-3.5-flash`

**Por que Gemini?**
- Plano gratuito generoso
- Fácil de configurar
- Boa documentação oficial

## Roadmap do Projeto

### Etapa 1 — Setup + primeiro script ✓
- [x] Escolher a API (Gemini)
- [x] Criar API key no Google AI Studio
- [x] Configurar projeto Python (estrutura, dependências, .env)
- [x] Primeiro script: prompt fixo → resposta da LLM
- [x] Subir projeto no GitHub

### Etapa 2 — Input pelo terminal (próxima)
- [ ] Usuário digita a pergunta no terminal em vez de estar fixa no código
- [ ] Loop para continuar conversando sem precisar rodar o script de novo
- [ ] Comando para sair (ex: digitar "sair")

### Etapa 3 — Memória (histórico de conversa)
- [ ] Modelo se lembra do que foi dito antes na mesma sessão
- [ ] Entender o conceito de multi-turn (conversa com contexto)
- [ ] Implementar histórico de mensagens

### Etapa 4 — Interface Web
- [ ] Backend com Flask (Python) servindo uma rota `/chat`
- [ ] Frontend com HTML/CSS/JS (usuário conhece bem HTML/CSS)
- [ ] JavaScript com `fetch()` para chamar o backend
- [ ] Chat visual no navegador em `http://localhost:5000`

### Etapa 5 — Multi-agentes
- [ ] Entender o conceito de agentes especializados
- [ ] Agente 1: recebe o prompt do usuário e gera uma resposta especializada
- [ ] Agente 2: pega a resposta do Agente 1 e a processa/melhora
- [ ] Orquestrador: coordena o fluxo entre os agentes

## Status Atual
**Etapa 1 concluída.** Próxima: Etapa 2 — input pelo terminal.

## Detalhes técnicos descobertos
- Modelo em uso: `gemini-3.5-flash` (configurado via `.env`)
- Biblioteca: `google-genai` (a nova, oficial)
- Chave da API: formato `AQ.` (diferente do padrão `AIza`, mas funciona)

## Estrutura do Projeto
```
test-api-gemini/
├── app.py                  ← servidor Flask (Etapa 4)
├── templates/
│   └── index.html          ← interface web (Etapa 4)
├── static/
│   ├── style.css
│   └── script.js
├── src/
│   ├── 01_hello_gemini.py  ← prompt fixo (Etapa 1 ✓)
│   ├── 02_terminal.py      ← input pelo terminal (Etapa 2)
│   ├── 03_memoria.py       ← histórico de conversa (Etapa 3)
│   └── 04_agentes.py       ← multi-agentes (Etapa 5)
├── PROJETO.md
├── README.md
├── .env
├── .env.example
├── .gitignore
└── requirements.txt
```

## Conceitos que Serão Aprendidos
- O que é uma API key e como usá-la com segurança
- Como instalar e usar o SDK do Gemini em Python
- O que é um `prompt` e como estruturá-lo
- Input do usuário e loops no terminal
- Como manter contexto de conversa (multi-turn)
- Backend com Flask e rotas HTTP
- Frontend se comunicando com backend via `fetch()` e JSON
- Arquitetura de multi-agentes com LLMs

## Notas de Aula
_(serão adicionadas conforme o projeto avança)_
