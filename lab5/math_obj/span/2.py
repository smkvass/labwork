#print the string passed into the function
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string) 