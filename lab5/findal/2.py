#Return an empty list if no match was found:
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)