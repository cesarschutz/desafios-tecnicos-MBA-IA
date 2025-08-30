import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()

def ingest_pdf(pdf_path: str):
    print("🚀 Iniciando processamento do PDF...")
    
    doc = _read_pdf(pdf_path)
    chunks = _create_chunks(doc)
    enriched = _enrich_chunks(chunks)
    _save_to_db(enriched)
    
    print("✅ Processamento do PDF finalizado com sucesso!")

def _read_pdf(pdf_path: str) -> str:
    """Lê um arquivo pdf com langchain"""
    doc = PyPDFLoader(pdf_path).load()
    #print(f"doc:\n{doc}")
    print(f"-> PDF carregado: {len(doc)} páginas")
    return doc

def _create_chunks(text: str) -> list[str]:
    """Cria chunks para um texto"""
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150, add_start_index=False)
    chunks = splitter.split_documents(text)
    #for chunk in chunks:
    #  print(f"chunk:\n{chunk.page_content}")
    #  print(f"metadata:\n{chunk.metadata}")
    #  print("-"*100)
    print(f"-> Chunks criados: {len(chunks)}")
    return chunks

def _enrich_chunks(chunks: list[str]) -> list[str]:
    """Enriquece os chunks com metadados"""
    enriched = [
      Document(
        page_content=d.page_content,
        metadata={k: v for k, v in d.metadata.items() if v not in ("", None)}
      )
      for d in chunks
    ]
    #for enriched in enriched:
    #  print(f"enriched:\n{enriched.page_content}")
    #  print(f"metadata:\n{enriched.metadata}")
    #  print("-"*100)
    print(f"-> Chunks enriquecidos com metadados")
    return enriched

def _save_to_db(docs: list[str]):
    """Salva embeddings na base de dados"""
    embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL","text-embedding-3-small"))
    store = PGVector(
      embeddings=embeddings,
      collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
      connection=os.getenv("DATABASE_URL"),
      use_jsonb=True,
    )
    ids = [f"doc-{i}" for i in range(len(docs))]
    store.add_documents(documents=docs, ids=ids)
    print(f"-> Documentos salvos na base de dados: {len(docs)}")

if __name__ == "__main__":
    ingest_pdf(os.getenv("PDF_PATH"))