import re
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space position:", x.start())