import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

# Criar tabela autores
cursor.execute(
    """
    CREATE TABLE autores (
        autor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(255) NOT NULL
    )
"""
)

# Criar tabela editoras
cursor.execute(
    """
    CREATE TABLE editoras (
        editora_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(255) NOT NULL,
        endereco VARCHAR(255)
    )
"""
)

# Criar tabela livros
cursor.execute(
    """
    CREATE TABLE livros (
        livro_id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo VARCHAR(255) NOT NULL,
        autor_id INTEGER,
        editora_id INTEGER,
        ano_publicacao INTEGER,
        genero VARCHAR(50),
        FOREIGN KEY (autor_id) REFERENCES autores(autor_id),
        FOREIGN KEY (editora_id) REFERENCES editoras(editora_id)
    )
"""
)

# Criar tabela usuarios
cursor.execute(
    """
    CREATE TABLE usuarios (
        usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE
    )
"""
)

# Criar tabela emprestimos
cursor.execute(
    """
    CREATE TABLE emprestimos (
        emprestimo_id INTEGER PRIMARY KEY AUTOINCREMENT,
        livro_id INTEGER,
        usuario_id INTEGER,
        data_emprestimo DATE NOT NULL,
        data_devolucao DATE,
        FOREIGN KEY (livro_id) REFERENCES livros(livro_id),
        FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
    )
"""
)

# Salvar (commit) as mudanças
conexao.commit()


# Fechar a conexão
conexao.close()
