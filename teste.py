from lista import Lista

if __name__ == "__main__":
    lista = Lista()

    x = 10

    while x != 0:
        print("Escolha um exercicio: ")
        print("1 - Media")
        print("2 - Aumento")
        print("3 - Numeros Iguais")
        print("4 - Preco Parcela")
        print("5 - Media 2")
        print("6 - Seletor")

        x = int(input())

        if x == 1:
            media = lista.media()
            print(f"A media foi {media}")
        elif x == 2:
            novoSalario = lista.aumento()
            print(f"O novo salario eh {novoSalario}")
        elif x == 3:
            res = lista.ex3()
            print(f"O resultado eh {res}")
        elif x == 4:
            total, parcela = lista.ex4()
            print(f"O preco total eh {total} e o preco de cada parcela eh {parcela}")
        elif x == 5:
            lista.ex5()
        elif x == 6:
            lista.seletor()