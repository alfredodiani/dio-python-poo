class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self,  cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class Ave (Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, numero_patas):
        print(Ornitorrinco.__mro__)
        super().__init__(cor_pelo=cor_pelo, cor_bico= cor_bico, numero_patas = numero_patas)


gato = Gato(numero_patas = 4, cor_pelo = "Preto")
print(gato)

orni = Ornitorrinco(numero_patas = 4, cor_pelo= "Vermelho", cor_bico= "laranja")
print(orni)