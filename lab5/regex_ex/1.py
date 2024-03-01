import re

def smth(string):
    pattern = pattern.compile(r'a(b*)')
    match = pattern.fullmatch(string)
    
    if match:
        return True
    else:
        return False
    
strring = input("Input string: ")
result = smth(strring)

if result:
    print("Condition corresponds")
else:
    print("String doesn't correspond to condition")