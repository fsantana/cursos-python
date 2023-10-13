import re

# Lista de endereços de exemplo
enderecos = [
    'Rua das Flores, 123, Centro, Curitiba, PR, Brasil, 80000-000',
    'Avenida Paulista, 1578, Bela Vista, São Paulo, SP, Brasil, 01310-200',
    # ...
]

# Expressão regular para CEPs no formato 00000-000
regex = r'\b(\d{5})-(\d{3})\b'

for endereco in enderecos:
    match = re.search(regex, endereco)
    if match:
        print(f'Endereço: {endereco}')
        print(f'CEP: {match.group(1)+match.group(2)}')