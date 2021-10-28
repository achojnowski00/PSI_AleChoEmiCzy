# Zad1
def zad1(a_list, b_list):
    for i in range(0, len(a_list), 2):
        print(a_list[i])
    print("------------")
    for i in range(1, len(b_list), 2):
        print(b_list[i])


zad1([1, 2, 3, 4, 5, 6, 7, 89], [2, 3, 5, 6, 8, 7, 9, 5, 4, 2, 3])

# Zad2


def zad2(data_text):
    length = len(data_text)
    letters = []
    for i in data_text:
        if i not in letters:
            letters.append(i)

    slownik = {"length": length, "letters": letters,
               "big_letters": data_text.upper(), "small_letters": data_text.lower()}
    return slownik


slownikZad2 = zad2("Lorem Ipsum jest tekstem")
print(slownikZad2)


# Zad3
def zad3(text, letter):
    return text.replace(letter, "")


print(zad3("rabarbar", "r"))


# Zad4
def zad4(temp, temperature_type):
    if(type(temp) == int or type(temp) == float):
        if temperature_type == "F":
            F = (temp*1.8)+32
            print(temp, "C =", F, "F")
        elif temperature_type == "R":
            R = (temp+273.15)+1.8
            print(temp, "C =", R, "R")
        elif temperature_type == "K":
            K = temp+273.15
            print(temp, "C =", K, "K")
        else:
            print("Błędna jednostka temperatury, tylko K F lub R")
    else:
        print("Błędna wartość temperatury, tylko int lub float")


zad4(10, "K")

# Zad 7


def zad7(text):
    return text[::-1]


print(zad7("koteł"))
