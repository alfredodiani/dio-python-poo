from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")

    def desligar(self):
        print("Desligando a TV")

    @property
    def marca(self):
        return "LG"

    
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o ar condicionado")

    def desligar(self):
        print("Desligando o ar condicionado")

    @property
    def marca(self):
        return "Samsung"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle2 = ControleArCondicionado()
controle2.ligar()
print(controle2.marca)