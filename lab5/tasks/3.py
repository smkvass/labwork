#write a python program to find sequences of lowercase letters 
#joined with a underscore
import re
x = str(input("Enter a string: "))
check = re.compile(r'[a-z]+_[a-z]+')
res = check.findall(x)

if res:
    print("Sequences found", res)
else:
    print("No sequences found")