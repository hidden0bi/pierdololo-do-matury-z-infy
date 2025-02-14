def dec_to_bin(n):
    return bin(n)[2:]

def bloczki(n):
    if n <= 0:
        return 0

    binarne = dec_to_bin(n)
    bloki = 1  # Zaczynamy od 1, ponieważ pierwszy blok zawsze istnieje

    # Iterujemy przez binarny zapis liczby od drugiego elementu
    for i in range(1, len(binarne)):
        if binarne[i] != binarne[i - 1]:
            bloki += 1

    return bloki

n1 = 67
n2 = 245

print(f'binarne {n1} to: {dec_to_bin(n1)}')
print(f'liczba bloków dla {n1}: {bloczki(n1)}')
print(f'binarne {n2} to: {dec_to_bin(n2)}')
print(f'liczba bloków dla {n2}: {bloczki(n2)}')