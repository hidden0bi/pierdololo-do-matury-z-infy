def rozklad_na_czynniki(liczba):
    dzielnik = 2
    wynik = 0
    lista = []

    while liczba > 1:
        if liczba % dzielnik != 0:
            dzielnik += 1
        else:
            liczba //= dzielnik
            lista.append(dzielnik)
    return lista


lista1 = [12,24,8]

for czynniki_pierwsze in lista1:
    wynik1 = rozklad_na_czynniki(czynniki_pierwsze)
    print(f'wynik pierwszy to: {wynik1}')
'''
def rozklad_debilny(n):
    czynniki = []
    i = 2
    while i * i <= n:
        while n% i == 0:
            czynniki.append(i)
            n = n // i
        i = i+ 1
    if n > 1:
        czynniki.append(n)
        return czynniki


asd = [12,24,8]


for czynniki in asd:
    wyniki = rozklad_debilny(czynniki)
    print(f'wynik drugi to: {wyniki}')
'''
#print(rozklad_na_czynniki(12))
#print(rozklad_debilny(asd))
#prawie sam to zrobilem GDYBY NIE TE CHUJOWSTWO ZAJEBANE, PRZEZ KTORE TEGO NIE ZROBILEM, BO DZIELILEM MIMO, ZE DZIELNIK SIE NIE DZIELIL