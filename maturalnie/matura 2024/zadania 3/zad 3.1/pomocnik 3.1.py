def npskrot(n):
    n = str(n)
    liczby = []
    for cyfra in n:
        cyfra = int(cyfra)  # Konwertujemy cyfrę na int od razu
        if cyfra % 2 != 0:  # Sprawdzamy, czy cyfra jest nieparzysta
            liczby.append(str(cyfra))  # Dodajemy tylko nieparzyste cyfry do listy (jako stringi)

    return "".join(liczby)  # Łączymy listę stringów w jeden string


print(npskrot(294762))  # Output: 97


def npskrot(n):
    n = str(n)
    lista = []
    for cyfry in n:
        cyfry = int(cyfry)
        if cyfry % 2 != 0:
            lista.append(str(cyfry))  # Dodajemy cyfry jako stringi

    return "".join(lista)  # Łączymy listę stringów w jeden string

print(npskrot(294762))  # Output: 97