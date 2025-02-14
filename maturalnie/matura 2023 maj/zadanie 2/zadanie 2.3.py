plik = open('bin_przyklad.txt','r')
linie = plik.readlines()
lista = []
wynikfinal = 0

def essa():
    global wynikfinal
    if wynikfinal == False:
        return wynik
    else:
        return wynikfinal





def zamiana(n):
    n = n.strip()
    return int(n,2) 

for linia in linie:
    x = zamiana(linia)
    lista.append(x)
wynik = max(lista)
wynikfinal = bin(int(wynik))
wynikfinal = wynikfinal[2::]


print(essa())