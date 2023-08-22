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

    def get_tarefa(self,filtro=None,unfinished=None):
        lista = sorted (self.lista,reverse=True)
        if unfinished == True:
            lista = [t for t in lista
                     if t.conclusion != True]

