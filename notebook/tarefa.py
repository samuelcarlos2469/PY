last_id=0

class Tarefa:
    def __init__(self,title,desc,prio):
        global last_id
        last_id += 1
        self.id = last_id
        self.title = title
        self.desc = desc
        self.prio = prio
        self.conclusion = False

    def simples(self):
        return f"Tarefa {self.id}: {self.title} "
    
    def detalhada(self):
        return f"Tarefa {self.id}: {self.title}\n {self.desc} \n{self.prio} Concluded?{self.conclusion}"

    def __lt__ (self,other):
        return self.prio < other.prio
    
    
    

            
        