import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

# Criar tabela autores
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS autores (
        autor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(255) NOT NULL
    )
"""
)

# Criar tabela editoras
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS editoras (
        editora_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(255) NOT NULL,
        endereco VARCHAR(255)
    )
"""
)

# Criar tabela livros
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS  livros (
        livro_id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo VARCHAR(255) NOT NULL,
        autor_id INTEGER,
        editora_id INTEGER,
        ano_publicacao INTEGER,
        genero VARCHAR(50),
        exemplares INTEGER DEFAULT 1,
        FOREIGN KEY (autor_id) REFERENCES autores(autor_id),
        FOREIGN KEY (editora_id) REFERENCES editoras(editora_id)
    )
"""
)

# Criar tabela usuarios
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS  usuarios (
        usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE
    )
"""
)

# Criar tabela emprestimos
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS  emprestimos (
        emprestimo_id INTEGER PRIMARY KEY AUTOINCREMENT,
        livro_id INTEGER,
        usuario_id INTEGER,
        data_emprestimo DATE NOT NULL,
        data_devolucao DATE,
        vencimento_emprestimo DATE,
        FOREIGN KEY (livro_id) REFERENCES livros(livro_id),
        FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
    )
"""
)

# Cria um gatilho para alterar o valor de exemplares (executar apenas uma vez)
cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS atualizar_exemplares
    AFTER INSERT ON emprestimos
    FOR EACH ROW
    BEGIN
        UPDATE livros
        SET exemplares = exemplares - 1
        WHERE livro_id = NEW.livro_id;
    END;
""")

# Cria um gatilho para atualizar o número de exemplares ao devolver um livro
cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS devolver_exemplar
    AFTER UPDATE OF data_devolucao ON emprestimos
    FOR EACH ROW
    WHEN NEW.data_devolucao IS NOT NULL
    BEGIN
        UPDATE livros
        SET exemplares = exemplares + 1
        WHERE livro_id = NEW.livro_id;
    END;
""")

# Salvar (commit) as mudanças
conexao.commit()

# --------------------------------------------------------------------------------
# 2 - INSERÇÃO DE DADOS

autores = [
    ("J.K. Rowling",),
    ("George R.R. Martin",),
    ("J.R.R. Tolkien",),
    ("Agatha Christie",),
    ("J.D. Salinger",),
    ("Herman Melville",),
    ("F. Scott Fitzgerald",),
    ("Jane Austen",),
    ("Mark Twain",),
    ("Stephen King",),
]

# Insere dados na tabela autores
cursor.executemany("INSERT INTO autores (nome) VALUES (?)", autores)

editoras = [
    ("Companhia das Letras", "Rua Guaicurus, 500 - São Paulo, SP"),
    ("Editora Record", "Rua Rego Freitas, 454 - São Paulo, SP"),
    ("Editora Intrínseca", "Rua do Ouvidor, 55 - Rio de Janeiro, RJ"),
    ("Editora Saraiva", "Avenida Paulista, 1000 - São Paulo, SP"),
]

# inserir dados na tabela editoras
cursor.executemany("INSERT INTO editoras (nome, endereco) VALUES (?, ?)", editoras)


livros = [
    ("Harry Potter e a Pedra Filosofal", 1, 1, 1997, "Fantasia", 5),
    ("A Guerra dos Tronos", 2, 2, 1996, "Fantasia", 10),
    ("O Hobbit", 3, 3, 1937, "Fantasia", 4),
    ("Assassinato no Expresso do Oriente", 4, 4, 1934, "Mistério", 6),
    ("O Apanhador no Campo de Centeio", 5, 2, 1951, "Ficção Literária", 9),
    ("Moby Dick", 6, 3, 1851, "Aventura", 8),
    ("O Grande Gatsby", 7, 5, 1925, "Romance", 3),
    ("Orgulho e Preconceito", 8, 1, 1813, "Romance", 6),
    ("As Aventuras de Huckleberry Finn", 9, 2, 1884, "Aventura", 8),
    ("O Iluminado", 10, 4, 1977, "Terror", 12),
]

# Insere livros na tabela livros
cursor.executemany(
    """
    INSERT INTO livros 
    (titulo, autor_id, editora_id, ano_publicacao, genero, exemplares) 
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    livros,
)

usuarios = [
    ("Alice Silva", "alice.silva@example.com"),
    ("Bruno Costa", "bruno.costa@example.com"),
    ("Carla Oliveira", "carla.oliveira@example.com"),
    ("Daniela Pereira", "daniela.pereira@example.com"),
    ("Eduardo Almeida", "eduardo.almeida@example.com"),
    ("Fernanda Santos", "fernanda.santos@example.com"),
    ("Gustavo Ferreira", "gustavo.ferreira@example.com"),
    ("Heloísa Martins", "heloisa.martins@example.com"),
    ("Igor Santos", "igor.santos@example.com"),
    ("Juliana Lima", "juliana.lima@example.com"),
]

# insere usuarios na tabela usuarios
cursor.executemany("INSERT INTO usuarios (nome, email) VALUES (?, ?)", usuarios)


# Lista de empréstimos
emprestimos = [
    (1, 1, "2024-08-01", None, "2024-08-11"),  # Livro 1 emprestado para o usuário 1 
    (2, 2, "2024-07-05", "2024-07-20", "2024-07-15"),  # Livro 2 emprestado para o usuário 2
    (3, 3, "2024-08-10", None, "2024-08-20"),  # Livro 3 emprestado para o usuário 3
    (4, 4, "2024-08-15", None, "2024-08-25"),  # Livro 4 emprestado para o usuário 4
    (5, 5, "2024-06-20", "2024-06-01", "2024-06-30"),  # Livro 5 emprestado para o usuário 5
    (6, 6, "2024-08-25", None, "2024-09-04"),  # Livro 6 emprestado para o usuário 6
    (7, 7, "2024-08-01", "2024-08-15", "2024-08-11"),  # Livro 7 emprestado para o usuário 7
    (8, 8, "2024-08-05", None, "2024-08-15"),  # Livro 8 emprestado para o usuário 8
    (9, 9, "2024-08-10", None, "2024-08-20"),  # Livro 9 emprestado para o usuário 9
    (10, 10, "2024-08-15", None, "2024-08-25"),  # Livro 10 emprestado para o usuário 10
]

# Insere dados na tabela emprestimos
cursor.executemany(
    """
    INSERT INTO emprestimos 
    (livro_id, usuario_id, data_emprestimo, data_devolucao, vencimento_emprestimo) 
    VALUES (?, ?, ?, ?, ?)
    """,
    emprestimos,
)

# Salvar (commit) as mudanças após as inserções
conexao.commit()
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# 3 - CONSULTA DE DADOS

# Encontrar todos os livros emprestados no momento
livros_emprestados = cursor.execute("""
    SELECT titulo 
    FROM emprestimos 
    INNER JOIN livros ON emprestimos.livro_id = livros.livro_id
    WHERE emprestimos.data_devolucao IS NULL;
""")
print("Livros emprestados no momento:")
for x in livros_emprestados:
    print(x)

# Localizar os livros escritos por um autor específico
livro_autor = cursor.execute("""
    SELECT titulo 
    FROM livros 
    INNER JOIN autores ON livros.autor_id = autores.autor_id 
    WHERE autores.nome = 'Stephen King';
""")
print("\nLivros escritos por Stephen King:")
for y in livro_autor:
    print(y)

# Verificar o número de exemplares disponíveis de um determinado livro
autor_exemplares = cursor.execute("""
    SELECT titulo, autores.nome AS autor, exemplares 
    FROM livros 
    INNER JOIN autores ON autores.autor_id = livros.autor_id 
    WHERE exemplares > 0 AND titulo = 'O Iluminado';
""")
print("\nExemplares disponíveis de 'O Iluminado':")
for exemplar in autor_exemplares:
    print(exemplar)

# Encontrar todos os livros emprestados no momento (quando todos os exemplares estão emprestados)
todos_emprestados = cursor.execute("""
    SELECT titulo, autores.nome AS autor 
    FROM livros 
    INNER JOIN autores ON autores.autor_id = livros.autor_id 
    WHERE exemplares = 0;
""")
print("\nLivros sem exemplares disponíveis (todos emprestados):")
for livro in todos_emprestados:
    print(livro)

# Mostrar todos os empréstimos em atraso e seus usuários
atrasos = cursor.execute("""
    SELECT emprestimos.*, usuarios.nome AS usuario_nome, usuarios.email 
    FROM emprestimos 
    INNER JOIN usuarios ON emprestimos.usuario_id = usuarios.usuario_id 
    WHERE vencimento_emprestimo < date('now') 
    AND data_devolucao IS NULL;
""")
print("\nEmpréstimos em atraso e seus usuários:")
for atraso in atrasos:
    print(atraso)


#--------------------------------------
#4 ATUALIZACOES E EXCLUSOES 

# Atualizar qaunt de exemplares 
cursor.execute("UPDATE livros SET exemplares = exemplares - 1 WHERE livro_id = 1") 

#Atualizar email 
cursor.execute("UPDATE usuarios SET email = 'safira.maria@gmail.com' WHERE usuario_id = 4 ")
#Atualizar genero livro
cursor.execute("UPDATE livros SET genero = 'Mistério' WHERE livro_id = 10")

# excluir um autor
cursor.execute("DELETE FROM  autores WHERE autor_id = 1")
# excluir emprestimos devolvidos 
cursor.execute("DELETE FROM emprestimos WHERE data_devolucao IS NOT NULL")
# Atualizar data de devolucao
cursor.execute("UPDATE emprestimos SET data_devolucao = '2024-10-06' WHERE emprestimo_id = 2")

# salva alterações
conexao.commit()

#--------------------------------------------------------------------------------
# 4 - EXCLUSÂO DE DADOS

#deletar um autor pelo nome (primeiro, precisa-se verificar se o autor existe para evitar exceções)
cursor.execute('DELETE FROM autores WHERE nome = "Stephen King"')

#deletar uma editora pelo nome (verificar se a editora existe para evitar exceções)
cursor.execute('DELETE FROM editoras WHERE nome = "Editora Intrínseca"')

# Deletar um empréstimo específico baseado no ID do livro e título
# Nota: Isso é feito na tabela `emprestimos`, mas é mais seguro referenciar pelo `emprestimo_id`
cursor.execute("""
    DELETE FROM emprestimos 
    WHERE livro_id = (SELECT livro_id FROM livros WHERE titulo = 'O Apanhador no Campo de Centeio')
""")

# Deletar um livro pelo título (primeiro, verificar se o livro existe para evitar exceções)
cursor.execute("DELETE FROM livros WHERE titulo = 'O Apanhador no Campo de Centeio'")

# Salvar as alterações no banco de dados
conexao.commit()


# Fecha a conexão
conexao.close()