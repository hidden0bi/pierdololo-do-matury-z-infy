plik = open('liczby.txt', 'r')
plik = plik.readlines()  #odczytywanie linii

wiersz1 = plik[0].strip().split(' ') #obranie liczby ze spacji i cudzyslowiu
lista = []
for liczby in wiersz1: #wyciagniecie z listy liczb
    lista.append(int(liczby)) #dodanie liczb do listy i zmiana ze stringa w inta


lista.sort(reverse=True) # odwrocenie sortowania liczby, nie mozna zrobic lista = lista.sort(-''-), bo program sie zesra

print(lista[101])

#w 3/4 zrobilem sam to zadanie, jestem dumy :)