class Estudante:
    escola = "ABC"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno1 = Estudante("John", 1)
aluno2 = Estudante("David", 2)
mostrar_valores(aluno1, aluno2)

print("*********")

aluno1.matricula = 3
mostrar_valores(aluno1, aluno2)

print("*********")

Estudante.escola = "Python"
aluno3 = Estudante("Peter", 4)
mostrar_valores(aluno1, aluno2, aluno3)
