# CLAUDE.md

## Contexto do Projeto
Projeto de aprendizado de consumo de APIs de LLM em Python, do zero, para uso profissional.
API escolhida: Google Gemini (`gemini-2.0-flash`). Biblioteca: `google-genai`.

## Nível do Usuário
- Conhece bem HTML e CSS
- Python em nível intermediário
- Nunca trabalhou com APIs de LLM antes
- Objetivo: aprender para aplicar no trabalho

## Etapa Atual
**Etapa 2 — Input pelo terminal**
- Usuário digita a pergunta no terminal em vez de estar fixa no código
- Loop para continuar conversando sem rodar o script de novo
- Comando para sair (ex: digitar "sair")

## Roadmap Resumido
1. ✅ Setup + primeiro script (`src/01_hello_gemini.py`)
2. 🔄 Input pelo terminal (`src/02_terminal.py`)
3. ⏳ Memória / histórico de conversa (`src/03_memoria.py`)
4. ⏳ Interface Web com Flask (`app.py` + `templates/`)
5. ⏳ Multi-agentes (`src/04_agentes.py`)

## Metodologia
- **Test-Driven Development (TDD)**: escrever o teste antes do código de produção
- Ciclo: Red (teste falha) → Green (mínimo para passar) → Refactor
- Biblioteca de testes: `pytest` + `pytest-mock`
- Testes ficam em `tests/`, espelhando a estrutura de `src/`
- GitHub Actions roda `pytest tests/ -v` a cada push em `main`
- Testes NÃO chamam a API real — usar mocks para simular respostas do Gemini

## Como Colaborar
- Responder sempre em **português**
- Explicar o conceito antes de mostrar o código
- Abordagem passo a passo — não pular etapas
- Não introduzir bibliotecas ou padrões além do necessário para a etapa atual
- Código simples e legível, sem abstrações prematuras
