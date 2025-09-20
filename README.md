# Ingestão e Busca Semântica com LangChain e PostgreSQL

Sistema de ingestão e busca semântica que processa documentos PDF e permite consultas via linha de comando utilizando tecnologias de Retrieval Augmented Generation (RAG).

## Descrição do Projeto

Este projeto implementa um sistema completo de ingestão e busca semântica com as seguintes funcionalidades:

- **Ingestão**: Processamento de arquivos PDF com divisão em chunks, geração de embeddings e armazenamento em banco vetorial PostgreSQL com extensão pgVector
- **Busca**: Interface de linha de comando para consultas semânticas baseadas exclusivamente no conteúdo do documento processado

## Tecnologias Utilizadas

- **Linguagem**: Python 3.10+
- **Framework**: LangChain
- **Banco de Dados**: PostgreSQL com extensão pgVector
- **Embeddings**: OpenAI text-embedding-3-small
- **LLM**: OpenAI gpt-5-nano
- **Containerização**: Docker e Docker Compose

## Configuração do Ambiente

### 1. Configuração do Ambiente Virtual Python

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows
```

### 2. Instalação das Dependências

```bash
pip install -r requirements.txt
```

### 3. Configuração das Variáveis de Ambiente

Copie o arquivo de exemplo e configure as variáveis:

```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas configurações:

```bash
# Configurações da OpenAI
OPENAI_API_KEY=sua_chave_openai_aqui
OPENAI_EMBEDDING_MODEL=text-embedding-3-small

# Configurações do Google (opcional)
GOOGLE_API_KEY=sua_chave_google_aqui
GOOGLE_EMBEDDING_MODEL=models/embedding-001

# Configurações do Banco de Dados
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/rag

# Configurações do Vector Store
PG_VECTOR_COLLECTION_NAME=document_embeddings

# Caminho do PDF
PDF_PATH=document.pdf
```

## Execução do Sistema

### 1. Inicialização do Banco de Dados

Inicie o PostgreSQL com pgVector usando Docker Compose:

```bash
docker compose up -d
```

### 2. Ingestão do Documento PDF

Execute o script de ingestão para processar o PDF e armazenar os embeddings:

```bash
python src/ingest.py
```

Este processo irá:

- Carregar o arquivo PDF especificado em `PDF_PATH`
- Dividir o conteúdo em chunks de 1000 caracteres com overlap de 150
- Gerar embeddings usando o modelo OpenAI
- Armazenar os vetores no PostgreSQL

### 3. Execução do Chat Interativo

Inicie a interface de linha de comando para fazer consultas:

```bash
python src/chat.py
```

## Exemplo de Uso

```bash
$ python src/chat.py
Digite sua pergunta: Qual o faturamento da Empresa SuperTechIABrazil?
Buscando resposta...
Resposta:
O faturamento foi de 10 milhões de reais.
```

## Funcionalidades Técnicas

### Processamento de Documentos

- **Chunking**: Divisão automática do texto em segmentos de 1000 caracteres
- **Overlap**: Sobreposição de 150 caracteres entre chunks para manter contexto
- **Metadados**: Preservação de informações de origem do documento

### Busca Semântica

- **Similaridade**: Busca por similaridade de cosseno nos embeddings
- **Top-K**: Retorna os 10 resultados mais relevantes (k=10)
- **Contextualização**: Concatenação dos resultados para formação de contexto

### Sistema de Respostas

- **Prompt Engineering**: Template estruturado para garantir respostas baseadas apenas no contexto
- **Validação de Contexto**: Respostas condicionadas à disponibilidade de informações relevantes
- **Prevenção de Alucinação**: Instruções explícitas contra uso de conhecimento externo
