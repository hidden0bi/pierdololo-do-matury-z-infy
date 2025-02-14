plik = open('pi_przyklad.txt', 'r')
plik_open = plik.readlines()
lista = []
wynik = 0
listownie = []
koncowa = []

for linia in plik_open:
    cyfra = int(linia.strip())
    lista.append(cyfra)
koniec = ''
for i in range(0, len(lista)-1, 2):
    calosc = lista[i:i+2]
    koniec = "".join(map(str, calosc))
    koniec = int(koniec)
    listownie.append(koniec)

for pojedyncze in listownie:
    pojedyncze = str(pojedyncze)
    if len(pojedyncze) == 1:
        pojedyncze = pojedyncze.zfill(2)
    koncowa.append(pojedyncze)

for essownicy in koncowa:
    for i in range (1, len(essownicy)-1):
        for j in range(1, len(essownicy) - 1):
            if essownicy[i] == essownicy[j]:
                wynik += 1
                print(wynik)