import requests

url = "https://viacep.com.br/ws/01001000/json/"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)
# print(response.text)

""" retorna um dictionary """
endereco = response.json()

print(endereco["logradouro"])
