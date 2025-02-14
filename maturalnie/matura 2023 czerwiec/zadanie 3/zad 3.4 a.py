plik = open('przyklad.txt','r')
plik_read = plik.readlines()
decy = []
calosc = 0
calosc = int(calosc)

for linijki in plik_read:
    decy.append([int(linijki.strip(), 2)])
    calosc += 1

zbior=[]
licznik = 0
for liczba in decy:
    for cyferka in liczba:
        cyferka = str(cyferka)
        for cyfra in cyferka:
            cyfra = str(cyfra)
            print(cyfra)
            if cyfra == '0':
                licznik += 1
                zbior.append(cyferka)
                break
wynik = calosc - licznik

print(wynik, zbior)