def npskrot(n):
    n = str(n)
    lista = []
    for cyfry in n:
        cyfry = int(cyfry)
        if cyfry % 2 != 0:
            lista.append(str(cyfry))
    return "".join(lista)

print(npskrot(294762))

