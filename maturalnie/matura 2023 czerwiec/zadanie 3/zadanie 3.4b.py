plik = open('przyklad.txt','r')
plik_read = plik.readlines()
decy = []
calosc = 0
calosc = int(calosc)

def dec_to_bin(liczba):
    for linijki in liczba:
        decy.append([int(linijki.strip(), 2)])x
    return decy



def cyfry(liczba):
    zbior = set()
    while liczba > 0:
        cyfra = liczba % 10
        zbior.add(cyfra)
        liczba = liczba // 10
    return zbior
print(cyfry())

ilosc = 0
maxliczba = 0
wiersze = plik_read

for wiersz in wiersze:
    wiersz = wiersz.strip()
    dziesietna = dec_to_bin(wiersz)
    rozne = cyfry(dziesietna)
    czy = 0 not in rozne
    if czy

        #while liczba > 0:
         #   cyfra = liczba % 10
