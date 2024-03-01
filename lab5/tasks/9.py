#write a python program to insert spaces between words 
#starting with capital letters
import re
def space(x):
    res = ''
    for char in x:
        if char.isupper() and res:
           res += ' '
        res += char
    return res

string = str(input("Enter strings: "))
result = space(string)
print(result)