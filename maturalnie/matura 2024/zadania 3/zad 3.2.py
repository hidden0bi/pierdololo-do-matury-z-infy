plik = open('skrot_przyklad.txt', 'r')
wiersze = plik.readlines()

ile_nie_ma =  0
najwieksza = 0
for wiersz in wiersze:
    liczba = int(wiersz)
    liczba = str(liczba)
    wiersz = wiersz.strip()
    skrot = False
    for cyfra in liczba:
        liczba = int(liczba)
        cyfra = int(cyfra)
        if cyfra % 2 != 0:
            skrot = True

    if skrot is False:
        ile_nie_ma += 1
        #liczba = int(liczba)
        if liczba > najwieksza:
            liczba = najwieksza
print(ile_nie_ma)
print(najwieksza)
