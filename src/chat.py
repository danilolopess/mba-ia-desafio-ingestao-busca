"""
    Interactive Chat Interface for PDF-based RAG System

    This module provides a command-line chat interface that allows users to:
    1. Ask questions about ingested PDF documents
    2. Receive contextual answers based on semantic search
    3. Maintain a conversational flow with proper error handling
    4. Exit gracefully with multiple quit commands

    The interface acts as a bridge between user input and the RAG pipeline,
    providing a user-friendly way to interact with the document knowledge base.
"""

from search import search_prompt

def main() -> None:

    print("-" * 50)
    print("Sistema de Chat com PDF")
    print("Digite 'quit', 'exit', 'sair' ou 'q' para encerrar a sessão")
    print("-" * 50)

    while True:
        try:

            user_question = input("Digite sua pergunta: ")

            if user_question.lower() in ('quit', 'exit', 'sair', 'q', ''):
                print("Encerrando a sessão de chat. Até logo!")
                break

            print("Buscando resposta...")

            response = search_prompt(user_question=user_question)

            if not response:
                print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
                return
            
            if not response.content:
                print("Não foi encontrado nenhum conteúdo na resposta do LLM.")
                continue
            
            print(f"Resposta:\n{response.content}")
            print("-" * 50)

        except KeyboardInterrupt:
            print("\nSessão de chat interrompida. Até logo!")
            break

if __name__ == "__main__":
    main()