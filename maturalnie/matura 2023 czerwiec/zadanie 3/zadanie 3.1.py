plik = open('anagram.txt','r')
plik_read = plik.readlines()

def zliczator(n):
    lista = []
    for wiersze in n:
        zera = 0
        jedynki = 0
        for cyfra in wiersze.strip():
            if cyfra == '0':
                zera += 1
            elif cyfra == '1':
                jedynki += 1
        lista.append([zera, jedynki])
    return lista

def czy_zrownowazona(x):
    zrownowazone = 0
    prawie_zrownowazone = 0
    for cyfra in zliczator(plik_read):
        zera = cyfra[0]
        jedynki = cyfra[1]
        if zera == jedynki:
            zrownowazone += 1
        if zera - jedynki == 1:
            prawie_zrownowazone += 1
        elif jedynki - zera == 1:
            prawie_zrownowazone += 1

    return f'zrownowazone: {zrownowazone}, prawie_zrownowazone {prawie_zrownowazone}'

#print(zliczator(plik_read))
print(czy_zrownowazona(plik_read))