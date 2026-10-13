from livros import cadastrar_livro, consultar_livro, emprestimo, buscar_por_id, buscar_por_titulo, buscar_por_autor

## Lista de livros cadastrados
livros = []

## SubMenu para consultar livros
def menu_consulta():
  print("======= CONSULTA DE LIVROS =======\n")
  print("1 - Consultar todos os livros")
  print("2 - Consultar livro por ID")
  print("3 - Consultar livro por título")
  print("4 - Consultar livro por autor")
  print("3 - Voltar ao menu principal")

  option = input("Escolha uma opção usando os números: ")

  if option == "1":
    consultar_livro(livros, menu)
  elif option == "2":
    buscar_por_id(livros, menu)
  elif option == "3":
    buscar_por_titulo(livros, menu)
  elif option == "4":
    buscar_por_autor(livros, menu)
  elif option == "5":
    menu()
  else:
    print("Opção inválida. Tente novamente.")
    menu_consulta()


## Interface terminal inicial
def menu():
  print("======= BIBLIOTECA =======\n")
  print("1 - Cadastrar livro")
  print("2 - Consultar livro")
  print("3 - Empréstimo")
  print("4 - Devolução")
  print("5 - Sair")

  option = input("Escolha uma opção usando os números: ")

  if option == "1":
    cadastrar_livro(livros, menu)
  elif option == "2":
    consultar_livro(livros, menu)
  elif option == "3":
    emprestimo(livros, menu)
  elif option == "4":
    devolucao(livros, menu)
  elif option == "5":
    print("Fechando biblioteca...")
    exit()
  else:
    print("Opção inválida. Tente novamente.")
    menu()


menu()
