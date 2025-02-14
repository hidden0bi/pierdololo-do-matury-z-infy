def iloczyn(x, y, k=0, z=0):
    print(f'Start \t x={x} \t y={y} \t k={k} \t z={z}')
    if y == 1:
        return x
    else:
        k = y // 2
        z = iloczyn(x, k)

        print(f'Else part \t x={x} \t y={y} \t k={k} \t z={z}')

        if y % 2 == 0:
            return z + z
        else:
            return x + z + z

print(iloczyn(10,45))