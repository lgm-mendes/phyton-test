class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"{self.titulo} por {self.autor} ({status})"


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if livro.disponivel:
            livro.disponivel = False
            self.livros_emprestados.append(livro)
            print(f"{self.nome} emprestou {livro.titulo}.")
        else:
            print(f"{livro.titulo} já está emprestado.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.disponivel = True
            self.livros_emprestados.remove(livro)
            print(f"{self.nome} devolveu {livro.titulo}.")
        else:
            print(f"{self.nome} não possui {livro.titulo} emprestado.")

    def listar_livros_emprestados(self):
        if self.livros_emprestados:
            print(f"Livros emprestados por {self.nome}:")
            for livro in self.livros_emprestados:
                print(f"- {livro.titulo}")
        else:
            print(f"{self.nome} não possui livros emprestados.")

class SistemaEmprestimo:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado ao sistema.")

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuário '{usuario.nome}' adicionado ao sistema.")

    def listar_livros_disponiveis(self):
        print("Livros disponíveis:")
        for livro in self.livros:
            if livro.disponivel:
                print(f"- {livro}")

    def listar_todos_livros(self):
        print("Todos os livros no sistema:")
        for livro in self.livros:
            print(f"- {livro}")