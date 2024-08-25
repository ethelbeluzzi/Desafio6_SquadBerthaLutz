# 📚 Sistema de Gerenciamento de Biblioteca

Este projeto é um sistema de gerenciamento de biblioteca desenvolvido em Python, utilizando o banco de dados SQLite. O sistema permite gerenciar autores, editoras, livros, usuários e empréstimos. Importante para aplicação dos conhecimentos adquiridos durante o módulo do curso.

## ✨ Funcionalidades

- **📖 Gerenciamento de Autores:** Adição, atualização e exclusão de autores no sistema.
- **🏢 Gerenciamento de Editoras:** Adição, atualização e exclusão de editoras.
- **📚 Gerenciamento de Livros:** Cadastro de livros, controle de exemplares, atualização de informações e exclusão.
- **👥 Gerenciamento de Usuários:** Cadastro e atualização de usuários.
- **🔄 Controle de Empréstimos:** Registro de empréstimos de livros, controle de devoluções e verificação de atrasos.

## 🗂️ Estrutura do Banco de Dados

O banco de dados é composto por cinco tabelas principais:

1. **👨‍💼 Autores:** Armazena informações sobre os autores.
   - `autor_id` (INTEGER): ID único do autor.
   - `nome` (VARCHAR): Nome do autor.

2. **🏢 Editoras:** Armazena informações sobre as editoras.
   - `editora_id` (INTEGER): ID único da editora.
   - `nome` (VARCHAR): Nome da editora.
   - `endereco` (VARCHAR): Endereço da editora.

3. **📚 Livros:** Armazena informações sobre os livros.
   - `livro_id` (INTEGER): ID único do livro.
   - `titulo` (VARCHAR): Título do livro.
   - `autor_id` (INTEGER): ID do autor associado ao livro.
   - `editora_id` (INTEGER): ID da editora associada ao livro.
   - `ano_publicacao` (INTEGER): Ano de publicação do livro.
   - `genero` (VARCHAR): Gênero do livro.
   - `exemplares` (INTEGER): Número de exemplares disponíveis.

4. **👤 Usuários:** Armazena informações sobre os usuários.
   - `usuario_id` (INTEGER): ID único do usuário.
   - `nome` (VARCHAR): Nome do usuário.
   - `email` (VARCHAR): Email do usuário.

5. **🔄 Empréstimos:** Armazena informações sobre os empréstimos de livros.
   - `emprestimo_id` (INTEGER): ID único do empréstimo.
   - `livro_id` (INTEGER): ID do livro emprestado.
   - `usuario_id` (INTEGER): ID do usuário que realizou o empréstimo.
   - `data_emprestimo` (DATE): Data do empréstimo.
   - `data_devolucao` (DATE): Data de devolução (pode ser nula).
   - `vencimento_emprestimo` (DATE): Data de vencimento do empréstimo.

## 🛠️ Scripts Principais

### 1. 🏗️ Criação das Tabelas

O script cria as tabelas necessárias para o funcionamento do sistema, caso ainda não existam.

```python
# Exemplo de criação da tabela de autores
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS autores (
        autor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(255) NOT NULL
    )
"""
)
```

### 2. 📝 Inserção de Dados

Dados iniciais de autores, editoras, livros e usuários são inseridos no banco de dados.

```python
autores = [
    ("J.K. Rowling",),
    ("George R.R. Martin",),
    # outros autores...
]

cursor.executemany("INSERT INTO autores (nome) VALUES (?)", autores)
```

### 3. 🔍 Consultas SQL

Algumas consultas úteis que podem ser realizadas no banco de dados:

- **📚 Listar todos os livros disponíveis:**
  ```sql
  SELECT titulo, exemplares FROM livros WHERE exemplares > 0;
  ```

- **🔄 Encontrar todos os livros emprestados no momento:**
  ```sql
  SELECT titulo FROM emprestimos INNER JOIN livros ON emprestimos.livro_id = livros.livro_id;
  ```

- **✍️ Localizar os livros escritos por um autor específico:**
  ```sql
  SELECT titulo FROM livros INNER JOIN autores ON livros.autor_id = autores.autor_id WHERE autores.nome = 'Stephen King';
  ```

- **⏰ Mostrar os empréstimos em atraso:**
  ```sql
  SELECT * FROM emprestimos NATURAL JOIN usuarios WHERE vencimento_emprestimo < date('now') AND data_devolucao IS NULL;
  ```

### 4. 🛠️ Atualizações e Exclusões

Algumas operações de atualização e exclusão de dados:

- **❌ Deletar um autor:**
  ```sql
  DELETE FROM autores WHERE autor_id = 1;
  ```

- **🔄 Atualizar o número de exemplares de um livro:**
  ```sql
  UPDATE livros SET exemplares = exemplares - 1 WHERE livro_id = 1;
  ```

- **🗑️ Excluir um empréstimo devolvido:**
  ```sql
  DELETE FROM emprestimos WHERE data_devolucao IS NOT NULL;
  ```

## 🚀 Como Executar

1. **📥 Clone o Repositório:**
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. **▶️ Execute o Script:**
   - Certifique-se de que o Python está instalado.
   - Execute o script principal:
     ```bash
     python nome-do-script.py
     ```

3. **🗄️ Verifique o Banco de Dados:**
   - O banco de dados `banco.db` será criado no diretório do projeto.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request conform foi construido pela nossa squad.
