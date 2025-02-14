def dupailoczyn(x,y):
    petla = 0
    def iloczyn(x, y):
        nonlocal petla
        if y == 1:
            return x
        else:
#            print(f'x to: {x}')
            petla = petla + 1
            k = y // 2
            print(f'k nr{petla}. k={k}')
            z = iloczyn(x,k)
            print(f'z nr{petla}. z={z}')
            print(f'y nr{petla}. y={y}')
            if y % 2 == 0:
                return z + z
            else:
                return x + z + z
    return iloczyn(x,y)

print(dupailoczyn(9, 11))



