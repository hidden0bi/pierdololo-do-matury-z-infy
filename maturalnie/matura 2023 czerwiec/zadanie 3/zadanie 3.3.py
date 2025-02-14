plik = open('anagram.txt','r')
plik_read = plik.readlines()

liczby = []

for wiersze in plik_read:
    liczby.append(int(wiersze.strip(),2))

roznice = []
for i in range(len(liczby) -1):
    roznica = abs(liczby[i] - liczby[i+1])
    roznice.append(roznica)
maks_roznica = max(roznice)
maks_roznica_binarna = bin(maks_roznica)[2:]
print(roznica)