# funkcja konwertująca liczbę dziesiętną na binarną
def dec_to_bin(n):
    a = ''  # inicjalizujemy pusty ciąg
    while n > 0:  # dopóki n jest większe od zera
        a = str(n % 2) + a  # dodajemy resztę z dzielenia n przez 2 do ciągu 'a'
        n = n // 2  # dzielimy n przez 2 i zapisujemy wynik jako nowe n
    return a  # zwracamy ciąg reprezentujący liczbę binarną


# funkcja zlicza liczbę bloków w binarnej reprezentacji liczby
def bloki(n):
    n = dec_to_bin(n)  # konwertujemy n na reprezentację binarną
    liczba_blokow = 0  # inicjalizacja licznika bloków
    obecny_blok = n[0]  # ustawiamy pierwszą cyfrę binarną jako obecny blok
    for cyfra in n:  # dla każdej cyfry w n
        if cyfra != obecny_blok:  # jeżeli cyfra jest różna od obecnego bloku
            liczba_blokow += 1  # zwiększamy liczbę bloków
            obecny_blok = cyfra  # i ustawiamy nowy blok jako obecny
    return liczba_blokow + 1  # zwracamy liczbę bloków + 1, bo liczymy od 0


# wywołujemy funkcję bloki dla liczby 67 i wyświetlamy wynik
print(bloki(67))