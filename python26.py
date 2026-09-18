def temperature_p (temperature):
    if temperature > 28 :
        return "Hot"
    elif temperature >= 18:
        return "warm"
    else:
        return "cold"

temperature = int(input("Enter temperature level "))

print (temperature_p(temperature))