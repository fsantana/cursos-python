n = int(input())

while(n > 0):
    n -= 1
    v = input()
    partes = v.split()
    print("encaixa" if partes[0].endswith(partes[1]) else "nao encaixa")