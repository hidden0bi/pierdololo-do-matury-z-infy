plik = open('skrot_przyklad.txt', 'r')
wiersze = plik.readlines()
for wiersz in wiersze:
    liczba = int(wiersz)
    liczba = str(liczba)
    wiersz = wiersz.strip()
    print(wiersz)