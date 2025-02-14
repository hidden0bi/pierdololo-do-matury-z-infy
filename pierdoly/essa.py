#to jest test

a = 'essa'
literak = 'z kajaka'
lista = []
odwrocenie = []
for literka in literak:
    lista.append(literka)
    odwrocenie = lista.copy()
    odwrocenie.reverse()
#print(a)
print(f'lista: {lista}')
print(f'odwrocenie: {odwrocenie}')

