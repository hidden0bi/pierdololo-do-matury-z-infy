'''# Wczytujemy plik i tworzymy ciąg znaków z cyframi
with open('pi_przyklad.txt', 'r') as file:
    # Usuwamy białe znaki i łączymy wszystkie linie w jeden ciąg
    pi_digits = "".join(line.strip() for line in file if line.strip())

# Zmienna do liczenia fragmentów > 90
count_above_90 = 0

# Zmienna, w której będziemy zapisywać wynikowy ciąg fragmentów
result_string = ""

# Iterujemy po ciągu, pobierając fragmenty po 2 cyfry
for i in range(0, len(pi_digits) - 1, 2):
    fragment = pi_digits[i:i+2]   # Pobieramy 2 cyfry
    print(fragment)              # Wypisujemy fragment
    result_string += fragment + " "  # Dodajemy fragment do wynikowego ciągu

    # Jeśli fragment (zamieniony na liczbę) jest większy niż 90, zwiększamy licznik
    if int(fragment) > 90:
        count_above_90 += 1

# Wypisujemy ostateczne wyniki
print("Fragmentów > 90:", count_above_90)
print("Wynikowy ciąg fragmentów:", result_string.strip())
'''

# Otwieramy plik i czytamy wszystkie linie
with open('pi_przyklad.txt', 'r') as file:
    lines = file.readlines()

# Konwertujemy linie na liczby (całe liczby)
digits = [int(line.strip()) for line in lines]

wynik = 0

# Przetwarzamy cyfry w parach
for i in range(0, len(digits), 2):
    # Sprawdzamy, czy istnieje para – jeśli nie, to mamy tylko jedną cyfrę
    if i + 1 < len(digits):
        # Łączymy dwie cyfry jako łańcuch znaków
        num_str = f"{digits[i]}{digits[i + 1]}"
    else:
        # Jeśli pozostała tylko jedna cyfra, uzupełniamy ją zerem z lewej
        num_str = str(digits[i]).zfill(2)

    # Konwertujemy wynikowy łańcuch na liczbę całkowitą
    number = int(num_str)
    print(number)

    # Jeśli liczba jest większa od 90, zwiększamy licznik
    if number > 90:
        wynik += 1

print("Wynik:", wynik)
