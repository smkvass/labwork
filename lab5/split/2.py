#Split the string only at the first occurrence:
import re
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)