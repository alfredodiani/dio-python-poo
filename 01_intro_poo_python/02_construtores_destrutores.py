class Cachorro:
    def __init__(self, nome, cor, acrodado = True):
        print("Inicializando a classe ... ")
        self.nome = nome
        self.cor = cor
        self.acordado = acrodado

    def __del__(self):
        print("Destruindo a classe ... ")

    def falar(self):
        print("Au au!")



c1 = Cachorro("Rex", "Marrom")
c1.falar()

print("Olá!")

c2 = Cachorro("Luna", "Preta")
c2.falar() 
del c2

print("Olá!2")
