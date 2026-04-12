class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome): #cls é a referencia para a classe
        # print(cls)
        idade = 2022 - ano
        return Pessoa(nome, idade)
    
    @staticmethod
    def is_maior_idade(idade):
        return idade >= 18
    
    def __str__(self):
        return f"{self.nome} - {self.idade}"


p = Pessoa("John", 45)
print(p.nome, p.idade)

p2 = Pessoa.criar_de_data_nascimento(1980, 5, 18, "James")
print(p2)

print(Pessoa.is_maior_idade(20))
print(Pessoa.is_maior_idade(16))