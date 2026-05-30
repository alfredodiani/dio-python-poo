# dio-python-poo

Repositório de estudos em **Python (Back-end)** desenvolvido durante a trilha da **DIO (Digital Innovation One)** em parceria com o **Luizalabs/Magalu**.

> Objetivo: registrar a evolução no aprendizado de Python e boas práticas de Back-end, com exercícios, desafios e pequenos projetos.

## Conteúdos do repositório
Este repositório contém, principalmente:

- Exercícios e anotações de **Python**
- Exemplos de **Programação Orientada a Objetos (POO)**
- Desafios práticos propostos na trilha (ex.: projetos de sistema bancário / API)

> Observação: a estrutura pode evoluir conforme novos módulos e desafios forem concluídos.

## Tecnologias
- **Python** (100%)

## Como executar (geral)
Este repositório contém **múltiplos projetos/pastas**. Para os módulos que possuem `pyproject.toml`, a forma recomendada de rodar é usando **Poetry**.

### Pré-requisitos
- Python instalado (os projetos 09 e 11 estão configurados com `requires-python = ">=3.13"` no `pyproject.toml`)
- Poetry instalado

> Dica: para garantir que o Poetry use a versão correta do Python:
> 
> ```bash
> poetry env use 3.13
> ```

### Rodando com Poetry (módulos 09 e 11)

#### 09 — APIs Assíncronas com FastAPI (dio-blog)
Pasta:

```bash
cd 09_apis_assincronas_com_fastapi/dio-blog
```

Instalar dependências (via `pyproject.toml`):

```bash
poetry install
```

Subir a API com Uvicorn:

```bash
poetry run uvicorn src.main:app --reload
```

#### 11 — Desafio API (API Bancária)
Pasta:

```bash
cd 11_desafio_api
```

Instalar dependências (via `pyproject.toml`):

```bash
poetry install
```

Subir a API com Uvicorn:

```bash
poetry run uvicorn src.main:app --reload
```

> Observação: este desafio pode depender de variáveis de ambiente definidas em um arquivo `.env` (ver `src/config.py`).

## READMEs internos
Alguns desafios têm README próprio dentro da pasta (por exemplo, `11_desafio_api/README.md`). Se existir, consulte-o para instruções e requisitos específicos.

---

Se você encontrar algum problema ou tiver sugestões de melhoria, fique à vontade para abrir uma issue.
