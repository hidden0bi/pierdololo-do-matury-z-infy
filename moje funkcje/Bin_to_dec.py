#1
def bin_to_dec(liczba):
    x = 0
    pom = len(liczba)
    for i in range(len(liczba)):
        if liczba[i] == '1':
            x = x + 2 ** (pom - 1)
            pom -= 1
    return x
#2
def bin_to_dec1(liczba):
    liczba = int('liczba', 2)
    return liczba