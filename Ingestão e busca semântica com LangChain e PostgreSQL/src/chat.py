import os
from dotenv import load_dotenv

from search import search_prompt
import ingest

from langchain_openai import ChatOpenAI

load_dotenv()

# Cores ANSI para print
class Colors:
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GREEN = '\033[92m'  
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'  # Reset da cor

def main():
    print(f"{Colors.BLUE + Colors.BOLD}╔══════════════════════════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.BLUE + Colors.BOLD}║                    🤖 ASSISTENTE IA RAG                      ║{Colors.END}")
    print(f"{Colors.BLUE + Colors.BOLD}╠══════════════════════════════════════════════════════════════╣{Colors.END}")
    print(f"{Colors.BLUE}║  📚 Para adicionar um documento: digite {Colors.YELLOW}'add doc'{Colors.BLUE}            ║{Colors.END}")
    print(f"{Colors.BLUE}║  ❌ Para sair: digite {Colors.YELLOW}'exit'{Colors.BLUE}                                 ║{Colors.END}")
    print(f"{Colors.BLUE}║  💬 Para fazer perguntas: digite sua pergunta diretamente    ║{Colors.END}")
    print(f"{Colors.BLUE + Colors.BOLD}╚══════════════════════════════════════════════════════════════╝{Colors.END}")
    print(f"{Colors.CYAN}✨ Como posso ajudá-lo hoje?{Colors.END}")
    print()

    while(True):
        # Captura da pergunta do usuário
        print(f"{Colors.CYAN}┌─ Você{Colors.END}")
        question = input(f"{Colors.CYAN}└─ {Colors.END}")
        print()
        
        if question == "add doc":
            print(f"{Colors.YELLOW}📁 Digite o caminho do documento:{Colors.END}")
            pdf_path = input(f"{Colors.CYAN}└─ {Colors.END}")
            _ingest_pdf(pdf_path)
            print()
        elif question == "exit":
            print(f"{Colors.GREEN}👋 Obrigado por usar o Assistente IA RAG! Até logo!{Colors.END}")
            break
        else:
            # Resposta da IA
            print(f"{Colors.PURPLE}┌─ 🤖 Assistente IA{Colors.END}")
            print(f"{Colors.PURPLE}├─ Processando sua pergunta...{Colors.END}")
            
            question =search_prompt(question)
            model = ChatOpenAI(model=os.getenv("OPENAI_MODEL_CHAT","gpt-3.5-turbo"), temperature=0.5)
            response = model.invoke(question)
            
            print(f"{Colors.PURPLE}└─ {response.content}{Colors.END}")
            print()

def _ingest_pdf(pdf_path: str):
    try:
        print(f"{Colors.BLUE}-> Iniciando processamento do PDF...{Colors.END}")
        ingest.ingest_pdf(pdf_path)
        print(f"{Colors.GREEN}-> PDF processado com sucesso!{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}❌ Erro ao processar o PDF: {str(e)}{Colors.END}")
        print(f"{Colors.YELLOW}💡 Verifique se o arquivo é um PDF válido e se todas as dependências estão configuradas.{Colors.END}")

if __name__ == "__main__":
    main()