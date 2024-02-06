#Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature.
#The following formula is used for the conversion: C = (5 / 9) * (F – 32)
def to_celsius():
    temp = float(input("Enter the temperature: "))
    c = (5/9) * (temp - 32)
    return c

res = to_celsius()
print(f"{res}")