#write a python program that mathes a string that has an 'a'
#followed by two to three 'b'
import re
x = str(input("Enter a string:"))
check = re.search("a.{2,3}b", x)


if check:
    print("We have a match!")
else:
    print("No match")
