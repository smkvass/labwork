#write python program to replace all occurrences of space, 
# comma, or dot with a colon
import re
def replace(input_str):
    chars = [' ', ',', '.']
    for char in chars:
        input_str = input_str.replace(char, ':')
    return input_str

text = str(input("Enter a text: "))
result = replace(text)
print("New text: ", result)