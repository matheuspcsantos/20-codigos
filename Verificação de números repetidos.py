def duplicados(lista):
    return len(lista) != len(set(lista))

print(duplicados([1,2,3,3]))
