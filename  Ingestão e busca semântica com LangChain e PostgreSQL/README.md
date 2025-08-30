# 🤖 Assistente IA RAG - Sistema de Busca Semântica com LLM

<div align="center">
  
  ![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
  ![LangChain](https://img.shields.io/badge/LangChain-0.3.27-green.svg)
  ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-336791.svg)
  ![OpenAI](https://img.shields.io/badge/OpenAI-API-412991.svg)
  ![Docker](https://img.shields.io/badge/Docker-Compose-2496ED.svg)
  
  <h3>Sistema inteligente de processamento e consulta de documentos PDF usando RAG (Retrieval-Augmented Generation)</h3>
   
</div>

---

## 📖 Sobre

Este projeto implementa um **Assistente IA com RAG** (Retrieval-Augmented Generation) que permite carregar documentos PDF, processar seu conteúdo e fazer perguntas contextualizadas sobre o material. O sistema utiliza embeddings vetoriais para busca semântica e modelos de linguagem para gerar respostas precisas baseadas apenas no contexto dos documentos carregados.

### ✨ Principais Funcionalidades

- 📄 **Ingestão de Documentos PDF**: Carregamento e processamento automático de arquivos PDF
- 🔍 **Busca Semântica Avançada**: Utiliza embeddings OpenAI para encontrar informações relevantes
- 💬 **Chat Contextualizado**: Respostas baseadas exclusivamente no conteúdo dos documentos
- 🎨 **Interface CLI Interativa**: Terminal colorido e amigável com feedback visual
- 🗄️ **Armazenamento Vetorial**: PostgreSQL com pgvector para persistência eficiente
- ⚡ **Performance Otimizada**: Chunking inteligente e cache de embeddings

## 🏗️ Arquitetura

```mermaid
graph TB
    A[📱 Interface CLI] --> B[🤖 Chat Engine]
    B --> C[🔍 Search Module]
    C --> D[🗄️ PostgreSQL + pgvector]
    
    E[📄 PDF Document] --> F[📚 Ingest Module]
    F --> G[✂️ Text Splitter]
    G --> H[🧮 OpenAI Embeddings]
    H --> D
    
    C --> I[🎯 Similarity Search]
    I --> J[📝 Context Builder]
    J --> K[🤖 LLM OpenAI]
    K --> L[💬 Resposta Contextualizada]
    
    style A fill:#e1f5fe
    style D fill:#fff3e0
    style K fill:#f3e5f5
```

## 🚀 Instalação

### Pré-requisitos

- **Python 3.9+**
- **Docker e Docker Compose**
- **Conta OpenAI com API Key**
- **8GB RAM mínimo recomendado**

### 📋 Passo a Passo

#### 1️⃣ Clone o Repositório

```bash
git clone https://github.com/seu-usuario/desafios-tecnicos-MBA-IA.git
cd desafios-tecnicos-MBA-IA
```

#### 2️⃣ Configure o Ambiente Virtual

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
# Linux/Mac:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

#### 3️⃣ Instale as Dependências

```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
# OpenAI Configuration
OPENAI_API_KEY=sua-chave-api-openai-aqui
OPENAI_EMBEDDING_MODEL=text-embedding-3-small

# Database Configuration
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/rag
PG_VECTOR_COLLECTION_NAME=documents

# Optional: Path for testing
PDF_PATH=document.pdf
```

> 💡 **Dica**: Obtenha sua API Key em [platform.openai.com/api-keys](https://platform.openai.com/api-keys)

#### 5️⃣ Inicie o Banco de Dados

```bash
# Iniciar PostgreSQL com pgvector
docker-compose up -d

# Verificar se está rodando
docker-compose ps
```

## 🎮 Como Usar

### Iniciando o Assistente

```bash
python src/chat.py
```

### Interface em Execução

![Assistente IA RAG em execução](exec.png)

### Comandos Disponíveis

| Comando | Descrição |
|---------|-----------|
| `add doc` | Adicionar um novo documento PDF ao sistema |
| `exit` | Sair do assistente |
| `[sua pergunta]` | Fazer uma pergunta sobre os documentos carregados |

### 📝 Exemplo de Uso

```bash
# 1. Inicie o assistente
$ python src/chat.py

# 2. Adicione um documento
┌─ Você
└─ add doc

📁 Digite o caminho do documento:
└─ ./relatorio-financeiro.pdf
-> PDF processado com sucesso!

# 3. Faça perguntas
┌─ Você
└─ Qual foi o faturamento total do último trimestre?

┌─ 🤖 Assistente IA
├─ Processando sua pergunta...
└─ De acordo com o documento, o faturamento total do último trimestre foi de R$ 2.5 milhões...
```

## 📁 Estrutura do Projeto

```
desafios-tecnicos-MBA-IA/
│
├── 📂 src/                     # Código fonte principal
│   ├── 📄 chat.py              # Interface CLI e loop principal
│   ├── 📄 ingest.py            # Processamento e ingestão de PDFs
│   └── 📄 search.py            # Busca semântica e geração de prompts
│
├── 📄 docker-compose.yml       # Configuração do PostgreSQL + pgvector
├── 📄 requirements.txt         # Dependências Python
├── 📄 .env                     # Variáveis de ambiente (criar localmente)
├── 📄 document.pdf             # Documento exemplo para testes
└── 📄 README.md               # Este arquivo
```

## 🛠️ Stack Tecnológica

### Core
- **[LangChain](https://langchain.com/)** (v0.3.27) - Framework para aplicações LLM
- **[OpenAI API](https://openai.com/)** - Embeddings e modelo de linguagem
- **[PostgreSQL](https://www.postgresql.org/)** (v17) - Banco de dados principal
- **[pgvector](https://github.com/pgvector/pgvector)** - Extensão para busca vetorial

### Bibliotecas Python
- **langchain-openai** - Integração com OpenAI
- **langchain-postgres** - Integração com PostgreSQL/pgvector
- **pypdf** - Processamento de arquivos PDF
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **psycopg** - Driver PostgreSQL para Python

## 🔧 Configurações Avançadas

### Ajuste de Parâmetros

Você pode ajustar os seguintes parâmetros no código:

**Em `ingest.py`:**
```python
# Tamanho dos chunks de texto
chunk_size=1000  # Padrão: 1000 caracteres
chunk_overlap=150  # Padrão: 150 caracteres de sobreposição
```

**Em `search.py`:**
```python
# Número de chunks relevantes para contexto
k=10  # Padrão: 10 chunks mais similares
```

**Em `chat.py`:**
```python
# Modelo e temperatura
temperature=0.5  # Criatividade das respostas (0-1)
```

## 📊 Performance e Limitações

### ✅ Pontos Fortes
- Respostas precisas baseadas em contexto
- Suporte a documentos grandes
- Interface intuitiva
- Persistência de dados

### ⚠️ Limitações Conhecidas
- Suporte apenas para arquivos PDF
- Requer conexão com API OpenAI
- Custo por token processado
- Limite de contexto do modelo LLM
