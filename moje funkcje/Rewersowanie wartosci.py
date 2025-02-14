def odwroc(wartosc):
    lista = []
    odwrocenie_listy = ''
#    odwrocony = ''
    for znaki in wartosc:
        print(znaki)
        lista.append(znaki)
        odwrocenie_listy = lista.copy()
        odwrocenie_listy.reverse().join()
#        odwrocenie_listy.join()
#        odwrocony = reversed(lista)
    print (odwrocenie_listy)
#    return odwrocony
wartosc = 'ala ma kota'
print(odwroc(wartosc))