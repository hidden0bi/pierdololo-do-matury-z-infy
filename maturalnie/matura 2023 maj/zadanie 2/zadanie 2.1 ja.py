n1 = 67
n2 = 245

def dec_to_bin(n):
    n = bin(n)
    n = str(n)
    n = n[2:]
    return n

print(f'binarne {n1} to: {dec_to_bin(n1)}')
#print(f'binarne {n2} to: {dec_to_bin(n2)}')


def bloczki(n):
    lista=[]
    bloki = 1
    binarne = dec_to_bin(n)
    binarne = str(binarne)

    for cyferka in binarne:
        lista.append(cyferka)

    for i in range(1, len(lista)):
        #print(f'len to {len(lista)}')
        #print(f'i to jest {i}')#nie pomyslalem o tym gownie :((
        if lista[i] != lista[i - 1]:
            bloki += 1

    return bloki

    '''for cyferka2 in lista[1]:
        if cyferka != cyferka2:
            print(cyferka2)
            bloki += 1
    return bloki # - 1'''


print(f'liczba bloków dla 65: {bloczki(n1)}')
#print(f'liczba bloków dla 245: {bloczki(n2)}')