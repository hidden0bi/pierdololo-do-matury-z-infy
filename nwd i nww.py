'''pierwsza = 54
druga = 117

dzielnik = 2

while pierwsza > 1:
    if pierwsza % dzielnik == 0:
        pierwsza = pierwsza // dzielnik
    else:
        dzielnik += 1

while druga > 1:
    if druga % dzielnik == 0:
        druga = druga // dzielnik
    else:
        dzielnik += 1'''

'''def nwd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


num1 = 117
num2 = 54
wynik = nwd(num1, num2)

print("Największy wspólny dzielnik dla", num1, "i", num2, "to:", wynik)'''

def rozloz_na_czynniki_pierwsze(liczba):
    dzielnik = 2
    czynniki = []
    while liczba > 1:
        if liczba % dzielnik == 0:
            czynniki.append(dzielnik)
            liczba = liczba // dzielnik
        else:
            dzielnik += 1
    return czynniki

def nwd_z_czynnikow(czynniki_x, czynniki_y):
    wspolne_czynniki = set(czynniki_x) & set(czynniki_y)
    nwd = 1
    for czynnik in wspolne_czynniki:
        nwd *= czynnik ** min(czynniki_x.count(czynnik), czynniki_y.count(czynnik))
    return nwd

def nww_z_czynnikow(czynniki_x, czynniki_y):
    wszystkie_czynniki = set(czynniki_x) | set(czynniki_y)
    nww = 1
    for czynnik in wszystkie_czynniki:
        nww *= czynnik ** max(czynniki_x.count(czynnik), czynniki_y.count(czynnik))
    return nww

x = 117
y = 54

czynniki_x = rozloz_na_czynniki_pierwsze(x)
czynniki_y = rozloz_na_czynniki_pierwsze(y)

nwd = nwd_z_czynnikow(czynniki_x, czynniki_y)
nww = nww_z_czynnikow(czynniki_x, czynniki_y)

print(f"Czynniki pierwsze {x}: {czynniki_x}")
print(f"Czynniki pierwsze {y}: {czynniki_y}")
print(f"NWD dla {x} i {y}: {nwd}")
print(f"NWW dla {x} i {y}: {nww}")
