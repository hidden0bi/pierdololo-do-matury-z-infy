def dec_to_bin(n):
    a = ''
    while n > 0:
        a = str(n % 2) + a
        n = n // 2
    return a
print(dec_to_bin(108))