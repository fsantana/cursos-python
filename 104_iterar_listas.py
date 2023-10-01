carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")



print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0]) #[0, 2, 4, 6, 64]