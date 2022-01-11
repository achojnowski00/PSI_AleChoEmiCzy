def delete(text,letter):
    newtext = text.replace(letter,"")
    text = newtext
    return text


print(delete("emilia","i"))
