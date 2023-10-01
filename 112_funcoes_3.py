'''

Em Python tudo é objeto, dessa forma funções também são objetos o que as tornam objetos de primeira classe. 
Com isso podemos atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em estruturas de dados 
(listas, tuplas, dicionários, etc) e usar como valor de retorno para uma função (closures).


'''

def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {funcao.__name__} entre {a} e {b} é igual á {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20



#escopo

'''
Python trabalha com escopo local e global, dentro do bloco da função o escopo é local. 
Portanto alterações ali feitas em objetos imutáveis serão perdidas quando o método terminar de ser executado. 
Para usar objetos globais utilizamos a palavra-chave global, que informa ao interpretador que a variável 
que está sendo manipulada no escopo local é global. Essa NÃO é uma boa prática e deve ser evitada.


'''

salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_bonus(500)  # 2500


foo = 'Foo'

def fooBar():
    foo = 'foo'
    print(foo + 'Bar')

fooBar() # fooBar
print(foo) # Foo

def fooBarWithGlobal():
    global foo
    foo = 'foo'
    print(foo + 'Bar')

fooBarWithGlobal() # fooBar
print(foo) # foo


numeros = [1]

def escopo_objetos_imutaveis():
    numeros.append(2)
    print(numeros) # [1, 2]


escopo_objetos_imutaveis()
print(numeros) # [1, 2]  - mesmo sem usar global ela alteraou a lista
