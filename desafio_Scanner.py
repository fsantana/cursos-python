import sys

for linha in sys.stdin:
    try:
        valor = float(linha)
    except ValueError:
        valor = -1

    if valor > 0:
        print("Deposito realizado com sucesso!")
        print(f"Saldo atual: R$ {valor:.2f}")
        break
    elif valor == 0:
        print("Encerrando o programa...")
        break
    else:
        print("Valor invalido! Digite um valor maior que zero.")