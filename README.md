# Desafio6_SquadBerthaLutz

## 3. Consultas SQL
Escreva consultas SQL para realizar as seguintes operações:
- [x] Listar todos os livros disponíveis @louiseluli
- [x] Encontrar todos os livros emprestados no momento @mcaponera
    ```sql
    SELECT titulo, exemplares FROM livros WHERE exemplares > 0;
    ```
- [x] Localizar os livros escritos por um autor específico @louiseluli
- [x] Verificar o número de cópias disponíveis de um determinado livro @mcaponera
    ```sql
    SELECT titulo, nome AS autor, exemplares FROM livros INNER JOIN autores ON autores.autor_id = livros.autor_id WHERE exemplares > 0 AND titulo = 'O Iluminado';
    ```
- [x] Mostrar os empréstimos em atraso @mcaponera
    ```sql
    SELECT * FROM emprestimos NATURAL JOIN usuarios WHERE vencimento_emprestimo < date('now') AND data_devolucao IS NULL

    ```
---
