plik = open('bin_przyklad.txt','r')
linie = plik.readlines()
print(f"Wczytane linie z pliku: {linie}")
wynik = 0

for linijka in linie:
    print(f"\n--- Analizuję nową linijkę: {linijka.strip()} ---")

    linijka = linijka.strip()  # Usuń białe znaki
    bloki = 1  # Zaczynamy od 1 bloku

    # Sprawdzamy każdą parę sąsiednich cyfr
    for i in range(1, len(linijka)):
        if linijka[i] != linijka[i - 1]:
            bloki += 1
            print(f"Znaleziono nowy blok - liczba bloków: {bloki}")

    print(f"Końcowa liczba bloków dla liczby {linijka}: {bloki}")

    # Sprawdzamy czy liczba ma co najwyżej 2 bloki
    if bloki <= 2:
        wynik += 1
        print(f"Liczba zakwalifikowana - aktualna suma liczb ≤ 2 bloki: {wynik}")

print(f'\nKońcowy wynik to: {wynik}')
plik.close()