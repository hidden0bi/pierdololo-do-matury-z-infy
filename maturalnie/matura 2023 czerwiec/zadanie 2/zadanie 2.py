#n. — długość słowa
#s[1..n] - słowo zapisane jako tablica znaków (numerowanych od 1)
#k1 - numer pierwszego sufiksu (1 <= k1 <= n)
#k2 - numer drugiego sufiksu (1 <= k2 <= n, k1=/=k2)

def rozbieranie(slowo):
    lista = []
    for literki in slowo:
        lista.append(literki)
    return lista

slowa1 = open('sufiks_1.txt','r')
plik1 = slowa1.readlines()

n = plik1[0]
n = int(n)
s = plik1[1]
lista_kaki = []

string_do_pliku = str(plik1[2]).replace('\n', '')
osobno = string_do_pliku.split(' ')

for kaki in osobno:
    lista_kaki.append(kaki)
wartosci_do_usuniecia = [' ', '\n']
lista1 = lista_kaki
lista1 = [dupa for dupa in lista1 if dupa not in wartosci_do_usuniecia]
k1 = lista1[0]
k1 = int(k1)
k2 = lista1[1]
k2 = int(k2)

s = rozbieranie(s)#zapisanie slowa w liscie
s.remove('\n') #wywalenie \n
print(f'n(dlugosc slowa) to: {n}\ns(slowo w liscie) to: {s} \nk1(1 sufiks) to: {k1}, a k2(drugi) to: {k2} \n\nodpowiedź:')

def czy_mniejszy(n, s, k1, k2):
    n=n-1
    i = k1
    j = k2
#    i = 1
#    j = 1
    while i<=n and j<=n:
        if s[i]==s[j]:
            i += 1
            j += 1
        else:
            if s[i] < s[j]:
                return True
            else:
                return False
    if j<=n:
        return True
    else:
        return False
odpowiedz = czy_mniejszy(n,s,k1,k2)
if odpowiedz:
    print('TAK')
else:
    print('NIE')
print(odpowiedz)