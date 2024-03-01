#write a python program to split a string at uppercase letters
import re 
"""
x = input("Enter a string: ")
split = [char for char in re.split('[A-Z][a-z]', x)if char]

print(split)
"""
def split_strings(string):
    result = ' '.join([char for char in string if char.isupper()])
    return result


x = str(input("Enter your strings: "))
res = split_strings(x)
print("Result is:", res)