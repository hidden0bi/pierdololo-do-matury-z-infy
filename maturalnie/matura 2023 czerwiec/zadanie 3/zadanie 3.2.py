import itertools


plik = open('przyklad.txt','r')
plik_read = plik.readlines()

def anagramy_8cyfr(n):
    for wiersze in n:
        if len(wiersze.strip()) == 8:
            permutacje = itertools.permutations(wiersze.strip())
            for permutacja in permutacje:
                print(''.join(permutacja))


print(anagramy_8cyfr(plik_read))