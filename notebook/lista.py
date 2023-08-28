from tarefa import Tarefa

class Lista:
    def __init__(self):
        self.lista = list()

    def add_tarefa(self,tarefa):
        self.lista.append(tarefa)

    def remove(self, id):
        self.lista = [t for t in self.lista
                      if t.id != id]
        
    def edit(self,id,title=None, desc=None,prio=None, conclusion=None):
        for t in self.lista:
            if t.id == id: 
                if title != None: t.title = title
                if desc != None: t.desc = desc
                if prio != None: t.prio = prio
                if conclusion != None: t.conclusion = conclusion
                break

    def get_tarefa(self,filtro=None,unfinished=False):
        self.lista = sorted (self.lista,reverse=True)
        lista = list()

        lista = [t for t in self.lista if not t.conclusion]#primeiro as nao concluidas

        if unfinished != True:
            lista += [t for t in self.lista
                     if t.conclusion == True]#add as concluidas tbm
            
        if filtro:
            for t in self.lista: 
                if filtro in t.title or filtro in t.desc:
                    lista.append(t)
        return lista
        
    def find_tarefa(self, id): #ex1 slide 2
        for t in self.lista:
            if t.id == id:
                return t

    

    



    

