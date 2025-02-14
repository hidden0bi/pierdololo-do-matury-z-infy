def rozklad_na_czynniki(liczba):
    dzielnik = 2
    wynik = 0
    lista = []

    while liczba > 1:
        if liczba % dzielnik != 0:
            dzielnik += 1
        else:
            liczba //= dzielnik
            lista.append(dzielnik)
    return lista

plik = open('liczby_przyklad.txt', 'r')
plik = plik.readlines()  #odczytywanie linii
wiersz1 = plik[0].strip().split(' ')
wiersz2 = plik[1].strip().split(' ')  #strip wywala wwszystkie puste miejsca jakby xD, a split wywala spacje z listy
ilosc = 0
liczby_pierwsze = []
liczby_calkowite = []  #zrobinie listy
czynniki = []
plusiki = 0

for wierszpierwszy in wiersz1:
    liczby_pierwsze.append(int(wierszpierwszy))
for wierszdrugi in wiersz2:
    liczbywierszdrugi.append(int(wierszdrugi)) #Dodanie z liczb do listy i zmiana z tekstu na liczby

for czynniki_z_drugiego_wiersza in liczbywierszdrugi:
    czynniki.append(rozklad_na_czynniki(czynniki_z_drugiego_wiersza))
    liczbywierszpierwszy_kopia = liczbywierszpierwszy.copy()
    czy_sie_uda = True
    for czynniki in czynniki:
        if czynniki not in liczbywierszpierwszy_kopia:
            czy_sie_uda = False
            #break
        else:




print(liczbywierszpierwszy_kopia)

print(plusiki)
