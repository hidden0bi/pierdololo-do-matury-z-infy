'''def iloczyn(x,y):
    z = y
    while (y//2) > 0:
        if y % 2 == 1:
            z = z + x
            return z
    x = x+x
    return x
    y = 1
print(iloczyn(9,11))'''

# z = x+z+z

'''
def iloczyn(x,y):
    z = x
    while y//2 > 0:
        if y%2 == 1:
            return z = z+x
    return x = x+x
    y = 1
print(iloczyn(9,11))
'''

def iloczyn(x,y):
    z = 0
    while y > 0:
        if y % 2 == 1:
            z = z + x
        x = x+x
        y = y//2
    return z
print(iloczyn(9,11))


def iloczyn(x, y):
    z = 0
    while y >= 1:
        if y % 2 == 1:
            z = z + x
        x = x + x
        y = y // 2
    return z


print(iloczyn(9, 11))