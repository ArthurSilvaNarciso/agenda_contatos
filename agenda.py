contatos = []

def menu():
    print("\nMenu:")
    print("1 - Adicionar contato")
    print("2 - Visualizar contatos")
    print("3 - Editar contato")
    print("4 - Favoritar contato")
    print("5 - Visualizar contatos favoritos")
    print("6 - Remover contato")
    print("7 - Sair")
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Entrada inválida! Por favor, digite um número entre 1 e 7.")
        return None
    return opcao

# Função para exibir uma mensagem de erro quando a lista estiver vazia
def verificar_lista_vazia(lista, mensagem):
    if not lista:
        print(mensagem)
        return True
    return False

# Função que adiciona um contato
def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    contatos.append({"nome": nome, "telefone": telefone, "email": email, "favorito": False})
    print("Contato adicionado com sucesso!")

# Função que visualiza os contatos
def visualizar_contatos():
    if verificar_lista_vazia(contatos, "Não há contatos para visualizar."):
        return
    
    for contato in contatos:
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"Email: {contato['email']}")
        print(f"Favorito: {contato['favorito']}")
        print("----------------------------")

# Função que edita um contato
def editar_contato():
    nome = input("Digite o nome do contato que deseja editar: ")
    for contato in contatos:
        if contato["nome"] == nome:
            novo_nome = input(f"Digite o novo nome do contato (atualmente {contato['nome']}): ")
            novo_telefone = input(f"Digite o novo telefone do contato (atualmente {contato['telefone']}): ")
            novo_email = input(f"Digite o novo email do contato (atualmente {contato['email']}): ")
            contato["nome"] = novo_nome
            contato["telefone"] = novo_telefone
            contato["email"] = novo_email
            print("Contato editado com sucesso!")
            return
    print("Contato não encontrado!")

# Função que favorita um contato
def favoritar_contato():
    nome = input("Digite o nome do contato que deseja favoritar: ")
    for contato in contatos:
        if contato["nome"] == nome:
            if contato["favorito"]:
                print("Este contato já está favoritado!")
            else:
                contato["favorito"] = True
                print("Contato favoritado com sucesso!")
            return
    print("Contato não encontrado!")

# Função que visualiza os contatos favoritos
def contatos_favoritos():
    favoritos = [contato for contato in contatos if contato["favorito"]]
    
    if verificar_lista_vazia(favoritos, "Não há contatos favoritos."):
        return
    
    for contato in favoritos:
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"Email: {contato['email']}")
        print(f"Favorito: {contato['favorito']}")
        print("----------------------------")

# Função que remove um contato
def apagar_contato():
    nome = input("Digite o nome do contato que deseja apagar: ")
    for contato in contatos:
        if contato["nome"] == nome:
            contatos.remove(contato)
            print("Contato removido com sucesso!")
            return
    print("Contato não encontrado!")

# Função principal que controla o fluxo do menu
def main():
    while True:
        opcao = menu()
        
        if opcao is None:  # Caso o usuário insira uma opção inválida
            continue
        
        if opcao == 1:
            adicionar_contato()
        elif opcao == 2:
            visualizar_contatos()
        elif opcao == 3:
            editar_contato()
        elif opcao == 4:
            favoritar_contato()
        elif opcao == 5:
            contatos_favoritos()
        elif opcao == 6:
            apagar_contato()
        elif opcao == 7:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o programa
main()
