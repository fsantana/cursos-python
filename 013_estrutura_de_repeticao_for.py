#For

texto = "Uma frase qualquer"
VOGAIS = "AEIOU"


# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha


#Range
# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")


