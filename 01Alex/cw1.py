import string

# ==========
# zadanie 1
lorem = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker'

# ==========
# zadanie 2


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

# ==========
# zadanie 4
stringVariable = "testowa zmienna typu string"
print(dir(stringVariable))
help(stringVariable.format)


# ==========
# zadanie 5
imie = "Alex"
nazwisko = 'Chojnowski'
print((imie[::-1].lower() + " " + nazwisko[::-1].lower()).title())


# ==========
# zadanie 6
lista = []
for i in range(1, 11):
    lista.append(i)
print(lista)
lista1 = lista[0:5]
lista2 = lista[5:10]
print(lista1)
print(lista2)


# ==========
# zadanie 7
lista3 = lista1 + lista2
print(lista3)
lista3 = [0] + lista3
print(lista3[::-1])


# ==========
# zadanie 8
student1 = ("123456", "Jan Kowalski")
student2 = ("789456", "Adam Nowak")
student3 = ("516454", "Urszula Dudziak")
student4 = ("783542", "Mariusz Ptak")

listaStudentow = [student1, student2, student3, student4]
print(listaStudentow)


# ==========
# zadanie 9


# ===========
# zadanie 10
tel = [123465789, 165615651, 123456789, 256439728, 652483792, 678234579]
print(tel)
tel = set(tel)
print(tel)


# ===========
# zadanie 11
for i in range(1, 11):
    print(i)


# ===========
# zadanie 12
for i in range(100, 19, -5):
    print(i)
