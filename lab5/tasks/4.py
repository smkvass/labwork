#write a python program to find sequences of one upper case letter
#followed by lower case letters
import re
x = str(input("Enter a string: "))
check = re.compile(r'[A-Z]+[a-z]+')
res = check.findall(x)

if res:
    print("Sequences found", res)
else:
    print("No sequences found")
