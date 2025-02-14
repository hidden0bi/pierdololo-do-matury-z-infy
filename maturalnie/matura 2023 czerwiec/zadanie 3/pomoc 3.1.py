plik = open('przyklad.txt','r')
plik_read = plik.readlines()

#print(plik_read)

def zliczator_0i1(n):
    zera = 0
    jedynki = 0
    lista1 = []
    lista2 = []
    lista3 = []
    for wiersz in n:
        wiersz.strip()
        lista1.append(wiersz)
    print(f'lista1: {lista1}')
    for osobne in lista1:


        for cyferka in osobne[0]:
            if cyferka == '0':
                zera += 1
            elif cyferka == '1':
                jedynki +=1
    return zera, jedynki






        #print(wiersze)
print(zliczator_0i1(plik_read))

#to jest jakies gowno xdd 