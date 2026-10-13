import random

# registro de IDs utilizados
ids_utilizados = set()

def gerar_id():
    if len(ids_utilizados) >= 10000:
        raise ValueError("Todos os IDs já foram utilizados!")

    while True:
        novo_id = f"{random.randint(0, 9999):04d}"
        if novo_id not in ids_utilizados:
            ids_utilizados.add(novo_id)
            return novo_id

def valida_ano(ano):
    if not ano.isdigit():
        return False
    ano_int = int(ano)
    return 1000 <= ano_int <= 9999

def mensagem_sem_registro(msg, menu):
    print(msg)
    print("Pressione ENTER para voltar ao menu principal.")
    input()
    menu()

def mostrar_livro(livro):
    status = "Disponível" if livro["disponivel"] else "Indisponível"
    print(f"ID: {livro['id']}, Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Status: {status}")

def cadastrar_livro(lista, menu):
    titulo = input("Digite o título do livro: ")
    while not titulo.strip():
        print("O título do livro não pode ser vazio. Tente novamente.")
        titulo = input("Digite o título do livro: ")

    autor = input("Digite o autor do livro: ")
    while not autor.strip():
        print("O autor do livro não pode ser vazio. Tente novamente.")
        autor = input("Digite o autor do livro: ")

    ano = input("Digite o ano de publicação do livro: ")
    while not valida_ano(ano):
        print("Ano inválido. Digite um ano entre 1000 e 9999.")
        ano = input("Digite o ano de publicação do livro: ")

    livro = {
        "id": gerar_id(),
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "disponivel": True
    }

    lista.append(livro)
    print("\n=== LIVRO CADASTRADO ===\n")
    print(f"Livro '{titulo}' cadastrado com sucesso!\n")
    menu()


def consultar_livro(lista):
    if not lista:
        mensagem_sem_registro("Nenhum livro cadastrado para consulta.\n", menu)
        return

    print("======= CONSULTA DE LIVROS =======\n")
    for livro in lista:
        mostrar_livro(livro)

def emprestimo(lista, menu):
    if not lista:
        mensagem_sem_registro("Nenhum livro cadastrado para empréstimo.\n", menu)
        return

    id_livro = input("Digite o ID do livro que deseja emprestar: ")
    for livro in lista:
        if livro["id"] == id_livro:
            if livro["disponivel"]:
                livro["disponivel"] = False
                print(f"Livro '{livro['titulo']}' emprestado com sucesso!\n")
            else:
                print(f"Livro '{livro['titulo']}' não está disponível para empréstimo.\n")
            break
    else:
        print("Livro não encontrado.\n")

    print("Pressione ENTER para voltar ao menu principal.")
    input()
    menu()


def buscar_por_id(lista):
    if not lista:
        mensagem_sem_registro("Nenhum livro cadastrado para consulta.\n", menu)
        return

    print("======= CONSULTA DE LIVROS =======\n")
    id = input("Digite o ID do livro que deseja consultar: ")
    while not id.isdigit() or len(id) != 4:
        print("ID inválido. Digite um ID de 4 dígitos.")
        id = input("Digite o ID do livro que deseja consultar: ")

    for livro in lista:
        if livro["id"] == id:
            return mostrar_livro(livro)

    print("Livro não encontrado.")


def buscar_por_titulo(lista):
    if not lista:
        mensagem_sem_registro("Nenhum livro cadastrado para consulta.\n", menu)
        return

    print("======= CONSULTA DE LIVROS =======\n")

    titulo = input("Digite o título do livro que deseja consultar: ")
    while not titulo.strip():
        print("O título do livro não pode ser vazio. Tente novamente.")
        titulo = input("Digite o título do livro que deseja consultar: ")

    for livro in lista:
        if titulo.lower() in livro["titulo"].lower():
            return mostrar_livro(livro)

    print("Livro não encontrado.")


def buscar_por_autor(lista):
    if not lista:
        mensagem_sem_registro("Nenhum livro cadastrado para consulta.\n", menu)
        return

    print("======= CONSULTA DE LIVROS =======\n")
    autor = input("Digite o autor do livro que deseja consultar: ")
    while not autor.strip():
        print("O autor do livro não pode ser vazio. Tente novamente.")
        autor = input("Digite o autor do livro que deseja consultar: ")

    for livro in lista:
        if autor.lower() in livro["autor"].lower():
            return mostrar_livro(livro)

    print("Livro não encontrado.")

