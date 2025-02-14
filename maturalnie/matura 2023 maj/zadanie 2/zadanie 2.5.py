plik = open('bin_przyklad.txt','r')
plik_open = plik.readlines()


def xor(x, y):
    # Konwertujemy wejścia na liczby całkowite,
    # dzięki czemu warunki będą działać prawidłowo.
    x = int(x)
    y = int(y)

    if x == 1 and y == 1:
        wynik = 0
    elif x == 1 and y == 0:
        wynik = 1
    elif x == 0 and y == 1:
        wynik = 1
    elif x == 0 and y == 0:
        wynik = 0
    else:
        # Jeśli wejście nie jest 0 lub 1, zgłaszamy błąd.
        raise ValueError("Argumenty funkcji xor muszą być 0 lub 1.")

    return wynik

for p in plik_open:

    result = ''
    p = str(p)
    p_2 = int(p,2)
    pna2 = bin(p_2//2)[2::]
    pna2 = int(pna2)
    p = int(p)
    wynik = p ^ pna2
    p = str(p)
    pna2 = str(pna2)
    max_len = max(len(p), len(pna2))
    pna2 = pna2.zfill(max_len)
    #print(f'p to: {p}')
    #print(f'p//2 to: {pna2}')
    for i in range(len(p)):
        bit_p = int(p[i])
        bit_pna2 = int(pna2[i])
        wynik1 = xor(bit_p,bit_pna2)
        wynik1 = str(wynik1)
        result += wynik1
    print(result)