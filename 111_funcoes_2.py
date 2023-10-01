'''
Definir parametros por posição ou por nome

O que está antes de / é só por posição, o que está depois da / pode ser por nome ou poisição
O que está depois de * é somente por nome, o que está antes pode ser por nome ou posição

Por padrão, argumentos podem ser passados para uma função Python tanto por posição quanto explicitamente pelo nome. 
Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados, 
assim um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados 
por posição, por posição e nome, ou por nome.
'''

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina") 
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido


def criar_carro2(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro2("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro2(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido


def criar_carro3(modelo, ano, placa, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro3(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") 
criar_carro3("Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") 