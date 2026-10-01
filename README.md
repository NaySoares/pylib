# Sistema de Biblioteca

## DEFINIÇÃO DO PROBLEMA
Desenvolver um sistema simplificado de biblioteca usando o paradigma imperativo para fixação de conhecimento.
O sistema deve possuir, pelo menos, cadastro de livros, consulta, empréstimo e devolução. Não é necessário interface gráfica podendo ser feita a utilização do terminal para a apresentação do sistema em funcionamento.

## PARTICIPANTES
- Elienai Soares @NaySoares
- Luisa Cruz

## COMO EXECUTAR

### Pré-requisitos

- Python 3 instalado.

### Execução

Clone ou baixe o projeto e, no terminal, acesse a pasta do projeto:

```bash
cd pylib
```

E então execute o projeto:
```bash
python3 main.py
```


## RF e RNF

## 1. Requisitos Funcionais

### RF01 — Cadastro de livros

O sistema deve permitir o cadastro de novos livros.

Cada livro deve possuir os seguintes atributos:

* **ID**
* **Título**
* **Autor**
* **Ano**
* **Status**

#### Regras

* O ID deve ser gerado automaticamente pelo sistema no momento do cadastro.
* O ID deve ser numérico e possuir exatamente **4 dígitos**.
* O status deve utilizar o campo `disponivel`, com os valores `True` ou `False`.
* Todo livro deve ser cadastrado inicialmente com `disponivel = True`.
* Os livros devem ser armazenados em uma **lista em memória**.
* Não deve ser possível cadastrar um livro sem título, autor ou ano válido.

---

### RF02 — Consulta de livros

O sistema deve permitir consultar os livros cadastrados.

O menu de consulta deve possuir as seguintes opções:

1. Listar todos os livros;
2. Buscar livro por título;
3. Buscar livro por autor;
4. Buscar livro por ID;
5. Voltar ao menu anterior.

#### Regras

* A opção "Listar todos" deve apresentar todos os livros cadastrados.
* A busca por título deve permitir localizar livros pelo título informado.
* A busca por autor deve permitir localizar livros pelo autor informado.
* A busca por ID deve aceitar somente valores numéricos.
* Caso seja informado um ID inválido, o sistema deve apresentar uma mensagem de erro.
* Caso nenhum livro seja encontrado, o sistema deve apresentar uma mensagem informativa.

---

### RF03 — Empréstimo de livros

O sistema deve permitir realizar o empréstimo de um livro cadastrado.

#### Regras

* O sistema deve receber o ID do livro.
* O sistema deve verificar se o livro existe.
* O sistema deve verificar se o livro está disponível.
* Um livro somente poderá ser emprestado quando `disponivel = True`.
* Após um empréstimo realizado com sucesso, o status deve ser alterado para `disponivel = False`.
* Caso o livro não exista, o sistema deve apresentar uma mensagem de erro.
* Caso o livro já esteja emprestado, o sistema deve apresentar uma mensagem de aviso e não realizar a operação.

---

### RF04 — Devolução de livros

O sistema deve permitir realizar a devolução de um livro emprestado.

#### Regras

* O sistema deve receber o ID do livro.
* O sistema deve verificar se o livro existe.
* O sistema deve verificar se o livro está atualmente emprestado.
* Um livro somente poderá ser devolvido quando `disponivel = False`.
* Após uma devolução realizada com sucesso, o status deve ser alterado para `disponivel = True`.
* Caso o livro não exista, o sistema deve apresentar uma mensagem de erro.
* Caso o livro já esteja disponível, o sistema deve informar que o livro não está emprestado.

---

### RF05 — Navegação entre menus

O sistema deve possuir um menu principal e submenus para as operações disponíveis.

#### Regras

* Todo submenu deve possuir uma opção para retornar ao menu anterior.
* O usuário deve poder retornar ao menu principal sem encerrar o sistema.
* O sistema deve possuir uma opção para encerramento da aplicação.

---

# 2. Requisitos Não Funcionais

### RNF01 — Linguagem

O sistema deve ser desenvolvido utilizando **Python 3**.

### RNF02 — Paradigma de programação

O sistema deve utilizar obrigatoriamente o **paradigma de programação imperativo**.

### RNF03 — Interface

O sistema deve possuir uma interface baseada em **terminal (CLI)**, utilizando principalmente:

* `input()`;
* `print()`.


### RNF04 — Armazenamento

Os livros devem ser mantidos exclusivamente em **memória durante a execução do programa**.

### RNF05 — Organização do código

As funções relacionadas ao gerenciamento dos livros devem ser implementadas no arquivo:

```text
livros.py
```

O arquivo deve estar localizado na raiz do projeto.

---

# 3. Regras de Validação

## 3.1 — ID

* O ID deve ser gerado automaticamente pelo sistema.
* O ID deve ser gerado no momento do cadastro.
* O ID deve conter exatamente **4 dígitos numéricos**.
* O ID deve ser aleatório.
* O sistema não deve permitir dois livros com o mesmo ID.

---

## 3.2 — Ano

* O ano não pode ser vazio.
* O ano deve ser um valor numérico inteiro.
* O ano não pode ser igual a zero.
* O ano não pode ser negativo.
* O ano não pode ser maior que o ano atual.

---

## 3.3 — Título

* O título não pode ser vazio.
* O título não pode ser nulo.
* O título deve conter pelo menos um caractere válido após a remoção de espaços em branco.

---

## 3.4 — Autor

* O autor não pode ser vazio.
* O autor não pode ser nulo.
* O autor não deve conter números.
* O autor deve conter pelo menos um caractere válido após a remoção de espaços em branco.

---

# 4. Estrutura esperada do projeto

Inicialmente, o projeto deverá possuir uma estrutura simples:

```text
pylib/
├── livros.py
└── main.py
```

### `main.py`

Responsável principalmente por:

* Exibir o menu principal;
* Receber as opções do usuário;
* Controlar a navegação entre menus;
* Chamar as funções necessárias.

### `livros.py`

Responsável principalmente por:

* Cadastro de livros;
* Consulta de livros;
* Empréstimo;
* Devolução;
* Manipulação da lista de livros;
* Validações relacionadas aos livros.
