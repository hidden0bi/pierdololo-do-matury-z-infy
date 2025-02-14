def nieparzysty_skrot(n):
    skrot = 0
    mnoznik = 1

    while n > 0:
        cyfra = n % 10
        if cyfra % 2 != 0:
            skrot = skrot + cyfra * mnoznik
            mnoznik *= 10
        n //= 10

    return skrot

def nwd(a, b):
    while a !=b:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a

plik = open('skrot2_przyklad.txt', 'r')
wiersze = plik.readlines()

for wiersz in wiersze:
    liczba = int(wiersz)
    liczba_skrot = nieparzysty_skrot(liczba)

    if nwd(liczba, liczba_skrot) == 7:
        print (liczba)