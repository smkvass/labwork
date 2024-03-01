#write a python program that matches a string that has an 'a'
#followed by anything, ending in 'b'
import re
x = str(input("Enter string:"))
check = re.compile(r'a.*b$')
res  = check.findall(x)

if res:
    print("Found")
else:
    print("Not found")