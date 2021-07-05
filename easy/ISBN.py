ISBN = 123456789012

ISBM = str(ISBN)

magicNumber = 0

for letter in ISBM:
    if letter == 1 or letter == 3 or letter == 5 or letter == 7 or letter == 9:
        {letter} * 3 + magicNumber

    else:
        letter+{magicNumber}
    
    print(magicNumber)