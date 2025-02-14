plik = open('bin_przyklad.txt','r')
linie = plik.readlines()
wynik = 0

for linijka in linie:


    linijka = linijka.strip()
    bloki = 1


    for i in range(1, len(linijka)):
        if linijka[i] != linijka[i - 1]:
            bloki += 1

    if bloki <= 2:
        wynik += 1



print(f'wynik to: {wynik}')



#print(f'liczba bloków dla 65: {bloczki()}')