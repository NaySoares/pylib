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
    cadastrar_livro()
  elif option == "2":
    consultar_livro()
  elif option == "3":
    emprestimo()
  elif option == "4":
    devolucao()
  elif option == "5":
    print("Saindo do programa...")
    exit()
  else:
    print("Opção inválida. Tente novamente.")
    menu()


menu()
