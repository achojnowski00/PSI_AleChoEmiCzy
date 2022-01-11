def temp(c,temperature_type):
    if temperature_type == "Fahrenheit":
        return c*9/5+32
    elif temperature_type == "Rankine":
        return (c + 273.15)*1.8
    elif temperature_type == "Kelvin":
       return c + 273.15
    else:
        return "Nieprawidłowa wartość"


print(temp(15,"Fahrenheit"))
print(temp(15,"Rankine"))
print(temp(15,"Kelvin"))
print(temp(15,"Celsjusz"))
