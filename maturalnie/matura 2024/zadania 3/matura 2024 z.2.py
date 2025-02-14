b = 1
c = 0
n=542102
how_many = 0
while n > 0:
    a = n % 10
    n = n // 10
    if a % 2 == 0:
        c=c+b*a/2
    else:
        c = c+b
        how_many += 1
    b = b * 10
print(c)
print(how_many)