def slownik(data_text):
    dict = {}
    dict["length"]=len(data_text)
    dict["letters"] = [letter for letter in data_text]
    dict["bigLetters"] = data_text.upper()
    dict["smallLetters"] = data_text.lower()
    return dict

print(slownik("Emilia"))

