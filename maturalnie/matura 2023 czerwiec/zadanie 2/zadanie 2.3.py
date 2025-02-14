def czy_mniejszy(n, s, k1, k2):
    n=n-1
    i = k1
    j = k2
#    i = 1
#    j = 1
    while i<=n and j<=n:
        if s[i]==s[j]:
            i += 1
            j += 1
        else:
            if s[i] < s[j]:
                return True
            else:
                return False
    if j<=n:
        return True
    else:
        return False

s = 'mascarpone'
liczba = len(s)
tab = [0] * liczba
miejsce = 0

for i in range(len(s)):
    for j in range(len(s)):
        if i == j:
            continue
        if czy_mniejszy(liczba, s, i, j) == 0:
            miejsce += 1
    tab[miejsce] = i + 1
    miejsce = 0
print(tab)