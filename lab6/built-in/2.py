#Write a Python program with builtin function that accepts a string
#and calculate the number of upper case letters and lower case letters
def lower_upper_num():
    s = str(input())
    upper = 0
    lower = 0
    for char in s:
       if char.isupper():
        upper += 1
       elif char.islower():
        lower += 1
    print(f"Uppercase count: {upper}")
    print(f"Lowercade count: {lower}")

lower_upper_num()