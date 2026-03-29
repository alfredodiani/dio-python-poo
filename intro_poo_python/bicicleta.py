from importlib.util import module_from_spec
from lzma import MODE_NORMAL


class Bicicleta:
    """
    Representa uma bicicleta com atributos como cor, modelo, ano e valor, e métodos para buzinar, parar e correr.
    """
    def __init__ (self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Ding ding")

    def parar(self):
        print("Parando a bicicleta")
        print("Bicicleta parada")

    def correr(self):
        print("Correndo com a bicicleta")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"



b1 = Bicicleta("Vermelha", "Caloi", 2020, 1500)
b1.buzinar()
b1.correr()
b1.parar()
print(b1)

b2 = Bicicleta("Azul", "Monark", 2018, 1200)
b2.buzinar()
b2.correr()
b2.parar()
print(b2)