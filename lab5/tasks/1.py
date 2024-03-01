#write a python program that mathes a string that has an 'a'
#followed by zero or more 'b's
import re
x = str(input("Enter a string:"))
check = re.search("a*b", x)


if check:
    print("We have a match!")
else:
    print("No match")