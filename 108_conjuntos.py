'''
Declaração com chaves {}
Valores são únicos
Conjuntos em python não suportam indexação

'''

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}


# acesso via indice só convertendo para lista
numeros = {1, 2, 3, 2}
numeros = list(numeros)
print(numeros[0])



# iteração
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")



# union
conjunto_a = {1, 2}
conjunto_b = {3, 4}

resultado = conjunto_a.union(conjunto_b)
print(resultado) # {1, 2, 3, 4}



# intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado) # {2, 3}



# difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado) # {1}

resultado = conjunto_b.difference(conjunto_a)
print(resultado) # {4}




# symmetric_difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado) # {1, 4}




# issubset & issuperset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  
print(resultado) # True

resultado = conjunto_b.issubset(conjunto_a)  
print(resultado) # False

resultado = conjunto_a.issuperset(conjunto_b) 
print(resultado) # False

resultado = conjunto_b.issuperset(conjunto_a) 
print(resultado) # True



# isdisjoint
# nenhum elemento de um conjunto está contido no outro
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  
print(resultado) # True

resultado = conjunto_a.isdisjoint(conjunto_c) 
print(resultado) # False



# add
sorteio = {1, 23}
sorteio.add(25)  # {1, 23, 25}
print(sorteio)
sorteio.add(42)  # {1, 23, 25, 42}
print(sorteio)
sorteio.add(25)  # {1, 23, 25, 42}
print(sorteio)



# clear
sorteio = {1, 23}
print(sorteio)  # {1,23}
sorteio.clear()
print(sorteio)  # {}



# copy
sorteio = {1, 23}
print(sorteio)  # {1, 23}
sorteio.copy()
print(sorteio)  # {1, 23}




# remove
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}




# discard
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.discard(1)
numeros.discard(45)
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}
# não da erro ao tentar retirar valor que não existe



# pop
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.pop())  # 0
print(numeros.pop())  # 1
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9}



# len
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(len(numeros))  # 10



# in
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(1 in numeros)  # True
print(10 in numeros)  # False