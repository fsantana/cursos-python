'''
Geralmente usamos métodos de classe criar métodos de fábrica.
Geralmente usamos métodos estáticos para criar funções utilitárias. 
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):  # Como convesão ao usar de usarmo self, usamos cls
        idade = 2022 - ano
        return cls(nome, idade)
    

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))

'''
não acredito que se a melhor forma, mas se não tiver a declaração do @staticmethod essa chamada da erro por não ter o parametro self
'''
print(p.e_maior_idade(20)) 