from itertools import count


nome = "gUIlherME"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá mundo!    "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print(menu.rjust(14, "#"))
print(menu.ljust(14, "#"))

print("-".join(menu))
print(menu.join("--"))

# Interpolação

nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}

# Em desuso
print("Nome: %s Idade: %d" % (nome, idade))
# %s string
# %d inteiro
# %f float

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")

#Fatiamento
nome = "Guilherme Arthur de Carvalho"

print(nome[0])
print(nome[-4])
print(nome[:9])
print(nome[10:])
print(nome[10:16])
print(nome[10:16:2])
# Atu
print(nome[:])
print(nome[::-1])


#Múltiplas linhas

nome = "Guilherme"

mensagem = f"""
   Olá meu nome é {nome},
 Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.
"""

print(mensagem)


print(
    '''
    ============= MENU =============
     1 - Depositar
     2 - Sacar
     0 - Sair
    ================================
            Obrigado por usar nosso sistema!!!!
'''
)

print(len(mensagem))
print(len(nome))

print('MUTE' if len(nome) > 140 else 'TWITTER')

#https://docs.python.org/pt-br/3/library/string.html
#https://docs.python.org/pt-br/3/library/stdtypes.html#text-sequence-type-str

'''
Teste de comentario múltipla linha 
'''