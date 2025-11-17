notas = []

def adicionar(nota):
    notas.append(nota)

def listar():
    return notas

def remover(i):
    notas.pop(i)

adicionar("Comprar pão")
adicionar("Estudar Python")
print(listar())
