import json

with open("dados.json", "r") as f:
    dados = json.load(f)

print(dados)
