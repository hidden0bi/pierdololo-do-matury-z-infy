def iloczyn(x,y):
    if y == 1:
        return x
    else:
        k = y//2
        z = iloczyn(x,k)
        if y % 2 == 0:
            return z + z
        else:
            return x+z+z
print(iloczyn(9,11))