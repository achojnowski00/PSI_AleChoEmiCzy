import string

# ==========
# zadanie 1
lorem = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker'

# ==========
# zadanie 2
# abcs


def licznik(string, char):
    wynik = 0
    string = string.lower()
    char = char.lower()
    for i in range(0, len(string)):
        if(string[i] == char):
            wynik += 1
    return wynik


howManyO = licznik(lorem, 'o')
howManyL = licznik(lorem, 'l')

print('W tekście jest {} liter "o", oraz {} liter "l"'.format(howManyO, howManyL))
