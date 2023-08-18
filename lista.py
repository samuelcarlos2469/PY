class Lista:
    def definirVars(self, aIsNumber, bIsNumber, cIsNumber):
        if aIsNumber == 1:
            self.a = float(input("Escreva algo"))
        elif aIsNumber == 2:
            pass
        else:
            self.a = input("Escreva algo")

        if bIsNumber == 1:
            self.b = float(input("Escreva outro algo"))
        elif bIsNumber == 2:
            pass
        else:
            self.b = input("Escreva outro algo")

        if cIsNumber == 1:
            self.c = float(input("Escreva mais um algo"))
        elif cIsNumber == 2:
            pass
        else:
            self.c = input("Escreva mais um algo")

    def media(self, a , b, c):
        self.definirVars(1, 1, 1)
        return (self.a + self.b + self.c) / 3
    
    def aumento(self):
        self.definirVars(0, 1, 2)
        return self.b + (0.1 * self.b)
    
    def ex3(self):
        self.definirVars(1,1,0)
        if self.a == self.b:
            return self.a + self.b
        else:
            c = self.a * self.b
            return c
        
    def ex4(self):
        self.definirVars(1, 1, 2)
        if self.b >= 3 or self.b < 5:
            preçoT = self.a + (0.1 * self.a)
            self.c = preçoT / self.b
            return preçoT, self.c
        elif self.b >= 5:
            preçoT = self.a + (0.2 * self.a)
            self.c = preçoT / self.b
            return preçoT, self.c
        else:
            self.c = self.a / self.b
            return self.a, self.c
        
    def ex5(self):
        nome = str(input("Digite seu nome"))
        media = self.media()

        if media >=8:
            print(f"O aluno {nome} foi aprovado com a média {media}")
        else:
            print(f"O aluno {nome} foi reprovado com a média {media}")

    def seletor(self):
        self.definirVars(1, 1, 1)
        if self.c == 1:
            print(self.a + self.b)
        elif self.c == 2:
            print(self.a * self.b)
        elif self.c == 3:
            print(self.a / self.b)
        else:
            print("O seletor tem que ser 1, 2 ou 3")



            
        

        

        


