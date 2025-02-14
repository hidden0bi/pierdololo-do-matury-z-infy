def xor(x,y):
    global wynik
    if x == 1 and y == 1:
        wynik = 0
    if x == 1 and y == 0:
        wynik = 1
    if x == 0 and y == 1:
        wynik = 1
    if x == 0 and y == 0:
        wynik = 0
    return wynik



a = '1111011'
b= '101101'
c = '101101'
lista_a = []
lista_b = []
lista_c = []

max_fill = max(len(a), len(b), len(c))

a = a.zfill(max_fill)
b = b.zfill(max_fill)
c = c.zfill(max_fill)

result=''
for i in range(max_fill):
    bit_a = int(a[i])
    bit_b = int(b[i])
    bit_c = int(c[i])

    wynik_bit = xor(xor(bit_a, bit_b), bit_c)
    result += str(wynik_bit)
    essa = int(result, 2)

print(essa)


