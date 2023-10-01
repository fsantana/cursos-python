# Texto
# str
from cgi import print_form
from wsgiref.validate import validator


print("Python")
str()

# Numérico
# int, float, complex
print(1 + 10)
# print("3" + 12) erro
print(1 + 10.5)
int()
float()

#Sequencia (1,2,4), (a,b,c), (32,5,57,32)
#list, tuple, range

#Mapa (chave valor)
#dict

#Coleção (não permite numeros repedidos)
#set, frozenset

#Booleano
#bool
print(True)
print(False)
bool()

#Binário
#bytes,Bytearray,memoryview

# Variáveis
# - Usar snake_case

age = 7
name = 'Eduardo'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.' )


# Python não tem constante, por convenção, usamos o nome todo maiusculo para constantes, mas se tentar alterar o valor ele vai aceitar
DEBUG = True
print(DEBUG)
STATES = ['SP', 'PR', 'GO']
DEBUG = "a"
print(DEBUG)

# Conversão der tipos
# inteiro para float
preco = 10
print(preco)

preco = float(preco)
print(preco)

preco - 10/2
print(preco)

# Float para inteiro
preco = 10.30
print(preco)
preco = int(preco)
print(preco)

# conversão por divisão
preco = 10
print(preco)
# 10

print(preco / 2)
# 5.0

print(preco // 2)
# 5 (int)

print(preco // 3)
# 3 (int)

# Numérico para string

preco = 10.50
idade = 28

print(str(preco))

print(str(idade))

texto = f"idade {idade} preco {preco}"
print(texto)

# string para numérico
preco = "10.50"
idade = "28"
print(float(preco))

print(int(idade))


#lança erro
preco = "python"
#print(float(preco))
#print(int("10.10"))

print(int(float("10.115")))
# 10


valor = 10.10
print(type(valor))
print(type(str(valor)))

