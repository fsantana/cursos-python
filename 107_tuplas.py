'''
Usa parenteses para a criação ou o construtor tuple
Diferentemente da lista ela é imutavel

'''

frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

#boa pratica para o python saber que é uma tupla
pais = ("Brasil",)
print(pais)



frutas = ("maçã", "laranja", "uva", "pera",)
print(frutas[0])  # maçã
print(frutas[2])  # uva
print(frutas[-1])  # pera
print(frutas[-3])  # laranja

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])  # (1, "a", 2)
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"



tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])  # ("t", "h", "o", "n")
print(tupla[:2])  # ("p", "y")
print(tupla[1:3])  # ("y", "t")
print(tupla[0:3:2])  # ("p", "t")
print(tupla[::])  # ("p", "y", "t", "h", "o", "n")
print(tupla[::-1])  # ("n", "o", "h", "t", "y", "p")



#iteração
carros = (
    "gol",
    "celta",
    "palio",
)

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")



cores = (
    "vermelho",
    "azul",
    "verde",
    "azul",
)

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1



linguagens = ("python", "js", "c", "java", "csharp",)

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0



linguagens = (
    "python",
    "js",
    "c",
    "java",
    "csharp",
)

print(len(linguagens))  # 5



carros = ("gol")
print(isinstance(carros, tuple))



lista = ["a","b","c"]
tupla = ("a", "b", lista)
print(tupla) # ('a', 'b', ['a', 'b', 'c'])
lista.append("d")
print(tupla) # ('a', 'b', ['a', 'b', 'c', 'd'])