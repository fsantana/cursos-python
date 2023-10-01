def calcular_juros_compostos_correto(valor_inicial, juros_anual, anos):
    # Converta a taxa de juros anual para decimal
    taxa_decimal = juros_anual / 100.0

    # Defina o número de vezes que os juros são compostos por ano (geralmente 12 para mensal)
    n = 12

    # Calcule o montante final
    montante_final = valor_inicial * (1 + taxa_decimal / n) ** (n * anos)

    return montante_final

def calcular_juros_compostos_desafio(valor_inicial, juros_anual, anos):
    # Converta a taxa de juros anual para decimal
    taxa_decimal = juros_anual / 100.0

    # Calcule o montante final
    montante_final = valor_inicial * (1 + taxa_decimal) ** (anos)

    return montante_final

# Exemplo de uso
valor_inicial = float(input("Digite o valor inicial: "))
juros_anual = float(input("Digite a taxa de juros anual (em porcentagem): "))
anos = int(input("Digite a quantidade de anos: "))

montante = calcular_juros_compostos_desafio(valor_inicial, juros_anual, anos)

print(f"O montante final após {anos} anos será de R${montante:.2f}")