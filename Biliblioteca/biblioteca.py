def cadastrar_livro(titulo, autor, disponibilidade):
    """
    Cadastra um novo livro na biblioteca.

    Args:
        titulo (str): O título do livro.
        autor (str): O autor do livro.
        disponibilidade (bool): Indica se o livro está disponível para empréstimo.

    Returns:
        str: uma string formatada com os dados do livro.
    """
    livro = {
        'titulo': titulo,
        'autor': autor,
        'disponibilidade': disponibilidade
    }

    livro_str = f"""Título: {livro['titulo']},
Autor: {livro['autor']},
Disponibilidade: {livro['disponibilidade']}"""

    
    return livro_str

def listar_livros(*livros):
    """
    Lista os livros cadastrados na biblioteca.

    Args:
        *livros: Uma lista de livros cadastrados.

    Returns:
        str: uma string formatada com os dados dos livros.
    """
    livros_str = ""
    for livro in livros:
        livros_str = f"Títulos: {livros}"
    return livros_str

print(cadastrar_livro("Dom Casmurro", "Machado de Assis", True))

print(listar_livros("Dom Casmurro","O Cortiço","Memórias Póstumas de Brás Cubas"))