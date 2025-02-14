plik = open('bin_przyklad.txt','r')
linie = plik.readlines()
lista = []
wynikfinal = 0

def essa():
    global wynikfinal
    if wynikfinal == 0:  # zmiana z False na 0
        return wynik
    else:
        return wynikfinal

def zamiana(n):
    n = n.strip()  # usuwa znaki białe i znaki nowej linii
    return int(n, 2)

for linia in linie:
    x = zamiana(linia)  # nie zamieniamy na string
    lista.append(x)

wynik = max(lista)
# odkomentuj poniższe linie jeśli chcesz wynik w formie binarnej
wynikfinal = bin(int(wynik))
wynikfinal = wynikfinal[2::]

print(essa())
plik.close()