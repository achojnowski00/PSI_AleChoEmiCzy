#zadanie 1
txt = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

# zadanie 2
imie = "Emilia"
nazwisko = "Czyrak"

litera_1 = imie[2]
litera_2 = nazwisko[3]
count1 = txt.count(litera_1)
count2= txt.count(litera_2)
print("W tekście jest {} liter {} oraz {} liter {}".format(count1,litera_1, count2, litera_2))