#append
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)  # [1, "Python", [40, 30, 20]]



#clear
lista.clear()
print(lista)  # []



#copy
lista = [1, "Python", [40, 30, 20]]
l2 = lista
l2[1] = "Copia por referencia"
print(lista) #[1, 'Copia por referencia', [40, 30, 20]]

lista = [1, "Python", [40, 30, 20]]
l2 = lista.copy()
l2[1] = "Copia por referencia"
print(lista) #[1, 'Python', [40, 30, 20]]

print(id(l2), id(lista)) 



#count
cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1



#extend
linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp", "c"])

print(linguagens)  # ["python", "js", "c", "java", "csharp", "c"]



#index  primeira ocorrencia
print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0
print(linguagens.index("c"))  # 2



#pop
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens) # ['python', 'js', 'c', 'java']
print(linguagens.pop())  # java
print(linguagens) # ['python', 'js', 'c']
print(linguagens.pop(0))  # python
print(linguagens) # ['js', 'c']


#remove
linguagens = ["python", "js", "c", "java", "csharp", "c"]
linguagens.remove("c")
print(linguagens)  # ["python", "js", "java", "csharp"]



#reverse
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.reverse()
print(linguagens)  # ["csharp", "java", "c", "js", "python"]



#sort
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  
print(linguagens) # ["c", "csharp", "java", "js", "python"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  
print(linguagens) # ["python", "js", "java", "csharp", "c"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  
print(linguagens) # ["c", "js", "java", "python", "csharp"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  
print(linguagens) # ["python", "csharp", "java", "js", "c"]



#sorted
linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True)) # ["python", "csharp", "java", "js", "c"]
print(linguagens) #['python', 'js', 'c', 'java', 'csharp'] // mantém original


#len
linguagens = ["python", "js", "c", "java", "csharp"]
print(len(linguagens))  # 5

terceira =  [6, "c"]
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    terceira
]
print(len(matriz))  # 3