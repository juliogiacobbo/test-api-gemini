# Projeto: Aprendendo a Consumir APIs de LLM

## Objetivo
Aprender a integrar e consumir uma API de LLM (Large Language Model) em Python,
começando do zero de forma didática para uso no trabalho.

## API Escolhida
**Google Gemini** — modelo `gemini-1.5-flash`

**Por que Gemini?**
- Plano gratuito generoso: 1.500 requisições/dia
- Fácil de configurar
- Boa documentação oficial

## Roadmap do Projeto

### Etapa 1 — Setup inicial (concluída ✓)
- [x] Escolher a API (Gemini)
- [x] Criar API key no Google AI Studio (https://aistudio.google.com)
- [x] Configurar projeto Python (estrutura de pastas, dependências)
- [x] Criar `.env` com a chave da API e nome do modelo
- [x] Primeiro script: prompt simples → resposta da LLM

### Etapa 2 — Evoluindo o projeto
- [ ] Adicionar histórico de conversa (multi-turn)
- [ ] Parâmetros de geração (temperatura, tokens)
- [ ] Tratamento de erros da API

### Etapa 3 — Casos de uso práticos
- [ ] Resumo de textos
- [ ] Classificação de textos
- [ ] Geração de conteúdo estruturado (JSON)

## Status Atual
**Etapa 1 concluída.** Próximo: Etapa 2 — histórico de conversa e parâmetros de geração.

## Detalhes técnicos descobertos
- Modelo em uso: `gemini-3.5-flash` (configurado via `.env`)
- Biblioteca: `google-genai` (a nova, oficial)
- Chave da API: formato `AQ.` (diferente do padrão `AIza`, mas funciona)

## Estrutura Planejada do Projeto
```
test-api-gemini/
├── PROJETO.md          ← este arquivo
├── .env                ← chave da API (não versionar!)
├── .gitignore
├── requirements.txt
└── src/
    ├── 01_hello_gemini.py      ← prompt simples
    ├── 02_conversa.py          ← multi-turn
    └── 03_casos_de_uso.py      ← exemplos práticos
```

## Conceitos que Serão Aprendidos
- O que é uma API key e como usá-la com segurança
- Como instalar e usar o SDK do Gemini em Python
- O que é um `prompt` e como estruturá-lo
- O que são parâmetros de geração (temperatura, max_tokens)
- Como manter contexto de conversa

## Notas de Aula
_(serão adicionadas conforme o projeto avança)_
