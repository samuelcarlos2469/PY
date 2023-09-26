import abc
from datetime import datetime, timedelta
from enum import Enum

class Papel(Enum):
    AUTOR = "autor"
    ATOR = "ator"
    DIRETOR = "diretor"
    EDITOR = "editor"
    MUSICO = "musico"

class Genero(Enum):
    DRAMA = "drama"
    COMEDIA = "comedia"
    TERROR = "terror"
    MUSICAL = "musical"
    ACAO = "ação"


class Colaborador:
    def __init__(self, nome, papel):
        self.nome = nome
        self.papel = papel

class Item(abc.ABC):
    def __init__(self, titulo,assunto, prazo, colaboradores):
        self.titulo = titulo
        self.assunto = assunto
        self.colaboradores = colaboradores
        self.data_emprestimo = None
    @property
    @abc.abstractmethod
    def prazo(self):
        pass

    def emprestar(self):
        self.data_emprestimo = datetime.today() 

    def devolver(self):
        self.data_emprestimo = None

    def disponivel(self):
        return self.data_emprestimo == None
    
    def verificar_devolução(self):
        if self.disponivel():
            return None
        prazo_maximo = self.data_emprestimo + timedelta(days = self.prazo)
        hoje = datetime.today()
        return (prazo_maximo - hoje).days 
    
    def obter_info(self):
        print('Titulo:', self.titulo)
        print('Assunto:', self.assunto)
        print('Prazo:', self.verificar_devolução())
        print('Colaboradores:')
        for colaborador in self.colaboradores:
            print('     ', colaborador.nome)

class Livro(Item):
    prazo = 21  #15-18

    def __init__(self, titulo, assunto, isbn, colaboradores):
        self.isbn = isbn
        super().__init__(titulo, assunto, colaboradores)

    def obter_info(self):
        super().obter_info() #pra usar o da classe pai
        print('ISBN:', self.isbn)