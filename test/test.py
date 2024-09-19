from src.main import *
from unittest.mock import patch

def test_livro_str_disponivel():
    livro = Livro("1984", "George Orwell")
    assert str(livro) == "1984 escrito por George Orwell (Disponível)"

def test_livro_str_emprestado():
    livro = Livro("Dom Casmurro", "Machado de Assis")
    livro.disponivel = False
    assert str(livro) == "Dom Casmurro escrito por Machado de Assis (Emprestado)"

def test_emprestar_livro():
    usuario = Usuario("Lucas")
    livro = Livro("1984", "George Orwell")
    usuario.emprestar_livro(livro)
    assert livro.disponivel == False
    assert livro in usuario.livros_emprestados

def test_emprestar_livro_indisponivel():
    usuario = Usuario("Lucas")
    livro = Livro("1984", "George Orwell")
    livro.disponivel = False
    usuario.emprestar_livro(livro)
    assert livro not in usuario.livros_emprestados

def test_devolver_livro():
    usuario = Usuario("Lucas")
    livro = Livro("1984", "George Orwell")
    usuario.emprestar_livro(livro)
    usuario.devolver_livro(livro)
    assert livro.disponivel == True
    assert livro not in usuario.livros_emprestados

def test_devolver_livro_nao_emprestado():
    usuario = Usuario("Lucas")
    livro = Livro("1984", "George Orwell")
    usuario.devolver_livro(livro)
    assert livro not in usuario.livros_emprestados