def nieparzysteskroty(n):
    lista = []
    n = str(n)
    for liczba in n:
        n = int(n)
        x = n % 10
        if x % 2 != 0:
            lista.append(str(x))
        n = n // 10
    lista = ''.join(lista)
    return lista
print(nieparzysteskroty(29476))