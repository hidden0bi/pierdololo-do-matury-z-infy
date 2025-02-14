def nieparzysty_skrot(n):
    skrot = 0
    mnoznik = 1

    while n > 0:
        cyfra = n % 10
        if cyfra % 2 != 0:
            skrot = skrot + cyfra * mnoznik
            mnoznik *= 10
        n //= 10

    return skrot
print(nieparzysty_skrot(29467))