plik = open('liczby.txt', 'r')
plik = plik.readlines()  #odczytywanie linii
wiersz1 = plik[0].strip().split(' ')
wiersz2 = plik[1].strip().split(' ')  #strip wywala wwszystkie puste miejsca jakby xD, a split wywala spacje z listy
ilosc = 0
liczbywierszpierwszy = []
liczbywierszdrugi = []  #zrobinie listy

for wierszpierwszy in wiersz1:
    liczbywierszpierwszy.append(int(wierszpierwszy))
for wierszdrugi in wiersz2:
    liczbywierszdrugi.append(int(wierszdrugi)) #Dodanie z liczb do listy i zmiana z tekstu na liczby

for wierszpierwszy in liczbywierszpierwszy:
    for wierszdrugi in liczbywierszdrugi: #wyciaganie po kolei liczb z tabeli
        if wierszdrugi % wierszpierwszy == 0:
            ilosc += 1
            break
print(f'ZAD 4.1 \n'
      f'Tych dzielników jest: {ilosc}')
