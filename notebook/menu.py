from tarefa import Tarefa
from lista import Lista

class Menu:         #ex2 slide 2
    lista = Lista()

    def add_tarefas(self):
        title = input("Qual o título da Tarefa?")
        desc = input("Qual a descrição da Tarefa?")
        prio = input("Qual a prioridade da Tarefa?")
        tarefa = Tarefa(title, desc, prio)
        self.lista.add_tarefa(tarefa)

    def edit_tarefa(self):
        id = input("Qual o ID da tarefa que deseja alterar")
        pergunta = int(input("Deseja alterar o título? Digite 1 para sim 0 para não"))
        if pergunta == 1:
            title = input("Insira o novo título da Tarefa")
        else: title = None

        pergunta = int(input("Deseja alterar a descrição? Digite 1 para sim 0 para não"))
        if pergunta == 1:
            desc = input("Insira a nova descrição da Tarefa")
        else: desc = None

        pergunta = int(input("Deseja alterar a descrição? Digite 1 para sim 0 para não"))
        if pergunta == 1:
            prio = input("Insira a nova prioridade da Tarefa")
        else: prio = None
        pergunta = int(input("Deseja marcar a tarefa como concluída? Digite 1 para sim 0 para não"))
        if pergunta == 1:
            conclusion = True
        else: conclusion = None

        self.lista.edit(id, title, desc, prio, conclusion)

    def remover_tarefa(self):
        id = int(input("Informe o ID da tarefa que deseja excluir"))
        self.lista.remove(id)

    def listar_tarefa(self):
        for t in self.lista:
            t.detalhada()

    def filtrar_tarefa(self):
        filtro = input("Qual o filtro que deseja utilizar na busca?")
        nao_concluidas = int(input("Digite 1 para que apenas sejam mostradas as que não foram concluídas, 2 para que mostrem todas"))
        if  nao_concluidas == 1: 
            unfinished = True
        else: unfinished = False   

        self.lista.get_tarefa(filtro, unfinished)
        



    