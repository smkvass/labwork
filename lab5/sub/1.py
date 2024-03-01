#Replace every white-space character with the number 9:
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)