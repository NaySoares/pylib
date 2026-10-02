from livros import cadastrar_livro, consultar_livro, emprestimo

## Lista de livros cadastrados
livros = []

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
