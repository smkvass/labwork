#Print a list of all matches:
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)