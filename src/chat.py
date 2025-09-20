from search import search_prompt

def main():
    user_question = input("Digite sua pergunta: ")

    print("Buscando resposta...")

    response = search_prompt(user_question=user_question)

    if not response:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return
    
    print(f"Resposta:\n{response.content}")

if __name__ == "__main__":
    main()