plik = open('pi_przyklad.txt', 'r')
plik_open = plik.readlines()
lista = []

wynik = 0

for linia in plik_open:
    cyfra = int(linia.strip())
    lista.append(cyfra)
koniec = ''
for i in range(0, len(lista), 2):
    calosc = lista[i:i+2]
    koniec = "".join(map(str, calosc))
    koniec = int(koniec)
    if koniec > 90:
        wynik += 1
for i in range(1, len(lista), 2):
    calosc = lista[i:i + 2]
    koniec = "".join(map(str, calosc))
    koniec = int(koniec)
    if koniec > 90:
        wynik += 1
#print(koniec)


print(wynik)

